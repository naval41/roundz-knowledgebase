# Email Infrastructure Inventory

Last updated: 2026-09-05

## Summary

| Domain | Mail Provider | DNS Host | MX Status | Purpose |
|---|---|---|---|---|
| `roundz.ai` (root) | Namecheap (Private Email) | AWS Route 53 (`roundz` profile, zone `Z052953399X0158UENH1`) | Active on Namecheap — **not repointed to Zoho** | Primary brand domain, existing Namecheap mailbox(es) |
| `mail.roundz.ai` | Zoho Mail (Workplace Standard, 30GB, Yearly) | AWS Route 53 (same zone) | Active on Zoho | Primary Zoho org domain; general outreach mailbox |
| `send.roundz.ai` | Zoho Mail (same org) | AWS Route 53 (same zone) | MX/SPF/DKIM added, verification in progress | Dedicated cold-email sending subdomain, isolates deliverability risk from `mail.roundz.ai` and `roundz.ai` |

## Mailboxes

Final target state: **two mailboxes only** — no alias on `send.roundz.ai`.

| Mailbox | Domain | Type | License Cost |
|---|---|---|---|
| `outreach@mail.roundz.ai` | mail.roundz.ai | Primary mailbox (Super Admin) | ₹1,188/year (1 license, included in current plan) |
| `navneet@send.roundz.ai` (planned, not yet purchased) | send.roundz.ai | Separate mailbox | +₹1,188/year (new license) — pending DNS verification of `send.roundz.ai`, then purchase approval |
| roundz.ai mailbox(es) | roundz.ai | Hosted on Namecheap Private Email | Billed separately via Namecheap, not Zoho |

## Zoho org details

- **Org name**: Roundz.ai
- **Plan**: Workplace Standard, 30GB, Yearly
- **Super Admin**: `outreach@mail.roundz.ai`
- **Total licenses**: 1 (currently fully used)
- **Cost**: ₹1,188/year for the 1 license (wallet credit available: ₹142.56 as of 2026-09-05)
- **Renewal date**: 01/09/27
- **Domains verified in this org**: `mail.roundz.ai` (primary), `send.roundz.ai` (secondary, added 2026-09-05)
- **`roundz.ai` (root)**: intentionally **not added** to this Zoho org yet, to avoid any risk to the existing Namecheap-hosted mail on that domain. Its SPF record still references `spf.privateemail.com` (Namecheap), confirming it's live there.

## DNS records added for `send.roundz.ai` (Route 53, `roundz.ai` zone)

Added via AWS CLI (`roundz` profile) on 2026-09-05, matching the existing `mail.roundz.ai` record pattern (TTL 300):

- `send.roundz.ai.` — TXT — Zoho domain verification (superseded after verification)
- `send.roundz.ai.` — MX — `10 mx.zoho.in.`, `20 mx2.zoho.in.`, `50 mx3.zoho.in.`
- `send.roundz.ai.` — TXT (SPF) — `v=spf1 include:zoho.in ~all`
- `zmail._domainkey.send.roundz.ai.` — TXT (DKIM)

DMARC and BIMI records were not yet duplicated for `send.roundz.ai` (existing pattern on `mail.roundz.ai` includes `_dmarc.mail.roundz.ai` and `default._bimi.mail.roundz.ai` — consider adding equivalents once `send.roundz.ai` is verified and in active use).

## Cost-conscious strategy

- Adding a **domain** to the Zoho org (verification only) is **free** — no per-domain charge, only per-mailbox licenses are billed.
- Final decision: two distinct mailboxes only (`outreach@mail.roundz.ai`, `navneet@send.roundz.ai`) — no alias approach. This means the second license (+₹1,188/year) **will** be purchased once `send.roundz.ai` DNS verification completes, pending explicit go-ahead before the purchase.

## Rationale for the subdomain approach

- Cold outreach volume can degrade sender reputation; isolating it on `send.roundz.ai` protects `mail.roundz.ai` and the root `roundz.ai` domain's deliverability if `send.roundz.ai` ever gets spam-flagged.
- Cost to isolate reputation this way is effectively zero (DNS + free domain verification), versus buying a second full domain (~$10-15/yr) for the same isolation benefit.
