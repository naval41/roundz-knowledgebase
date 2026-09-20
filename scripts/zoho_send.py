#!/usr/bin/env python3
"""Send mail through the Zoho Mail API as any configured sender.

Each sender is an independent Zoho account with its own OAuth credentials, so
mailboxes that are merely *delegated* in the Zoho UI (and therefore rejected by
a delegate's token with "Operation not permitted") each get their own grant.

Config is JSON, default ~/.config/roundz/zoho_senders.json, see
scripts/zoho_senders.example.json. Never commit the real file.

Usage:
  zoho_send.py --sender vivek --to a@b.com --subject "Hi" --body-file note.txt
  zoho_send.py --sender navneet --batch warmup.json
  zoho_send.py --sender navneet --batch warmup.json --dry-run
  zoho_send.py --list-senders

A batch file is a JSON list of {"to", "subject", "body"} objects.
"""

import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_CONFIG = os.path.expanduser("~/.config/roundz/zoho_senders.json")

# Zoho is region-partitioned; India accounts live on .in, not .com.
DEFAULT_ACCOUNTS_HOST = "https://accounts.zoho.in"
DEFAULT_MAIL_HOST = "https://mail.zoho.in"

# Warm-up traffic should not arrive as an obvious burst.
DEFAULT_DELAY_SECONDS = 20.0


class ZohoError(RuntimeError):
    pass


def _post_form(url, fields):
    body = urllib.parse.urlencode(fields).encode()
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    return _read_json(req)


