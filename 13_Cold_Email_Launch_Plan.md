# 13 — Cold Email Launch Plan (Roundz AI)

> **Written:** 2026-07-29 (Wed). **Binding constraint:** the sending mailbox `outreach@mail.roundz.ai` was created **today**. Nothing goes out at volume before **Tue 18 Aug 2026**.
>
> **Inputs:** `10_Founding_Sales_Playbook.md` (Kazanjy), `11_Cold_Email_Sequence.md` (draft sequence), `12_Apollo_Contact_List.md` (24 contacts), `04-sales-toolkit/Cold_Outreach_Cadence_and_ICP.md`, `01-base-knowledge/Product_Ground_Truth.md` (honesty guardrails), roundz.ai.

---

## PART 0 — The three things that matter most

Everything below expands on these. If you read nothing else:

1. **Your list is not the ICP you wrote down — and that may be good news.** 15 of 24 contacts (63%) are at **IT staffing / consulting / services firms**, not the Series A–C product companies in your ICP doc. Only **4 are true "deer."** Don't force one message onto both. Run them as **two separate segments with two different narratives**, and treat the staffing segment as a serious candidate beachhead — see Part 2.
2. **A brand-new mailbox is the whole schedule.** A domain that started sending yesterday has zero reputation. Send 24 cold emails from it next week and you burn `mail.roundz.ai` before you've learned anything. **14-day warmup minimum.** Use those 14 days to do the work Kazanjy actually prescribes: build a real demand-signified list (Part 4).
3. **24 contacts cannot teach you anything statistically.** At a good 10% reply rate that's 2.4 replies. This batch is a **qualitative message test**, not a campaign. Judge it on *what people say back*, not on conversion math. The scaling gate (15–30% meeting→won) needs ~10x this volume.

---

## PART 1 — Fix the mailbox before anything else

### 1.1 Change the sending address (do this today, while it's free)

`outreach@mail.roundz.ai` is a **role address**. Role-based mailboxes (`outreach@`, `sales@`, `info@`, `hello@`) are scored harder by every major filter and read as bulk to a human. Kazanjy's entire email doctrine is *peer-to-peer, plainspoken, CEO-to-CEO* — that starts with the From line.

**Create `vivek@mail.roundz.ai`** (or whatever name will actually reply to responses) and make it the primary sender. Keep `outreach@` as an alias/catch-all if you like. Doing this on day 1 costs nothing; doing it after 3 weeks of warmup means starting warmup over.

> Display name: `Vivek P` — not `Roundz AI` and not `Roundz Sales`.

### 1.2 DNS — verify all four records on the **subdomain**

`11_Cold_Email_Sequence.md` notes DMARC is already in Route 53 but MX/SPF/DKIM were pending a provider. Now that the box exists, confirm each of these resolves **for `mail.roundz.ai`**, not just for `roundz.ai`:

| Record | Host | What it must be |
|---|---|---|
| **MX** | `mail.roundz.ai` | Your provider's MX (Google Workspace / Microsoft 365) |
| **SPF** | `mail.roundz.ai` TXT | `v=spf1 include:<provider> -all` — one record only, `-all` not `~all` |
| **DKIM** | provider selector | 2048-bit, enabled in the provider admin console (Google does *not* enable it by default) |
| **DMARC** | `_dmarc.mail.roundz.ai` TXT | `v=DMARC1; p=none; rua=mailto:dmarc@roundz.ai; adkim=r; aspf=r` |

Start DMARC at `p=none` and read the aggregate reports for two weeks; move to `p=quarantine` only once SPF/DKIM alignment is clean. A `p=reject` on an unverified setup silently kills your own mail.

