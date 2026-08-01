# 11 — Cold Email Sequence (Recruiter / TA Outreach)

> Cold outreach drip for Talent Acquisition / Recruiting contacts at IT & software companies (the Apollo list built 2026-07-25: 12 US + 12 India, small companies <500 employees, verified emails).
>
> Angle: written to the **Talent/Recruiting persona**, not the CTO. Per the Founding Sales Playbook, this audience responds to "10x screening throughput, no scheduling hell" — not the CTO-focused "less of your time" framing.
>
> Rules followed (from 10_Founding_Sales_Playbook.md): text-only, short, single-thought per email, one thread, breakup email at the end. 5-min personalized first email + drip ≈ 15x reply rate vs one-and-done.

---

## Before sending — checklist

- [ ] Fill `{Calendar_Link}` and `{Rep_Name}` before sending. If no booking link yet (Calendly/Cal.com), get one first — every email points there.
- [ ] CAN-SPAM: physical mailing address + working unsubscribe in the footer. Apollo adds unsubscribe automatically; confirm sending profile has a real address set.
- [ ] Sending domain: `mail.roundz.ai` (dedicated subdomain, protects roundz.ai reputation). Mailbox provider still TBD — DMARC record already in Route 53; MX/SPF/DKIM pending provider signup.
- [ ] Warm up the mailbox 2-4 weeks before launching this sequence at volume.
- [ ] Optional but high-leverage: enrich each contact with their company's actual open engineering roles (careers page / LinkedIn Jobs) so Email 1 can reference real roles instead of staying generic. Biggest single lever on reply rate.

---

## Email 1 (Day 0) — the hook

**Subject:** `{First_Name}, technical screening eating your team's week?`

```
Hi {First_Name},

Quick question: how much of your week goes into coordinating technical
screens for engineering roles at {Company}?

Most TA teams we talk to are stuck in the same loop: schedule the eng
interviewer, reschedule when they're pulled onto something urgent, then
do it all again for the next candidate. Meanwhile good candidates go
cold waiting.

Roundz AI runs the first-round technical interview with an AI voice
agent instead of your engineers, DSA, system design, behavioral, live
proctored, available 24/7. No calendar tetris. Your engineers only
show up for the candidates who already cleared a real technical bar.

Worth 15 minutes to see it run on one of your open roles?

Reply here, or grab a slot: {Calendar_Link}

{Rep_Name}
```

---

## Email 2 (Day 3) — throughput angle

**Subject:** `re: {First_Name}, technical screening eating your team's week?`

```
Hi {First_Name},

Following up in case this got buried.

The teams using Roundz AI screen about 10x more candidates in the same
window, since the AI agent runs interviews around the clock instead of
waiting on an engineer's open calendar slot. That means less time
between "candidate applies" and "candidate gets a real answer," which
usually means fewer good candidates ghosting mid-process.

Happy to walk you through it on one of your current reqs if that's
useful. {Calendar_Link}

{Rep_Name}
```

---

## Email 3 (Day 7) — the fraud / trust angle

**Subject:** `catching fake technical interviews`

```
Hi {First_Name},

Different angle this time: are you seeing candidates lean on ChatGPT or
a second screen during technical interviews? It's become common enough
that a lot of TA teams have stopped fully trusting a clean screen.

Roundz AI proctors every session live and catches AI-assisted answers,
tab-switching, and proxy interviewers, with about 92% detection accuracy.
So when a candidate passes, it means something.

If that's a live problem for {Company}, I can show you what a flagged
session actually looks like. {Calendar_Link}

{Rep_Name}
```

---

## Email 4 (Day 12) — the ROI number, framed for a recruiter to hand upward

**Subject:** `the $555K number for your next 1:1`

```
Hi {First_Name},

One more, then I'll leave it alone.

Across bad hires, unfilled-seat cost, and engineering time lost to
screening, broken technical hiring runs the average Series A-C company
about $555K a year. That's usually a useful number to bring into a
budget conversation, even outside of us.

Roundz AI is built to take a big chunk of that off the table: faster
screening, fewer bad hires, engineering time back. If it's relevant, I'd
still like to show you. {Calendar_Link}

{Rep_Name}
```

---

## Email 5 (Day 18) — breakup

**Subject:** `closing the loop`

```
Hi {First_Name},

I'll stop emailing after this one so I'm not cluttering your inbox.

If technical screening at {Company} is running smoothly, ignore all of
this. If it's not, and a 15-minute look at Roundz AI would help, I'm
around: {Calendar_Link}

Either way, good luck with the hiring push.

{Rep_Name}
```

---

## Merge fields used

| Field | Source |
|-------|--------|
| `{First_Name}` | Apollo contact first name |
| `{Company}` | Apollo contact company name |
| `{Calendar_Link}` | Your booking link (Calendly/Cal.com) — set before sending |
| `{Rep_Name}` | Sender name (should be the person actually replying to responses) |
