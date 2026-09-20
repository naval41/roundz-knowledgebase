# Zoho sending scripts

`zoho_send.py` sends mail through the Zoho Mail API as any configured sender.
Python 3 stdlib only — nothing to install.

## Why this exists

`navneet@send.roundz.ai` is a separate Zoho user whose mailbox is *delegated* to
Vivek. Delegation is a Zoho Mail UI feature: it does not extend to API tokens, so
Vivek's token rejects sends from that address with:

```
500 Internal Error — "Operation not permitted"
```

The fix is one OAuth grant per mailbox. Each sender in the config is an
independent account with its own credentials.

## One-time setup, per mailbox

Do this twice: once signed in as `vivek@mail.roundz.ai`, once as
`navneet@send.roundz.ai`. The account you are signed into is the mailbox the
token can send as — that is the whole point, so check the top-right avatar first.

1. Go to https://api-console.zoho.in/ (`.in` — the org is on the India DC).
2. **Add Client → Self Client → Create**. Note the **Client ID** and **Client Secret**.
3. Open the **Generate Code** tab and enter:
   - Scope: `ZohoMail.messages.CREATE,ZohoMail.accounts.READ`
   - Time Duration: 10 minutes
   - Scope Description: anything (e.g. `warmup sending`)
4. Pick the portal/account when prompted, then **Create**. Copy the code — it is
   single-use and expires in 10 minutes.
5. Exchange it for a refresh token (run within those 10 minutes):

   ```bash
   curl -s -X POST https://accounts.zoho.in/oauth/v2/token \
     -d grant_type=authorization_code \
     -d client_id=YOUR_CLIENT_ID \
     -d client_secret=YOUR_CLIENT_SECRET \
     -d code=THE_GENERATED_CODE
   ```

   Keep `refresh_token` from the response. It does not expire unless revoked;
   `access_token` is short-lived and the script refreshes it automatically.

Then create the config, which lives outside the repo:

```bash
mkdir -p ~/.config/roundz
cp scripts/zoho_senders.example.json ~/.config/roundz/zoho_senders.json
chmod 600 ~/.config/roundz/zoho_senders.json
# edit in the two sets of credentials
```

## Verify before sending

```bash
python3 scripts/zoho_send.py --list-senders
python3 scripts/zoho_send.py --sender navneet --batch warmup.json --dry-run
```

`--dry-run` refreshes the token and resolves the account id, so it fails loudly
on a bad grant without sending anything. If a token belongs to the wrong
mailbox, the script says so and lists the addresses that token *can* send as.

## Sending

```bash
# one message
python3 scripts/zoho_send.py --sender vivek \
  --to someone@example.com --subject "Quick hello" --body-file note.txt

# a batch, 20s apart by default
python3 scripts/zoho_send.py --sender navneet --batch warmup.json --delay 30
```

A batch file is a JSON list:

```json
[
  {"to": "someone@example.com", "subject": "Quick hello", "body": "Hi,\n\n...\n\nBest,\nNavneet"}
]
```

Exit code is non-zero if any message failed; failures are listed per recipient
and do not stop the remaining sends.

## Notes

- Never commit `zoho_senders.json` or any real refresh token. `.gitignore`
  covers the usual paths, but the file belongs in `~/.config/roundz/`.
- Warm-up traffic should be paced and two-way. Spread sends across the day and
  have some receiving accounts reply — inbound engagement moves reputation more
  than volume does.
- Region matters: this org is on the India DC, so hosts are `accounts.zoho.in`
  and `mail.zoho.in`. The `.com` endpoints will return auth errors.