**Verify with:** `dig TXT mail.roundz.ai`, `dig TXT _dmarc.mail.roundz.ai`, then send a test to [mail-tester.com](https://www.mail-tester.com) and require **10/10** before Batch 1.

### 1.3 Warmup schedule (starts today, 29 Jul)

Run an automated warmup (Instantly, Smartlead, Warmy, or MailReach) on the new mailbox from today. Volume ramp:

| Days | Dates | Warmup traffic/day | Real cold sends/day |
|---|---|---|---|
| 1–7 | Jul 29 – Aug 4 | 5 → 20 (auto-ramp) | **0** |
| 8–14 | Aug 5 – Aug 11 | 20 → 40 | **0** |
| 15–20 | Aug 12 – Aug 17 | 40, steady | **0** — send 3–5 *genuine* 1:1 emails/day (network, advisors, warm intros) |
| 21+ | Aug 18 onward | keep warmup running at 30–40 | **8–12/day, hard ceiling 25** |

Never exceed **25–30 cold sends/day from one mailbox**, warm or not. Your entire list is 24 people — this is not a constraint yet, but it will be after Part 4.

### 1.4 Sending tooling — go simple

For 24 contacts, **do not use a full sequencer.** Use Gmail/Outlook + a light mail-merge (Mailmeteor, GMass, or Mixmax). Reasons: sequencer IPs and tracking domains add deliverability risk you don't need, and manual sending forces the per-contact personalization that is the single biggest lever on reply rate.

**Turn open-tracking pixels OFF.** They measurably hurt inbox placement on cold domains, and open rates are unreliable anyway post-Apple MPP. You still get Kazanjy's instrumentation by using a **unique link per contact** — e.g. `cal.com/vivek/roundz?ref=falconx` — so Cal.com tells you exactly who clicked. That's a click-target without a pixel.

### 1.5 Pre-send hygiene

- **Re-verify all 24 emails** through NeverBounce or ZeroBounce before Batch 1. Apollo "verified" runs ~85–92% accurate; a bounce spike on a 3-week-old domain is fatal. Drop anything not `valid` — do not send to `catch-all` or `risky` on the first batch.
- **CAN-SPAM footer** on every email: a real physical mailing address + a plain-text opt-out line (`Don't want these? Reply "stop" and I'll remove you.`). No HTML unsubscribe widget — it screams bulk.
- **India (DPDP Act 2023):** B2B outreach to a work address is fine; honor opt-outs immediately and don't retain data beyond purpose. No consent gate required for this use.
- **Email 1 should contain zero links.** On a fresh domain, a link-free first touch materially improves placement. Introduce the calendar link from Email 2 onward.

---

## PART 2 — Detailed analysis of the Apollo list

### 2.1 The headline finding

Your Apollo filter (`TA/Recruiting titles` + `Information Technology & Services` + `<500 employees`) did exactly what you asked — but **"Information Technology & Services" is the industry code that IT staffing, consulting, and outsourcing firms self-classify under.** It is not the code product companies use (that's "Software Development" / "Internet"). So the filter systematically selected *against* your written ICP.

| Segment | Count | Fit vs. written ICP |
|---|---|---|
| **A — True deer** (funded product companies, eng-heavy) | 4 | On-ICP |
| **B — Marginal** (too small, or too big, or thin eng) | 3 | Off-ICP but sendable |
| **C — IT staffing / services / consulting** | 15 | **Off-ICP — different narrative required** |
| **D — Skip** (rabbits / not a fit) | 2 | Remove |

### 2.2 Tier A — send these first (4)

| Contact | Company | Why it qualifies |
|---|---|---|
| **Jess Schuster** — Head of TA & People Ops | **Iterative Health** | Series C, **$77M raised Apr 2026**, ~168–250 staff, AI/ML-heavy (FDA-cleared endoscopy AI). Fresh capital + AI hiring = live, funded pain. The single best name on this list. Note: company is Cambridge, MA — Apollo's "Long Beach, NY" is her personal location. |
| **Owen Luddy** — Head of US Talent Acquisition | **FalconX** | Crypto prime broker, heavily funded, engineering-dominant, remote-first hiring across geos → high fraud/impersonation exposure. Slightly above the 250-person band; treat as a large deer. |
| **Eshita Motiani** — People Ops & TA Manager | **Madhive** | CTV adtech, 201–500, NYC HQ with a **Pune, India engineering office**. This is the ideal shape: US product company hiring engineers in India at volume, remotely. ⚠️ Apollo lists her as "Baramati, India" — almost certainly bad data; she's likely Pune. Verify on LinkedIn before personalizing. |
| **Nicole Minaudo** — TA Manager \| People Ops | **Detroit Labs** | ~100-person software studio, hires developers continuously across client projects. Screening volume is genuinely high; decision cycle short. |

### 2.3 Tier B — send, lower expectations (3)

| Contact | Company | Read |
|---|---|---|
| **Ashley Pinder** | **SuperCircle** | Real company — **$24M Series A, Dec 2025**, 75+ brand customers. But textile-waste logistics; the engineering team is likely <15. Low screening volume. Worth one touch because the funding signal is fresh. |
| **Jason Zerega** — Head of TA & Principal Recruiter | **Intersection Co.** | Urban media / smart city. Has engineering, but hiring is cyclical and the company has been through restructuring. Middling. |
| **Utkarsh Mishra** — TA Lead | **OLX India** | A genuine product company with a large Gurgaon engineering org and real screening volume — but it's a **small elephant**. Procurement, security review, incumbent tools. Great logo if it lands; will not move on a founder-led timeline. Send it, expect a long cycle. |

### 2.4 Tier C — the IT staffing / services segment (15)

**US (5):** Metahorizon (Manish Bisht) · Connvertex Technologies (Pooja Mishra) · Ingenworks (Nagapavankumar Vankadari) · Osi Vision (Cory Cavender) · Mphasis Silverline (Jason Litman)

**India (10):** AvanteNow (Reshma Ramachandran) · ConglomerateIT (Archana Koul) · American Chase (Harsh Sen) · Intone (Ashok Andras) · WalkingTree Technologies (Damini Bilandani) · Techila Global Services (Kranti Bhosale) · DeUS Tech Services (Shikha Narayanan) · ZUCOL (Damini Bhagat) · Virisha (Abhinav Yadav) · finspectra (Juhi Duggal)

**This is not a junk segment. Read it carefully before you discount it.**

Arguments *for* staffing/services as a beachhead:

- **Screening volume is 10–50x a 100-person product company.** A staffing firm may screen 500+ engineers a month. Roundz meters per candidate-interview (1 credit = 1 interview) — volume *is* the revenue model.
- **The pain is P&L, not opportunity cost.** Recruiter and bench-engineer hours spent screening are direct COGS. That makes the ROI conversation concrete rather than hypothetical — the hardest thing to get right with a product-company CTO.
- **The fraud problem is acute, public, and 2026-current.** In **June 2026 a leading Indian IT services firm deferred assessments for 20,000+ applicants** after detecting mass impersonation. Hyderabad proxy rings have serviced 200+ candidates/year at ₹30–40k a head for TCS/Infosys/Wipro vendor roles. In IT/ITeS, **79% of employment-fraud incidents involve previously employed candidates** — not freshers. This is the strongest "why now" you have with this audience, and it is far more visceral to them than the agentic-coding wedge.
- **The buyer is exactly who's on your list.** TA Head / TA Manager at a 200-person staffing firm *owns* the screening budget. No CTO required, no committee.
- **A proxy hire that reaches the end client is an account-losing event.** That's the emotional hook: not "save recruiter time," but **"a proxy candidate you submitted costs you the client."**

Arguments *against*:

- **Willingness to pay is much lower**, especially India-side. Expect to be negotiating in the hundreds-of-dollars-per-month range, not the `$24,000/yr` placeholder in `Pilot_Offer_and_Pricing.md`.
- They may push for **white-label / reseller** terms, which is a different product decision.
- They are a **middleman persona** — they don't own the hiring outcome, so "quality of hire" arguments land softer than "throughput and trust."
- Razorpay is your only rail. Fine for India; check it works for the US staffing firms.

**Recommendation:** send to this segment, but with a **purpose-built narrative** (Part 3.2) and an explicit goal of *learning whether the ACV is viable*, not of closing. If two or three of these convert to paid pilots at any price, you have discovered a faster beachhead than the Series A–C product companies — and Kazanjy's whole point in Epoch 1 is that you find the ICP by talking, not by declaring it.

### 2.5 Tier D — remove (2)

| Contact | Company | Why |
|---|---|---|
| Tia Baker | **Aerial** (aerialops.io) | Pre-seed, **$2M raised May 2024**, ~10 people, legal-doc AI. Also actually Seattle, not Denver — Apollo geo is wrong. Classic rabbit: no screening volume, no budget. |
| Marie Gupta | **Canundra** | Business/enterprise-transformation consultancy, no meaningful engineering hiring. Not a fit. |

Removing these two costs you nothing and protects your bounce/complaint rate.

### 2.6 Data-quality flags to fix in `12_Apollo_Contact_List.md`

Three of 24 locations are wrong (Madhive/Baramati, Aerial/Denver, Iterative Health/Long Beach). That's ~12% error on a field you can see — assume similar error on fields you can't. **Verify every Tier A/B contact on LinkedIn before writing their email.** Referencing the wrong city or wrong company in a personalized line is worse than sending nothing.

---

## PART 3 — The messaging, rewritten

### 3.1 What's wrong with `11_Cold_Email_Sequence.md` as drafted

It's a solid draft and it correctly targets the TA persona. Three fixes before it ships:

**(a) It breaks your own honesty guardrails.** `Product_Ground_Truth.md` §2–3 is explicit: the `92% fraud detection` and `$555K/yr` figures are **third-party research estimates, not Roundz-measured outcomes**, and must be attributed as such. But Email 3 says *"with about 92% detection accuracy"* attributed to Roundz, and Email 4 states the `$555K` as fact. Email 2's *"10x more candidates"* is likewise a marketing figure with no customer data behind it. **Rewrite all three.** A TA head at an IT firm will ask "says who?" on the first call, and an unsourced number is how you lose a deal you'd otherwise win. This is also the cheapest possible fix.

**(b) It omits your best asset.** `Product_Ground_Truth.md` §4 calls the **agentic-coding round** — where the candidate solves *with* an AI copilot and you score how they *direct* it (prompt quality, decomposition, judgment, token efficiency) — "category-defining," something HackerRank/Karat/CodeSignal don't have, and "the #1 GTM wedge." It appears nowhere in the sequence. For Tier A it should be the *lead*.

**(c) It sends the same narrative to both segments.** A Series C healthtech Head of TA and a Hyderabad staffing TA lead have different problems. Split it.

### 3.2 Two narratives

| | **Segment 1 — Product companies (Tier A+B, n=7)** | **Segment 2 — IT staffing / services (Tier C, n=15)** |
|---|---|---|
| **Core pain** | Screening signal has collapsed — candidates pass the take-home with AI, then can't reason live | Proxy candidates and AI-assisted fakes reach your client's interview and cost you the account |
| **Why now** | Engineers now *direct* AI rather than hand-write code; the interview hasn't caught up | June 2026: a major Indian IT firm deferred assessments for 20,000+ applicants over mass impersonation |
| **Lead with** | The **agentic-coding round** — the first interview that scores how a candidate directs an AI copilot | **Live proctored voice interview** — you see the reasoning happen, live, not a submitted artifact |
| **ROI frame** | Senior-engineer hours reclaimed; meet only the pre-vetted top ~20% | Recruiter/bench hours per submission; submit-to-interview ratio; client trust preserved |
| **Proof to offer** | Explainable level-aware rubric report, audited line by line | A flagged session — show them what a caught proxy actually looks like |
| **CTA** | 20-min look at how it fits their loop | "Want me to send a real sample report?" (lower friction) |
| **Expected ACV** | Pilot pack → annual, per `Pilot_Offer_and_Pricing.md` | Unknown — **this batch exists to find out** |

### 3.3 Segment 1 — Email 1 (Tier A, product companies)

Zero links. Under 130 words. One thought.

```
Subject: {Company}'s screen vs. candidates who use AI

Hi {First_Name},

Congrats on the {Series C / recent raise} — I imagine the engineering
hiring plan just got a lot bigger.

The reason I'm writing: most technical screens now tell you almost
nothing, because candidates clear them with AI and then can't reason
through the live round. Your engineers find out in week three.

We built Roundz around that. A live voice AI runs the actual interview
watching the candidate's code and whiteboard as they work — and one
round hands them an AI copilot on purpose, scoring how well they
*direct* it. Prompt quality, decomposition, judgment. Which is how your
team ships now anyway.

I'd rather show you a real report than describe it. Worth 20 minutes?

Vivek
Founder, Roundz
```

Per-contact personalization (the 5 minutes Kazanjy says returns 15x) — replace line 1 with something only true of them:
- **Iterative Health:** the $77M Series C (Apr 2026) + ML/clinical-AI roles → *"hiring ML engineers who can actually reason, not just prompt"*
- **FalconX:** remote hiring across geos → lead with identity/fraud exposure instead
- **Madhive:** NYC + Pune engineering split → *"screening candidates 10 time zones from the hiring manager"*
- **Detroit Labs:** client-project staffing → *"every new project means another screening sprint"*

### 3.4 Segment 2 — Email 1 (Tier C, staffing/services)

```
Subject: the proxy-candidate problem at {Company}

Hi {First_Name},

Straight to it: how are you verifying that the engineer on the video
call is the one who shows up on day one?

I ask because it's gotten bad enough to make the news — in June a major
Indian IT services firm deferred assessments for 20,000+ applicants
after finding widespread impersonation. For a firm submitting
candidates to clients, one proxy that gets through isn't a bad hire,
it's a lost account.

Roundz runs the first technical round as a live, proctored voice
interview — the AI talks to the candidate, watches their code and
design work as it happens, and flags gaze, tab-switching and
clipboard behaviour in the report. You see the reasoning happen
instead of grading a submitted artifact.

Would a real sample report be useful to look at?

Vivek
Founder, Roundz
```

Note the CTA: **"want a sample report?"** not "book 20 minutes." For a cold, price-sensitive, high-volume audience, an interest-ask converts better than a calendar-ask — and a "yes" gives you a warm thread to book the call inside.

### 3.5 Follow-ups (both segments)

Keep `11_`'s structure — Day 0 / 3 / 7 / 12 / 18, replying **into the same thread** so each bump drags them back to the personalized first email. Kazanjy's data: the 2nd email outperforms the 1st (~18% vs ~12%); replies hold through ~5 then decay; always end with a breakup.

**Every statistic must carry its source inline.** Correct forms:

- ✅ *"A bad engineering hire runs up to 30% of first-year salary to unwind (US Dept. of Labor / SHRM)."*
- ✅ *"Engineering leaders report losing roughly a third of the week to low-signal screening (Stripe, Developer Coefficient)."*
- ✅ *"In IT/ITeS, 79% of employment-fraud incidents involved previously employed candidates — not freshers."*
- ❌ *"Roundz catches 92% of fraud"* — not a measured Roundz outcome. Say **"our proctoring surfaces gaze, tab-switch and clipboard signals in every report"** and let the demo prove it.
- ❌ *"10x more candidates screened"* — no customer data yet. Say **"interviews run around the clock instead of waiting on an engineer's calendar."**

Never say Roundz **executes code or reports pass rates.** Say it **evaluates approach, complexity, and correctness of reasoning.**

---

## PART 4 — The work to do during the 14-day warmup

This is the most valuable part of the plan and the easiest to skip. You have two idle weeks; Kazanjy would spend all of them on list-building.

**Goal: 100–150 demand-signified accounts by Fri 14 Aug**, built by hand, not bought.

Filter for the compound target from `Cold_Outreach_Cadence_and_ICP.md` §1.1:

1. **Google the ATS boards** — `site:boards.greenhouse.io "software engineer"`, `site:jobs.lever.co "engineer"`, `site:jobs.ashbyhq.com`. Any company with **3+ live engineering reqs** is funded, time-boxed pain.
2. **Grep the JDs for the incumbent** — "complete a HackerRank / CodeSignal / Karat / Codility / take-home." That confirms attribute #5: a screening budget line already exists, so you're a replace, not a net-new spend.
3. **Funding triggers** — Crunchbase/Tracxn Series A–C, raised in the last 12 months, 50–250 headcount. Reach out 2–4 weeks post-raise.
4. **Sales Navigator lead search** inside those accounts: Head of Talent / Director TA / VP Eng / CTO, filtered to "changed jobs in last 90 days."

Log per account: `Company | HQ | Headcount | Eng % | Stage / last raise | # open eng reqs | Screening tool | ATS | Buyer | User | Signal notes`.

**Also finish during warmup:**
- [ ] Booking link live (Cal.com), 20-min slot, with per-contact `?ref=` tracking
- [ ] **A real sample rubric report as a PDF** — both sequences promise one; you need it in hand before anyone says yes
- [ ] A **2-minute Loom** of the agentic-coding round, unlisted on YouTube (Kazanjy: ship the rough video, don't wait for the polished explainer)
- [ ] Physical mailing address for the CAN-SPAM footer
- [ ] CRM or a Google Sheet with stage definitions and a **calendared next step per contact** — non-negotiable; pipelines die from missing next actions
- [ ] Decide the pilot price and stop calling it `[PLACEHOLDER]` — Kazanjy: charge from day one, price just under the incumbent (HackerRank ≈ $8–20k/yr; agencies at 20–30% of first-year salary)

---

## PART 5 — The calendar

| Date | Action |
|---|---|
| **Wed 29 Jul** | Create `vivek@mail.roundz.ai`. Verify MX/SPF/DKIM/DMARC on the subdomain. **Start warmup.** |
| **Thu 30 – Fri 31 Jul** | Re-verify all 24 emails (NeverBounce). Drop Tier D. Fix the 3 bad location fields. Rewrite the sequences per Part 3. |
| **Mon 3 – Fri 14 Aug** | Warmup runs untouched. **Build the 100–150 account list.** Ship the sample report, the Loom, the booking link. |
| **Mon 17 Aug** | mail-tester 10/10. Seed-test to personal Gmail / Outlook / Yahoo — confirm inbox, not Promotions. Final personalization pass on Tier A. |
| **Tue 18 Aug, 10:00 local** | **Batch 1: Tier A + B (7 contacts).** Sent individually, hand-personalized, no links. Tuesday 10am per Kazanjy. |
| **Tue 25 Aug** | **Batch 2: Tier C US (5).** Segment-2 narrative. Meanwhile Batch 1 follow-ups run on the D+3 / D+7 schedule. |
| **Tue 1 Sep, 10:00 IST** | **Batch 3: Tier C India (10).** Send on IST — Tue/Wed 10–11am. |
| **Fri 4 Sep** | **Review gate.** Read every reply. Decide: does the staffing narrative outperform the product narrative? |
| **Wk of 8 Sep** | Roll the winning narrative onto the 100–150 hand-built list at 10–15/day. |

---

## PART 6 — What "working" looks like

Benchmarks from `Cold_Outreach_Cadence_and_ICP.md` §10, with the honest caveat that n=22 measures nothing:

| Metric | Target | On 22 contacts |
|---|---|---|
| Bounce rate | <5% | **>1 bounce = stop and re-verify the list** |
| Reply rate (any) | 8–15% | ~2–3 replies |
| Positive replies | ≥30% of replies | ~1 |
| Meetings set | 3–8% | **1 meeting = this batch worked** |

**What to actually judge this batch on** — qualitative, and far more useful than the numbers:

1. Which **segment** replied at all? That's your beachhead signal.
2. Which **pain** did they echo back in their own words — AI-assisted cheating, proxy candidates, engineer time, or throughput? Lead with that from Batch 4 onward.
3. Did anyone ask **"how much?"** unprompted? That's a buying signal and tells you your price anchor.
4. Every rejection gets a **reason code** logged (`NO_HIRING_NOW`, `TRUST_AI`, `PRICE`…) per `Pilot_Offer_and_Pricing.md` §5.1, with a reopen trigger and a diarized date.

**Decision gate at Fri 4 Sep:**
- **0 replies of 22** → the list is wrong, not the copy. Stop sending; go all-in on the hand-built demand-signified list.
- **Replies but no meetings** → the CTA is too heavy. Switch Segment 1 to the "want a sample report?" ask.
- **Meetings booked** → run them, and hold the line on the honesty guardrails. One demo on a prospect's *real open req* is worth more than the next 200 emails.

---

## PART 7 — Changes to make in the existing files

| File | Change |
|---|---|
| `11_Cold_Email_Sequence.md` | Fix the three unsourced claims (92% / $555K / 10x). Split into Segment 1 and Segment 2 sequences. Add the agentic-coding wedge to Segment 1. Strip links from Email 1. |
| `12_Apollo_Contact_List.md` | Add Tier (A/B/C/D) and Segment columns. Correct Madhive (Pune, not Baramati), Aerial (Seattle, not Denver), Iterative Health (Cambridge MA). Mark Aerial + Canundra as removed with reasons. |
| `04-sales-toolkit/Cold_Outreach_Cadence_and_ICP.md` | Add the IT staffing/services firm as a **second candidate ICP** with its own attribute table — pending what Batch 2/3 teach you. |
| `04-sales-toolkit/Pilot_Offer_and_Pricing.md` | Replace `$[X]` with a real number before the first meeting. You cannot run the §1.6 ask script with a blank in it. |

---

## Appendix — sources for the claims used above

- Iterative Health $77M Series C, Apr 2026 — [FinSMEs](https://www.finsmes.com/2026/04/iterative-health-raises-77m-in-series-c-funding.html), [Tracxn](https://tracxn.com/d/companies/iterative-health/__TZox9l5196B5OMiQBqqqQ5QMGF70C4tu2jD2IyZUfWM)
- SuperCircle $24M Series A, Dec 2025 — [PR Newswire](https://www.prnewswire.com/news-releases/supercircle-raises-24m-series-a-to-scale-retails-waste-management-operating-system-302637202.html)
- Aerial $2M pre-seed, Seattle — [Crunchbase](https://www.crunchbase.com/organization/aerial-58e9), [Founder Lodge](https://founderlodge.com/round/Aerial-raises-2000000-Pre-Seed-2024-05-15-Doug-Logan-MTkwMzU)
- Madhive HQ NYC, 201–500 staff, Pune office — [Built In NYC](https://www.builtinnyc.com/company/madhive), [Madhive about](https://www.madhive.com/about-us)
- Canundra = enterprise transformation consultancy — [canundra.com](https://www.canundra.com/)
- WalkingTree ~336 staff, IT services — [RocketReach](https://rocketreach.co/walkingtree-technologies-profile_b5cc061ef42e0a52)
- 20,000+ applicants deferred over impersonation, June 2026; Hyderabad proxy rings; 79% of IT/ITeS fraud from experienced candidates — [RippleHire](https://www.ripplehire.com/blog/how-interview-fraud-is-disrupting-professional-services-hiring), [Sherlock](https://www.sherlock.sh/blog/rise-of-ai-interview-fraud), [SpringVerify](https://in.springverify.com/blog/proxy-interviews-identity-fraud-remote-hiring/), [SHRM India](https://www.shrm.org/in/topics-tools/news/how-to-navigate-ai-candidate-fraud-race)
