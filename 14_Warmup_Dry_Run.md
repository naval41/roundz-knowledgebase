# 14 — Warmup Dry Run (manual, 10 internal mailboxes)

> **Started:** 2026-07-30 (Thu). **Mailbox:** `outreach@mail.roundz.ai` (per explicit direction 2026-07-30 — overrides the `vivek@` recommendation in `13_Cold_Email_Launch_Plan.md` §1.1. Flagging once more: `outreach@` is a role address and reads as bulk harder than a personal-name sender. If this is meant to be permanent, fine — just don't switch senders again later, since that resets reputation to zero.)
> **Purpose:** build sender reputation on a 1-day-old domain, then seed-test real placement before Batch 1 on **Thu 6 Aug** (compressed twice on 2026-07-30: first 18→11 Aug, then 11→6 Aug — see Part 3. Total ramp-to-launch window is now **8 elapsed days**, below the 12-day floor originally recommended. The seed test on 3–4 Aug is now the hard gate: any spam placement there means delaying launch, not proceeding anyway.)

---

## PART 0 — Read this before you send anything

### Opens do almost nothing. Replies do almost everything.

The plan as you described it — "internal people open the email to increase the score" — is the most common warmup misconception, and acting on it would waste the two weeks.

Gmail and Microsoft don't meaningfully weight opens. They can't reliably see them: an open is a tracking pixel load, and Apple Mail Privacy Protection plus Gmail's image proxy fire that pixel whether or not a human looked. It's noise, and the filters treat it as noise.

What actually moves sender reputation, ranked:

| Signal | Weight | Who can do it |
|---|---|---|
| **A real reply** (2+ sentences, from the thread) | Highest | All 10 |
| **"Not spam" / "Not junk"** on a message that landed in spam | Very high | Whoever it happens to |
| **Dragging Gmail Promotions → Primary** ("do this for future messages") | High | Gmail users |
| **Adding you to Contacts / Safe Senders** | High | All 10 |
| **A thread with 2–3 back-and-forth turns** | High | All 10 |
| Star / flag / move to a folder | Moderate | All 10 |
| Opening the email | ~Zero | — |
| Deleting without replying | **Negative** | — |
| Marking as spam | **Severely negative** | — |

So the instruction to your 10 people is **not** "please open this." It's **"please reply properly, and tell me where it landed."**

### Second correction: internal-only may be worth nothing

If any of your 10 addresses are on `roundz.ai`, `mail.roundz.ai`, or the same Google Workspace / Microsoft 365 tenant as your sending mailbox, **that mail never leaves the server.** It's routed internally, never evaluated by Gmail's or Microsoft's inbound filters, and contributes **zero** external reputation.

Every one of the 10 must be an **external** mailbox at a **different** provider from yours. See Part 1.

### Third: keep the automated warmup running underneath

Ten humans generating ~60–80 replies over two weeks is a good *quality* layer, but a warmup tool (Instantly / Smartlead / MailReach / Warmy) puts you in a pool of thousands of real mailboxes across every major provider, at a volume you can't reproduce by hand. Run both. The 10 humans are for the **seed test** and the high-quality reply signal; the tool is for the volume base.

---

## PART 1 — Audit your 10 addresses first

Reputation is provider-specific. Your Batch 1 targets sit mostly on Google Workspace and Microsoft 365, so a warmup that's 10/10 personal Gmail teaches Microsoft nothing about you.

**Target mix:**

| Provider | How many | Why |
|---|---|---|
| **Personal Gmail** (`@gmail.com`) | 3 | Biggest consumer filter; also tells you Primary vs Promotions |
| **Microsoft consumer** (`@outlook.com` / `@hotmail.com` / `@live.com`) | 2 | Microsoft's filter is the harshest and behaves nothing like Gmail's |
| **Corporate Google Workspace** (any real company domain) | 2 | Closest analogue to your actual prospects |
| **Corporate Microsoft 365** (any real company domain) | 2 | Defender/EOP is what a FalconX or Iterative Health inbox looks like |
| **Yahoo / Zoho / Proton / Rediff** | 1 | Cheap extra signal; Rediff/Zoho are useful for the India segment |
| **Anything on `roundz.ai` or your own tenant** | **0** | Contributes nothing |

If your 10 don't cover this, fix the mix before Day 1 — ask people for their personal Gmail or their address at a previous employer. A well-distributed 7 beats a lopsided 10.

Log them in a sheet: `Name | Address | Provider | Where it landed (per send) | Replied? | Actions taken`.

---

## PART 2 — The instruction sheet to send your 10 people

Send this once, from your **existing** mailbox, before Day 1.

> Hi — I'm setting up a new sending domain for Roundz and I need about two weeks of help from you. It's genuinely low effort, maybe 90 seconds a day.
>
> You'll get real emails from **vivek@mail.roundz.ai**. They're real questions about real work, so just answer them normally.
>
> **Every time one arrives:**
>
> 1. **Check where it landed first** — Inbox, Gmail's Promotions/Updates tab, or Spam/Junk. Tell me which, in your reply. This is the part I actually need.
> 2. **If it's in Spam/Junk:** hit "Not spam" / "Not junk," then move it to your inbox.
> 3. **If Gmail put it in Promotions or Updates:** drag it to Primary, and say yes when it asks whether to do that for future messages.
> 4. **Reply properly** — two or three sentences of an actual answer. Not "ok" or "got it." A one-word reply is worth almost nothing to me.
> 5. **Add the address to your contacts** (Gmail: "Add to contacts" from the sender menu. Outlook: right-click the sender → Add to Safe Senders).
> 6. If I reply again in the same thread, reply again. Threads are worth more than single messages.
>
> **Please don't:** delete without replying, archive it immediately, or mark it as spam. Any of those actively set me back.
>
> One more thing: **reply whenever you naturally would** — an hour later, that afternoon, next morning. Don't all reply within the same five minutes. Natural timing spread matters.
>
> Thanks. I'll tell you when we're done.

---

## PART 3 — The schedule

> **Compressed twice on 2026-07-30.** First pass: launch 18→11 Aug (more recipients + cut buffer days, ramp shape held). Second pass, at the user's request to finish by 2 Aug: ramp end pulled in to **Sun 2 Aug**, launch now **Thu 6 Aug**. Total elapsed ramp-to-launch window is now **8 days**, below the 12-day floor originally recommended — domain/mailbox age is weighted by providers independent of volume and this is the thinnest margin advisable. **The seed test on 3–4 Aug is the hard gate**: any spam/junk placement there means delaying launch, not proceeding on schedule anyway.
>
> Sat 1 Aug / Sun 2 Aug carry real sends. This is workable *because* the framing is personal correspondence, not bulk B2B — friends emailing on a weekend is normal; a cold-outreach spike on a weekend is not. Keep weekend content casual; don't introduce links before Sunday.

| Phase | Dates | Sends/day | What |
|---|---|---|---|
| **Ramp** | Thu 30 – Fri 31 Jul (done) | 2, 4 | Short, plain text, **zero links, zero attachments**. Every one asks a question. |
| **Ramp (weekend)** | Sat 1 – Sun 2 Aug | 5, 8 | Casual/personal tone continues; links can start Sun 2 Aug at the earliest. |
| **Seed test** | Mon 3 – Tue 4 Aug | 10 + 10 | The **real** cold emails to all active recipients. See Part 5. |
| **Final checks** | Wed 5 Aug | 3 | mail-tester 10/10, remediate anything from the seed test |
| **Launch** | **Thu 6 Aug, 10:00** | 7 | Batch 1 — Tier A+B. Thursday is independently the best-performing send day in cold-email benchmark data (6.87% reply rate), so this isn't purely a compromise pick. |

Sends can repeat to the same person. Seven recipients over 8 days at this ramp is roughly 40–50 messages, most of which should generate a reply.

**Still needed to hold this schedule safely:** 2–3 more external addresses, ideally at least one Microsoft/Outlook or corporate domain — see Part 1's provider gap. Compressing the calendar without widening the provider mix just moves the same risk earlier, and matters more now that there's less time to absorb a bad Microsoft signal before launch.

---

## PART 3A — Audit of the 14 supplied addresses

```
nrabadiya@gmail.com            navneet.rabadiya@gmail.com     navneetrabadiya@gmail.com
nraddy1990@gmail.com           info.codemate@gmail.com        vivekvara222@gmail.com
Try.vivekv@gmail.com           Try.vivekv2@gmail.com          Viveck.vara@gmail.com
zarnavaghela554@gmail.com      zarnavaghela@yahoo.in          bharadiya.sagar.dev@gmail.com
bharadiya.99@gmail.com         heenabharadiya1102@gmail.com
```

### Finding 1 — two of these are literally the same mailbox

**Gmail ignores dots in the local part.** `navneet.rabadiya@gmail.com` and `navneetrabadiya@gmail.com` deliver to **one identical inbox**. Gmail also ignores case, so `Try.vivekv@` = `tryvivekv@`. You have 13 distinct mailboxes, not 14 — and sending the same person two copies of one email is a bulk pattern, not a warmup signal.

### Finding 2 — 14 addresses, roughly 5 humans

| Human | Addresses | Distinct inboxes |
|---|---|---|
| Navneet Rabadiya | `nrabadiya@`, `navneet.rabadiya@`, `navneetrabadiya@`, `nraddy1990@` | 3 |
| Vivek Vara | `vivekvara222@`, `Try.vivekv@`, `Try.vivekv2@`, `Viveck.vara@` | 4 |
| Zarna Vaghela | `zarnavaghela554@gmail`, `zarnavaghela@yahoo.in` | 2 |
| Bharadiya (Sagar / +1?) | `bharadiya.sagar.dev@`, `bharadiya.99@` | 2 |
| Heena Bharadiya | `heenabharadiya1102@` | 1 |
| — (role address) | `info.codemate@` | 1 |

**Extra Gmail aliases of the same person do not multiply the signal.** Google links them by recovery phone, device, IP and session. Four inboxes one person checks from one browser on one connection are worth roughly one — and if they all reply within the same few minutes from the same IP, Google reads that as coordinated warmup and discounts it. `Try.vivekv@` and `Try.vivekv2@` look like dormant throwaway accounts; mail to low-engagement Gmail accounts is near-worthless and mildly negative.

### Finding 3 — the real gap: no Microsoft, no corporate domains

13 of 14 are consumer Gmail. One Yahoo. **Zero Microsoft. Zero Google Workspace or M365 corporate domains.**

That's the lopsided mix flagged in Part 1, and it matters concretely: FalconX, Iterative Health, Detroit Labs, Intersection and Mphasis Silverline are the kind of companies that run **Microsoft 365**. Microsoft's filter (Defender/EOP) behaves nothing like consumer Gmail's and is far slower to trust a new domain. After two weeks of this warmup you will have **no idea** how you land there — and Microsoft is where Batch 1 is most likely to fail.

**The cheap fix, this week:** ask each of your 5 people for **one work address** — their employer's, a client's, a previous employer's, anything on a real company domain. Five corporate mailboxes are worth more than the nine surplus Gmail aliases combined. Prioritise anyone on Outlook/M365.

### The roster to actually use

**Active (7) — one per human, plus the Yahoo:**

| # | Address | Person | Provider | Notes |
|---|---|---|---|---|
| R1 | `nrabadiya@gmail.com` | Navneet | Gmail | Primary only — retire the other three |
| R2 | `vivekvara222@gmail.com` | Vivek V | Gmail | Primary only — skip the `Try.*` accounts |
| R3 | `zarnavaghela554@gmail.com` | Zarna | Gmail | |
| R4 | `zarnavaghela@yahoo.in` | Zarna | **Yahoo** | Same human, different filter — keep it, it's your only non-Gmail |
| R5 | `bharadiya.sagar.dev@gmail.com` | Sagar | Gmail | Technical — give him the technical topics |
| R6 | `bharadiya.99@gmail.com` | ? | Gmail | **Confirm this is a different person from R5.** If it's Sagar's alias, drop it. |
| R7 | `heenabharadiya1102@gmail.com` | Heena | Gmail | Non-technical topics |
| R8 | `info.codemate@gmail.com` | role | Gmail | Optional. Only use if a human genuinely reads and replies from it. |

**Bench — do not send to these:** `navneet.rabadiya@`, `navneetrabadiya@`, `nraddy1990@`, `Try.vivekv@`, `Try.vivekv2@`, `Viveck.vara@`

One instruction specific to Zarna: she's on both R3 and R4, so tell her they're deliberately separate threads, and ask her to **reply from each account independently, hours apart** — not both in one sitting.

---

## PART 4 — Ramp send plan (Thu 30 Jul – Wed 5 Aug)

**Compressed from 7 days to 6.** Same 21 opener/topic/reply sends, same "new topic → second topic → thread reply" shape per recipient — just tightened onto fewer calendar days by using the day-3 and day-4 slots more fully. Day 1–2 already sent (see below); nothing about those two changes.

No email body goes to more than two people, and nobody sees the same body twice.

| Day | Date | Sends | Schedule | Status |
|---|---|---|---|---|
| 1 | Thu 30 Jul | 2 | `OPEN-A`→R5 · `OPEN-B`→R1 | **Sent** |
| 2 | Fri 31 Jul | 7 | `OPEN-B`→R3 · `OPEN-C`→R2 · `OPEN-A`→R6 · `T1`→R5 · `T2`→R1 · `OPEN-A`→R4 · `OPEN-C`→R7 | **Sent** — last 2 (R4, R7) pulled forward from the weekend slot: first touch for both, no 5-hour-gap conflict, keeps roster coverage complete |
| 3 | Sat 1 Aug | 5 | `T3`→R3 · `T4`→R2 · `T7`→R4 · `T5`→R6 · `T6`→R7 | **Sent** — all 5. (Stray scheduled test email to R7 was cancelled by user before it fired.) |
| 4 | Sun 2 Aug / next send | — | `T6`→R7 (once clear) · `C1`→R5 *(reply in T1 thread)* | R1 and R5 already have 2 touches (Thu+Fri); next for them is a thread reply, not a new topic |
| 5 | Wed 5 Aug | 4 | `T6`→R7 · `C2`→R1 · `T7`→R4 · `C3`→R3 | |
| 6 | (folded into Tue 4/Wed 5) | — | `C4`→R2 · `C5`→R6 · `C6`→R7 · `C7`→R4 spread across 4–5 Aug | |

Send between 10:00–17:00 IST, spread across the day — never several in the same minute.

**Hard rule: minimum 5-hour gap between any two sends to the same address**, even across different templates/threads. Within a 10:00–17:00 IST window that caps any one recipient at 2 touches/day, sent well apart (e.g. ~10:30 and ~15:30+). If a recipient is due a second touch and there isn't a 5-hour gap left in the day, push it to the next day rather than compress the gap. Tue 4 – Wed 5 Aug is now a slightly heavier day (5, 4) rather than a separate week; that's the compression — still under the "never jump" rule since it's one step up from 3–4, not a leap to 10.

### The openers

**`OPEN-A` — subject: `sending from this one now`** → R5, R6, R4

```
Hey {First},

Moving my outbound off the main domain, so this is the new mailbox.

Two things when you get a sec:

1. Did this land in your inbox, or Promotions/Spam?
2. Are you reading it on the Gmail app or on web?

Want a read on how it's showing up across setups before I start using
it for real.

RoundzAI
```

**`OPEN-B` — subject: `new address, ignore the old one`** → R1, R3

```
{First},

Quick heads up — I'm sending from mail.roundz.ai now instead of the
main domain. Same me.

Can you tell me where this one landed for you? Inbox or Promotions? And
if it went to Spam, pull it out and let me know, that's genuinely
useful data right now.

RoundzAI
```

**`OPEN-C` — subject: `does this reach you`** → R2, R7

```
Hi {First},

Testing a new sending setup before I start using it properly next
month.

Would you mind replying with just two things — which folder this landed
in, and whether the sender name showed up as "Vivek P" or as the raw
email address? Different clients render it differently and I can't see
it from my end.

Thanks,
RoundzAI
```

### The topic emails

Matched to the person — technical topics to the technical contacts, opinion topics to everyone else. An email asking Heena about MID-level backend rubrics would read as obviously fake; the whole point is that these are real questions someone might genuinely ask *that person*.

**`T1` — subject: `rubric report — which order`** → R5 *(technical)*

```
Sagar,

Building out the sample interview report we hand to prospects — the
level-aware one with the hire verdict on it.

Before I finish: for a MID-level backend candidate, should it lead with
the per-criterion scores, or with the written summary? I keep
flip-flopping. My gut says summary on top and scores underneath, but
you've read more of these than I have.

Which way would you go?

RoundzAI
```

**`T2` — subject: `pricing sanity check`** → R1 *(anyone)*

```
Navneet,

Want your gut on something.

The first paid pilot is one open role, 20-30 candidate interviews, two
to four weeks, paid up front. I need to put a real number on it instead
of leaving it blank in the deck.

If you were buying: what price makes you say "that's obviously worth
trying," and what makes you say "let me think about it"? Ballpark is
fine, I just need a reality check from outside my own head.

RoundzAI
```

**`T3` — subject: `two subject lines, pick one`** → R3 *(anyone)*

```
Zarna,

Testing subject lines for the first outbound batch. Which of these
would you open if it landed cold from someone you didn't know?

A: "your screen vs. candidates who use AI"
B: "the proxy-candidate problem"

More useful — which one would make you delete it without opening? That's
the one I actually need to know about.

RoundzAI
```

**`T4` — subject: `careers page wording`** → R2 *(anyone)*

```
Vivek,

We're updating the careers page and I want the interview description
right, since candidates read it before they ever speak to us.

Does "you'll do one live technical round with our AI interviewer, then
meet the team" sound reassuring, or slightly alarming? I genuinely
can't tell from the inside anymore.

Say it how you'd react if you were applying.

RoundzAI
```

**`T5` — subject: `proctoring — where's the line`** → R6 *(semi-technical)*

```
{First},

Been chewing on this one.

Our reports surface gaze, tab-switching and clipboard activity during
the interview. Useful signal, clearly. But how much should a hiring
manager actually see, versus just a summary flag?

Where's the line for you between "helpful" and "creepy"? Curious where
you land, because I keep landing in a different place each day.

RoundzAI
```

**`T6` — subject: `how would you explain this`** → R7 *(anyone)*

```
Heena,

Trying to explain one part of the product in two sentences and failing
badly.

What it does: during the interview we hand the candidate an AI
assistant on purpose, then score how well they use it — how they break
the problem down, what they accept, what they throw away.

Every version I write sounds either too clever or too obvious. If I
explained it to you that way, what would you say back?

RoundzAI
```

**`T7` — subject: `which phrasing`** → R4 *(anyone)*

```
Zarna,

Two ways of saying the same thing on the homepage. Which reads better
to you?

1. "Your team meets only the top 20%."
2. "We filter the funnel. You still make every call."

I lean towards the second because the first sounds like we're deciding
who gets hired, which isn't what happens. But I've read both so many
times they've stopped meaning anything.

RoundzAI
```

### The thread replies (Day 5–7)

Short by design. Send as a **reply inside the existing thread**, never as a new email — a 2–3 turn thread is worth considerably more than two unrelated messages.

**`C1` → R5** *(in the T1 thread)*
```
That's useful, thanks — summary first it is.

One follow-on: the verdict scale runs STRONG_HIRE down to
STRONG_NO_HIRE. Should that sit at the top of page one, or at the end
after the reasoning? Putting it first is honest but then nobody reads
the rest.
```

**`C2` → R1** *(in the T2 thread)*
```
Helpful, thank you.

Follow-up: would you rather pay that as one flat pilot fee, or per
candidate interviewed? Same total either way — I'm curious which one
feels less risky when you've never used the thing before.
```

**`C3` → R3** *(in the T3 thread)*
```
Interesting, you picked the opposite of what I expected.

What made B worse for you — the word "proxy," or just that it sounds
like a problem you don't have? Trying to work out if it's the wording
or the premise.
```

**`C4` → R2** *(in the T4 thread)*
```
Fair. "Alarming" is what I was afraid of.

Would it change if the line said your interview is reviewed by a human
before any decision? Or does mentioning AI at all put people off
regardless?
```

**`C5` → R6** *(in the T5 thread)*
```
Agreed, summary flag only by default.

Last thing on this: if a candidate got flagged and asked why, how much
should we be able to show them? Feels like they should be able to see
whatever the employer sees, but I'd like a second opinion.
```

**`C6` → R7** *(in the T6 thread)*
```
That's much better than what I had, thank you — stealing it.

One more: does "AI interviewer" make you think of a robot voice, or of
a normal conversation? Trying to work out how much expectation-setting
we need to do up front.
```

**`C7` → R4** *(in the T7 thread)*
```
Good, that settles it.

While I've got you — does "technical screening" mean anything to you as
a phrase, or is it jargon? Half our audience is technical and half
isn't and I keep writing for the wrong one.
```

---

## PART 4B — Generic bodies (Week 2 and reuse)

These are deliberately **real work**, not filler. That's the whole trick: don't fabricate warmup traffic, move genuine correspondence onto the new mailbox. Real questions get real replies, and real replies are the signal you're buying.

Vary who gets which. **Never send the same text to more than two people** — identical bodies fanned across 10 recipients is exactly the pattern filters are built to catch.

### Ramp days (30 Jul – 3 Aug) — plain text, no links, no attachments

**W1-01 — subject: `sending from this one now`**

```
Hey {Name},

Moving my outbound off the main domain, so this is the new mailbox.

Can you reply and tell me two things:

1. Did this land in your inbox, or Promotions/Junk?
2. Are you on Gmail web, the app, or Outlook?

Trying to get a read on how it shows up across different setups before
I start using it for real.

RoundzAI
```

**W1-02 — subject: `rubric report — which order`**

```
{Name},

Building out the sample interview report we hand to prospects — the
level-aware one with the hire verdict on it.

Before I finish it: for a MID-level backend candidate, should the report
lead with the per-criterion scores, or with the written summary? I keep
flip-flopping. My gut says summary on top, scores underneath, but you've
read more of these than I have.

Which way would you go?

RoundzAI
```

**W1-03 — subject: `pricing sanity check`**

```
Hi {Name},

Want your gut on something.

The first paid pilot is one open role, 20-30 candidate interviews, two
to four weeks, paid up front. I need to put an actual number on it
instead of leaving it blank in the deck.

If you were buying: what price makes you say "that's obviously worth
trying," and what price makes you say "let me think about it"? Ballpark
is completely fine, I just need a reality check.

RoundzAI
```

**W1-04 — subject: `how would you explain the AI copilot round`**

```
{Name},

Trying to explain our agentic-coding round in two sentences and failing.

The thing itself: we hand the candidate an AI copilot during the
interview on purpose, and score how well they direct it — how they break
the problem down, what they accept, what they throw away.

Every version I write sounds either too clever or too obvious. How would
you say it to someone who's never heard of us?

RoundzAI
```

**W1-05 — subject: `careers page copy`**

```
Hi {Name},

We're about to update the careers page and I want to get the interview
description right, since candidates read it before they ever talk to us.

Does "you'll do one live technical round with our AI interviewer, then
meet the team" sound reassuring to you, or slightly alarming? Genuinely
can't tell from the inside.

RoundzAI
```

**W1-06 — subject: `proctoring — what's fair to show`**

```
{Name},

Question I've been chewing on.

Our reports surface gaze, tab-switching and clipboard activity. Useful
signal, obviously. But how much of that should a hiring manager actually
see versus just a summary flag?

Where's the line for you between "helpful" and "creepy"? Curious where
you land.

RoundzAI
```

**W1-07 — subject: `re: rubric report — which order`** *(thread continuation, Day 4+)*

```
That's useful, thanks. Summary-first it is.

One follow-on: the verdict scale runs STRONG_HIRE down to
STRONG_NO_HIRE. Should that sit at the very top of page one, or at the
end after the reasoning?

Putting it first is honest but I worry nobody reads past it.

RoundzAI
```

### Links/attachments phase (4–5 Aug) — longer, links allowed, threads

**W2-08 — subject: `2 min loom`** *(first link — one only)*

```
{Name},

Recorded a rough walkthrough of the agentic round, about two minutes:
{loom_link}

It's unlisted and genuinely unpolished — I'm not fussing over production
value yet.

Two things I want to know: does it make sense if you don't already know
the product, and does it drag anywhere? Timestamp it if so.

RoundzAI
```

**W2-09 — subject: `does this link work for you`**

```
Hi {Name},

Setting up the booking link before outreach starts. Can you open this
and tell me if the times look sane in your timezone: {cal_link}

Don't actually book anything. I just want to know it isn't offering
people 3am slots.

RoundzAI
```

**W2-10 — subject: `two subject lines, pick one`**

```
{Name},

Testing two subject lines for the first outbound batch. Which one would
you open if it landed cold?

A: "{Company}'s screen vs. candidates who use AI"
B: "the proxy-candidate problem at {Company}"

And more useful — which one would make you *delete* it? That's the one
I need to know about.

RoundzAI
```

**W2-11 — subject: `sample report attached`** *(first attachment — PDF, not zip, not docx)*

```
{Name},

Attached is the sample rubric report, first real version.

Read it as if you were the hiring manager receiving it: would you trust
the verdict, and is there anything on there you'd need explained before
you acted on it?

Also — did this land in your inbox with the attachment, or did it get
filtered? Worth knowing.

RoundzAI
```

**W2-12 — subject: `the fraud numbers`**

```
Hi {Name},

Fact-checking myself before I put these in front of anyone.

A major Indian IT services firm deferred assessments for 20,000+
applicants in June after finding widespread impersonation. And in
IT/ITeS, 79% of employment-fraud cases involve previously employed
candidates, not freshers.

Both are third-party research, not our data, and I'm going to source
them inline every time. Does citing them that way read as credible to
you, or as hedging?

RoundzAI
```

**W2-13 — subject: `re: pricing sanity check`** *(thread continuation)*

```
Circling back on this one — you said {their number} felt about right.

Follow-up: would you rather pay that as a flat pilot fee, or per
candidate interviewed? Same total either way. I'm curious which one
feels less risky to a first-time buyer.

RoundzAI
```

**W2-14 — subject: `quick favour — forwarding test`**

```
{Name},

Last one of these, I promise.

Can you forward this email to your own personal address (or any other
inbox you have) and tell me whether it lands in the inbox there?

Forwarding behaves differently from direct sending and I want to know
if anything breaks on the way through.

RoundzAI
```

---

## PART 5 — The seed test (Thu 6 – Fri 7 Aug)

This is the highest-value thing your mailboxes give you, and it only works if you run it correctly.

**Thu 6 Aug** — send the real **Segment 1** email (`13_Cold_Email_Launch_Plan.md` §3.3) to all active recipients, personalized as though each were a genuine prospect. **Fri 7 Aug** — same with the real **Segment 2** email (§3.4).

**The one rule that makes or breaks it:**

> For these two sends only, everyone must **report where it landed BEFORE touching anything.** No "not spam," no dragging to Primary, no replying, until they've told you the placement.

During warmup, remediating is the point. During the seed test, remediating first destroys the measurement — you'd be marking your own homework. Send that instruction separately so it doesn't get lost.

**Record per recipient:** `Provider | Inbox / Promotions / Updates / Spam | Any warning banner ("Be careful with this message", "This sender is new to you")`.

**How to read the result:**

| Result | Meaning | Action |
|---|---|---|
| All in inbox, no banners | Warmup worked | Launch Tue 11 Aug as planned |
| Gmail inbox, but Microsoft spam/junk | Very common; Microsoft is slower to trust new domains | Push Batch 1 by one week and weight warmup toward the Microsoft addresses |
| Landing in **Promotions** | Something reads as bulk | Strip remaining links, remove the signature block image if any, shorten |
| **Any** spam placement after 2 weeks | Something is broken, not just cold | Re-check SPF/DKIM/DMARC alignment, re-run mail-tester, delay launch |
| "This sender is new to you" banner | Normal and expected on a 3-week domain | Not a blocker; fades with volume |

Then remediate: everyone marks not-spam, drags to Primary, adds to contacts. Those actions are worth a lot right before launch.

---

## PART 6 — What this does and doesn't buy you

Be clear-eyed. ~9 days of manual warmup across 7 active mailboxes gets `mail.roundz.ai` to the point where **a low-volume, plain-text, hand-personalized send to 7 people on Tue 11 Aug will reach the inbox.** That's exactly what Batch 1 is, so it's sufficient — but it's a thinner margin than the original 14-day plan, precisely because it's a week shorter. If the seed test on 6–7 Aug shows anything landing in spam or Promotions, don't launch on schedule — push Batch 1 back rather than eat the risk. Compression bought back time only if the seed test actually passes clean.

It does **not** buy you the reputation to send 200/day in September. That comes from sustained real sending with real reply rates over 6–8 weeks. Ramp accordingly: 10–15/day through late August, 25–30/day by mid-September, and never past 30/day on one mailbox. If you need more than that later, buy more mailboxes and warm each one separately — don't push a single box harder.

One number worth holding in mind while you set expectations for Batch 2 and 3: cold email into **IT services runs ~3.5% reply rate**, the lowest of any industry tracked, alongside SaaS and financial services. Your Tier C staffing segment sits squarely in that bucket. If 15 contacts produce zero replies, that's within normal variance and is **not** evidence the staffing narrative is wrong — you'd need 150 to know. Don't kill the segment on Batch 3's numbers; kill it or keep it on what the replies actually *say*.
