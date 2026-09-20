# 28 — X Profile Fix + Week-1 Content: @roundz_ai

> **Companion to:** `27_X_Engagement_Playbook.md` (reply targets, saved searches, account rules)
> **Goal:** Go from 21 followers / ~25 impressions per post to a compounding daily presence. Followers come from replies (doc 27); this doc covers what people see when they click through.
> **Written:** 2026-09-11

---

## 0. Audit snapshot (2026-09-11)

| Metric | Value |
|---|---|
| Followers / Following | 21 / 6 |
| Posts | 43 since Jan 2025 (~2–3/month) |
| Median post reach | 20–60 impressions, 0–1 likes |
| Best post | Pinned "free DSA round" (Feb 9) — 11K impressions, 3 likes, 1 reply |
| Best reply | Sep 1 reply on a hiring-manager post — 55 impressions (more than most originals) |
| Profile | Avatar ✅ Banner ✅ Professional account ✅ ("Science & Technology") · Not verified |

**Diagnosis:** content register is fine (the Aug 11 "job changed, questions didn't" thread is the right voice). The problems are cadence (twice a month), distribution (no replies, 6 follows), and a split audience (bio → job seekers, recent replies → hiring managers).

### Done 2026-09-11
- Bio rewritten: *"AI voice interviewer that runs real coding, system design & behavioral rounds — with live follow-ups, proctoring and structured feedback. Free DSA round ↓"*
- Website added: roundz.ai
- Location: intentionally blank

### Still open (needs a human)
- [ ] **Premium** — paid; needed for reply ranking + analytics. Do this before starting the reply cadence in doc 27 or the replies get buried.
- [ ] **Follow 200+ accounts** from the target list in doc 27 §1 and §4 saved searches.
- [ ] Record the 30s product clip for the pinned post (below).

---

## 1. Audience decision

**Primary audience for @roundz_ai: engineers preparing for interviews.** Reasons: 100× larger than hiring managers on X, they share content, and the free DSA round is a native CTA for them. The hiring-side pitch (free pilots, staffing partnerships) stays on LinkedIn (docs 23/24) and in cold email (docs 19–22).

Rule: hiring-manager replies on X are still fine (they're the outlier-reach ones), but the *timeline* is written for candidates.

---

## 2. New pinned post

Replace the Feb 9 pin. Same offer, but lead with a hook and a **video**, not a screenshot. Post as a 2-tweet thread so the link sits in the reply (links in the first tweet get down-ranked).

**Tweet 1 (attach 30s screen recording of the voice interviewer pushing back on an answer):**

```
Most mock interviews let you finish your answer.

Real ones don't.

We built an AI interviewer that interrupts, asks "why not a heap?", and grades you on how you recover — not just whether your code passes.

One full DSA round is free. No card, no signup wall.
```

**Tweet 2 (reply):**

```
Try it here → roundz.ai

Post your score below. We'll tell you which follow-up question tripped most people this week.
```

**Video spec:** 25–35s, portrait or 16:9, captions burned in (most watch muted). Show: candidate mid-answer → AI follow-up question → the structured feedback card. No intro slide, no logo animation.

---

## 3. Week-1 daily posts

One original per day, ≥5 replies per day (doc 27 §2 has drafts). Post between 8:30–10:00 IST or 18:30–20:00 IST (catches India evening + US morning). No hashtags.

All numbers marked `[N]` are placeholders — **pull the real figures from the platform before posting.** Real data is the moat; invented data is a credibility bomb.

### Day 1 (Mon) — Opinion

```
LeetCode tests a skill AI already has.

Writing a correct two-sum in 15 minutes told you something in 2019. In 2026 it tells you the candidate has a keyboard.

What it doesn't test: can they explain why they picked that approach when someone pushes back?

That's the round nobody practices.
```

### Day 2 (Tue) — Interview question of the day

```
Question of the day (system design, mid-level):

"Design a rate limiter for a public API. 10K requests/sec, multi-region."

Reply with your first 3 clarifying questions — not the design. Tomorrow I'll post what our interviewer asks when candidates skip that step.
```

### Day 3 (Wed) — Follow-up to Day 2 with real data

```
Yesterday's rate limiter question.

Out of [N] candidates who answered it on Roundz, [N]% jumped straight to "token bucket + Redis" without asking a single clarifying question.

The follow-up that stopped most of them:
"Your Redis node in us-east goes down. What happens to a client in eu-west?"

Asking questions first isn't stalling. It's the interview.
```

### Day 4 (Thu) — Show the product

Attach a 15–20s clip: AI asks a behavioral follow-up, candidate pauses, feedback card appears.

```
Behavioral rounds are where strong engineers lose offers.

Not because they lack stories — because they've never had someone say "and what would you do differently?" and then wait.

This is what that looks like with our interviewer. The silence is the point.
```

### Day 5 (Fri) — Contrarian / hot topic

```
Everyone's worried about candidates using AI to cheat in interviews.

Unpopular take: if your interview can be passed by reading ChatGPT off a second screen, the interview was already broken.

Live follow-ups fix this. Proctoring is a bandage. Depth is the cure.
```

### Day 6 (Sat) — Data post

```
We ran [N] mock interviews last month. The single most common reason a strong coder got a "no hire" from the AI:

They never stated the time complexity until asked.

[N]% of candidates who volunteered it unprompted scored a full band higher on the whole round.

Say the Big-O. Every time.
```

### Day 7 (Sun) — Community / CTA (lightest post of the week)

```
Sunday prep thread.

Reply with the role + level you're interviewing for this week. I'll reply with the one follow-up question you should have an answer ready for.

(Free DSA round is pinned if you want to run it before Monday.)
```

---

## 4. Week 2+ — the repeating cadence

| Day | Slot | Source |
|---|---|---|
| Mon | Opinion on interviewing/hiring in the AI era | Founder's takes; things said in sales calls |
| Tue | Question of the day | Pull from the platform's question bank |
| Wed | Answer + real data from Tue | Platform analytics |
| Thu | Product clip | One 20s recording per week |
| Fri | Contrarian take on a live X discussion | Doc 27 saved searches, "Latest" tab |
| Sat | Data post | Platform analytics |
| Sun | Community reply-thread | — |

Batch-write Mon–Sun in one sitting; schedule via X's native scheduler.

**Founder account:** the Mon/Fri opinion posts should go out from the founder's personal handle first, with @roundz_ai quote-posting. People follow people; the brand account alone will cap out.

---

## 5. What to measure (weekly, Sundays)

| Metric | Week 0 baseline | 60-day target |
|---|---|---|
| Followers | 21 | 300–500 |
| Median impressions / original post | ~25 | 500+ |
| Replies received / week | ~0 | 20+ |
| Profile link clicks (needs Premium analytics) | unknown | track |
| Replies sent / week (doc 27 cadence) | 0 | 35+ |

If replies-sent is on target for 3 weeks and median impressions haven't moved, change the content angle — not the volume.