def _read_json(req):
    try:
        with urllib.request.urlopen(req, context=ssl.create_default_context()) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")
        raise ZohoError(f"HTTP {exc.code} from {req.full_url}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise ZohoError(f"Could not reach {req.full_url}: {exc.reason}") from exc


class Sender:
    """One Zoho mailbox: its credentials, access token and account id."""

    def __init__(self, name, conf):
        self.name = name
        for key in ("client_id", "client_secret", "refresh_token", "from_address"):
            if not conf.get(key):
                raise ZohoError(f"sender '{name}' is missing '{key}' in the config")
        self.client_id = conf["client_id"]
        self.client_secret = conf["client_secret"]
        self.refresh_token = conf["refresh_token"]
        self.from_address = conf["from_address"]
        self.display_name = conf.get("display_name", "")
        self.accounts_host = conf.get("accounts_host", DEFAULT_ACCOUNTS_HOST)
        self.mail_host = conf.get("mail_host", DEFAULT_MAIL_HOST)
        self._token = None
        self._account_id = conf.get("account_id")

    @property
    def token(self):
        if self._token is None:
            data = _post_form(
                f"{self.accounts_host}/oauth/v2/token",
                {
                    "refresh_token": self.refresh_token,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "grant_type": "refresh_token",
                },
            )
            if "access_token" not in data:
                raise ZohoError(
                    f"sender '{self.name}': no access_token in refresh response: {data}"
                )
            self._token = data["access_token"]
        return self._token

    def _request(self, url, payload=None):
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(url, data=data, method="POST" if data else "GET")
        req.add_header("Authorization", f"Zoho-oauthtoken {self.token}")
        if data:
            req.add_header("Content-Type", "application/json")
        return _read_json(req)

    @property
    def account_id(self):
        """Resolve the account id, and verify from_address is actually sendable."""
        if self._account_id is None:
            data = self._request(f"{self.mail_host}/api/accounts")
            accounts = data.get("data") or []
            if not accounts:
                raise ZohoError(f"sender '{self.name}': token returned no accounts")
            wanted = self.from_address.lower()
            for account in accounts:
                sendable = {
                    entry.get("fromAddress", "").lower()
                    for entry in account.get("sendMailDetails", [])
                }
                if wanted in sendable:
                    self._account_id = account["accountId"]
                    break
            else:
                available = sorted(
                    entry.get("fromAddress", "")
                    for account in accounts
                    for entry in account.get("sendMailDetails", [])
                )
                raise ZohoError(
                    f"sender '{self.name}': {self.from_address} is not sendable by this "
                    f"token. Available: {', '.join(available) or '(none)'}. A delegated "
                    f"mailbox needs its own OAuth grant."
                )
        return self._account_id

    def send(self, to_address, subject, content, mail_format="plaintext", draft=False):
        payload = {
            "fromAddress": (
                f"{self.display_name} <{self.from_address}>"
                if self.display_name
                else self.from_address
            ),
            "toAddress": to_address,
            "subject": subject,
            "content": content,
            "mailFormat": mail_format,
        }
        if draft:
            payload["mode"] = "draft"  # saved to Drafts, nothing leaves the mailbox
        result = self._request(
            f"{self.mail_host}/api/accounts/{self.account_id}/messages", payload
        )
        status = (result.get("status") or {}).get("code")
        if status != 200:
            raise ZohoError(f"send to {to_address} failed: {result}")
        return (result.get("data") or {}).get("messageId", "")


def load_senders(path):
    if not os.path.exists(path):
        raise ZohoError(
            f"no config at {path}. Copy scripts/zoho_senders.example.json there "
            f"and fill in the credentials (chmod 600)."
        )
    with open(path) as handle:
        raw = json.load(handle)
    return {name: Sender(name, conf) for name, conf in raw.items()}


def load_batch(path):
    with open(path) as handle:
        items = json.load(handle)
    if not isinstance(items, list):
        raise ZohoError(f"{path}: expected a JSON list of messages")
    for index, item in enumerate(items, 1):
        missing = [key for key in ("to", "subject", "body") if not item.get(key)]
        if missing:
            raise ZohoError(f"{path}: message {index} is missing {', '.join(missing)}")
    return items


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--sender", help="sender key from the config")
    parser.add_argument("--list-senders", action="store_true")
    parser.add_argument("--to")
    parser.add_argument("--subject")
    parser.add_argument("--body")
    parser.add_argument("--body-file")
    parser.add_argument("--batch", help="JSON list of {to, subject, body}")
    parser.add_argument("--html", action="store_true", help="send as HTML")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS,
                        help="seconds between batch sends (default: %(default)s)")
    parser.add_argument("--dry-run", action="store_true",
                        help="validate credentials and print what would be sent")
    parser.add_argument("--draft", action="store_true",
                        help="save each message to the sender's Drafts folder instead of sending")
    args = parser.parse_args(argv)

    try:
        senders = load_senders(args.config)
    except ZohoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.list_senders:
        for name, sender in sorted(senders.items()):
            print(f"{name}\t{sender.from_address}")
        return 0

    if not args.sender:
        parser.error("--sender is required (or use --list-senders)")
    if args.sender not in senders:
        print(
            f"error: unknown sender '{args.sender}'. Known: "
            f"{', '.join(sorted(senders))}",
            file=sys.stderr,
        )
        return 2
    sender = senders[args.sender]

    if args.batch:
        try:
            messages = load_batch(args.batch)
        except (ZohoError, OSError, json.JSONDecodeError) as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2
    else:
        if not (args.to and args.subject):
            parser.error("--to and --subject are required without --batch")
        if args.body_file:
            with open(args.body_file) as handle:
                body = handle.read()
        elif args.body is not None:
            body = args.body
        else:
            parser.error("one of --body or --body-file is required")
        messages = [{"to": args.to, "subject": args.subject, "body": body}]

    mail_format = "html" if args.html else "plaintext"

    try:
        # Touch the account id once up front so a bad grant fails before any send.
        account_id = sender.account_id
    except ZohoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"sender {sender.name} <{sender.from_address}> account {account_id}")
    if args.dry_run:
        for message in messages:
            print(f"  [dry-run] -> {message['to']}: {message['subject']}")
        print(f"{len(messages)} message(s) validated, nothing sent.")
        return 0

    sent = 0
    failures = []
    for index, message in enumerate(messages, 1):
        try:
            message_id = sender.send(
                message["to"], message["subject"], message["body"], mail_format,
                draft=args.draft,
            )
            sent += 1
            verb = "drafted" if args.draft else "sent"
            print(f"  [{index}/{len(messages)}] {verb} -> {message['to']} ({message_id})")
        except ZohoError as exc:
            failures.append((message["to"], str(exc)))
            print(f"  [{index}/{len(messages)}] FAILED -> {message['to']}: {exc}",
                  file=sys.stderr)
        if index < len(messages) and args.delay > 0:
            time.sleep(args.delay)

    print(f"{sent}/{len(messages)} {'drafted' if args.draft else 'sent'} from {sender.from_address}")
    if failures:
        print(f"{len(failures)} failed:", file=sys.stderr)
        for address, reason in failures:
            print(f"  {address}: {reason}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
