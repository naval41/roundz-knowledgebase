# Email Infrastructure Inventory

Last updated: 2026-09-05 (final — mailboxes live)

## Summary

| Domain | Mail Provider | DNS Host | MX Status | Purpose |
|---|---|---|---|---|
| `roundz.ai` (root) | Namecheap (Private Email) | AWS Route 53 (`roundz` profile, zone `Z052953399X0158UENH1`) | Active on Namecheap — **not repointed to Zoho** | Primary brand domain, existing Namecheap mailbox(es) |
| `mail.roundz.ai` | Zoho Mail (Workplace Standard, 30GB, Yearly) | AWS Route 53 (same zone) | Active on Zoho | Primary Zoho org domain; general outreach mailbox |
| `send.roundz.ai` | Zoho Mail (same org) | AWS Route 53 (same zone) | Verified — MX/SPF/DKIM live and confirmed via public resolvers | Dedicated cold-email sending subdomain, isolates deliverability risk from `mail.roundz.ai` and `roundz.ai` |

## Mailboxes

Final state: **two mailboxes**, both live.

| Mailbox | Domain | Type | Role | License Cost |
|---|---|---|---|---|
| `outreach@mail.roundz.ai` | mail.roundz.ai | Primary mailbox (Super Admin) | Administrator | ₹1,188/year (1 license) |
| `navneet@send.roundz.ai` | send.roundz.ai | Separate mailbox, created 2026-09-05 | Administrator | ₹1,188/year (2nd license, purchased) |
| roundz.ai mailbox(es) | roundz.ai | Hosted on Namecheap Private Email | — | Billed separately via Namecheap, not Zoho |

## Zoho org details

- **Org name**: Roundz.ai
- **Plan**: Workplace Standard, 30GB, Yearly
- **Super Admin**: `outreach@mail.roundz.ai`
- **Total licenses**: 2 (both in use — `outreach@mail.roundz.ai`, `navneet@send.roundz.ai`)
- **Cost**: ₹2,376/year total (2 licenses × ₹1,188/year). Second license purchased 2026-09-05 for ₹1,386.48 (prorated amount + tax, charged immediately; full ₹1,188/year applies from next renewal)
- **Renewal date**: 01/09/27
- **Domains verified in this org**: `mail.roundz.ai` (primary), `send.roundz.ai` (secondary, added and fully verified 2026-09-05)
- **`roundz.ai` (root)**: intentionally **not added** to this Zoho org, to avoid any risk to the existing Namecheap-hosted mail on that domain. Its SPF record still references `spf.privateemail.com` (Namecheap), confirming it's live there.

## DNS records added for `send.roundz.ai` (Route 53, `roundz.ai` zone)

Added via AWS CLI (`roundz` profile) on 2026-09-05, matching the existing `mail.roundz.ai` record pattern (TTL 300):

- `send.roundz.ai.` — TXT — Zoho domain verification (superseded after verification)
- `send.roundz.ai.` — MX — `10 mx.zoho.in.`, `20 mx2.zoho.in.`, `50 mx3.zoho.in.`
- `send.roundz.ai.` — TXT (SPF) — `v=spf1 include:zoho.in ~all`
- `zmail._domainkey.send.roundz.ai.` — TXT (DKIM)

All records confirmed resolving correctly via Google (8.8.8.8), Cloudflare (1.1.1.1), and Quad9 (9.9.9.9) public resolvers, and verified green in Zoho's own domain check.

DMARC and BIMI records were not yet duplicated for `send.roundz.ai` (existing pattern on `mail.roundz.ai` includes `_dmarc.mail.roundz.ai` and `default._bimi.mail.roundz.ai` — consider adding equivalents once `send.roundz.ai` is in active sending use).

## Cost-conscious strategy — final outcome

- Adding a **domain** to the Zoho org (verification only) was **free** — no per-domain charge, only per-mailbox licenses are billed.
- Final decision: two distinct mailboxes (`outreach@mail.roundz.ai`, `navneet@send.roundz.ai`) — no alias approach used.
- Second license purchased 2026-09-05: **₹1,386.48 charged immediately** (prorated for the remaining subscription cycle + tax), bringing the org to 2 licenses at **₹2,376/year total** going forward.
- `navneet@send.roundz.ai` was created with the **Administrator** role (by explicit choice), not restricted to a lower-privilege User role.

## Rationale for the subdomain approach

- Cold outreach volume can degrade sender reputation; isolating it on `send.roundz.ai` protects `mail.roundz.ai` and the root `roundz.ai` domain's deliverability if `send.roundz.ai` ever gets spam-flagged.
- Cost to isolate reputation this way is effectively zero (DNS + free domain verification), versus buying a second full domain (~$10-15/yr) for the same isolation benefit.
