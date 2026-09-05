# Seed User Sourcing Model — Share-Propensity Cohort

**Date:** 2026-08-08
**Goal:** Recruit ~20 trial users who will publicly share their Roundz results.
**Derived from:** `ecc:lead-intelligence`, reweighted for share-propensity seeding (not B2B decision-maker outreach).

---

## 0. Why the default model doesn't apply

The stock lead-intelligence pipeline weights role/title (30%) and industry (25%) highest, and
routes through mutual connections for warm intros. Both are wrong for this job:

- **Title is nearly irrelevant.** A junior dev who posts weekly is worth more than a silent Staff engineer.
- **Warm paths are unnecessary.** You're offering something the target already wants, for free.
  Cold DM is the expected channel. Mutual-mapping adds latency with no lift.

The binding constraint is **share propensity**, which is a behavioral trait, not a firmographic one.
Baseline: ~1-2% of users ever post about a product unprompted. Among people who *already*
post publicly about their job hunt, it is 10-20x that — because you are supplying content for an
existing habit rather than asking for a new behavior.

---

## 1. Signal scoring (reweighted)

| Signal | Weight | Where to observe it |
|---|---|---|
| **Public posting recency** — posted about interviews/job hunt in last 90 days | 35% | LinkedIn posts, Reddit self-posts, YouTube uploads |
| **Posting frequency** — habit, not a one-off | 20% | Profile activity tab / post history |
| **Current interview activity** — actively interviewing or teaching interviews | 20% | Post content, #OpenToWork, channel topic |
| **Audience size** — 500-50k. Big enough to matter, small enough to reply | 15% | Follower/subscriber count |
| **Platform fit** — audience overlaps candidate or eng-leader pools | 10% | Platform + content topic |

**Qualification bar:** posted publicly in the last 90 days AND 500+ followers AND currently
interviewing or producing interview content.

**Disqualifiers:**
- Runs a competing interview-prep product (see §4)
- No original posts, only comments/reshares
- Audience >100k — will not answer a cold DM from a pre-launch product

---

## 2. Tiering

| Tier | Profile | Expected share rate | Ask |
|---|---|---|---|
| **T1** | Micro-creators, <50k subs, publish interview content | High — your product is a free episode | Free unlimited access, no conditions |
| **T2** | Candidates who write public interview writeups | Medium-high — proven public narrators | Founding-cohort access + feedback call |
| **T3** | Active job seekers, 500+ followers, occasional posters | Medium | Cohort access |

Target mix: ~5 T1, ~10 T2, ~5 T3. Build a list of **50 names to land 20 participants**
(expect 30-40% response on a personalized DM).

---

## 3. Search queries

### LinkedIn — Posts filter, Past month, sort by Recent
- `"interview experience"` + `software engineer`
- `"finally cracked"` OR `"got the offer"` + `SDE`
- `"system design interview"` — the people *posting*, not commenting
- `#OpenToWork` + `backend engineer` — filter to those with post history

### Reddit — sort by New
Subreddits: `r/leetcode`, `r/cscareerquestions`, `r/developersIndia`, `r/ExperiencedDevs`
Look for self-post writeups: "interview experience", "my journey", "rejected after final round".
Qualify: author has comment karma and a posting habit.

### YouTube
Search `mock interview system design`, filter **This month** + **4-20 minutes**, sort by upload date.
This deliberately skips the incumbents and surfaces small active creators.

---

## 4. Competitive exclusions

The top of this niche is competitors, not partners. Do **not** pitch:

| Channel/Platform | Size | Why excluded |
|---|---|---|
| Hello Interview | — | Sells mock interviews + AI prep tools. Direct competitor. |
| Exponent (TryExponent) | ~380k subs | Sells mock interview practice. Direct competitor. |
| ByteByteGo | ~1.37M | Course/book business; too large for cold outreach |
| Gaurav Sen | ~718k | Course business; too large for cold outreach |

Implication: partnership with established interview-prep creators is largely a dead end.
Target individual candidates and sub-50k creators who have not yet built a competing product.

---

## 5. Outreach drafts

**Channel priority:** LinkedIn DM > Reddit DM > YouTube channel email > X DM.
(Email is deprioritized — you have no address for these people and no warm path.)

### T2/T3 — candidate who posted a writeup

> Hey [name] — read your writeup on the [company] loop. The bit about [specific detail]
> matched my experience exactly.
>
> I'm building an AI interviewer that runs an actual conversational round — it interrupts,
> pushes back, asks the follow-up you were hoping it wouldn't. Picking 20 people to run it
> before we open up.
>
> You'd get the full evaluation breakdown. All I want back is 15 minutes of honest feedback —
> including if you think it's bad. Interested?

### T1 — small creator

> Hey [name] — been watching your mock interview breakdowns.
>
> I've built an AI that conducts the interview live: voice, interruptions, follow-ups, then a
> scored evaluation. Nobody's put it on camera yet and I think it'd make a genuinely good
> video — either way it goes.
>
> Free unlimited access, no conditions, no approval over what you say. Want to try it?

### Design rules
- **The ask is feedback, not a share.** Sharing must stay voluntary or testimonials read as bought.
- **"Including if you think it's bad"** materially raises reply rate — signals you want truth, not a favor.
- **Never script the caption.** Suggested captions read as suggested captions.
- One ask per message. No feature dumps. No merge-field slop.

---

## 6. Prerequisites before the cohort runs

1. **Free-tier cap set** (2-3 interviews/month). Creates the currency referral loops need,
   and bounds voice-AI marginal cost.
2. **End-of-session share moment shipped** — scorecard asset + in-product ask at the moment
   of reaction. 20 impressed users with no share mechanism produce zero posts.
3. **Both outcomes shareable.** A humbling result ("the AI destroyed me on system design")
   often outperforms a flattering one in dev culture. Do not tune to flatter everyone.

---

## 7. Expected yield

50 approached -> ~20 join -> ~12-15 complete a session -> **~5-8 post publicly.**

Judge this by usable public artifacts, not user count. Those 5-8 posts are what make the
next 50 easier, because they are third-party proof instead of self-description.

---

## 8. Compliance

If participants receive anything of material value in exchange for posting, they must disclose it.
Keeping the ask genuinely optional and unpaid avoids the issue entirely — and produces better content.

---

## 9. Execution status

- [x] Scoring model + tiering defined
- [x] Search queries specified
- [x] Outreach drafts written
- [ ] **Named list of 50 prospects** — BLOCKED. Requires LinkedIn/Reddit access;
      Exa + X API credentials are not configured, and Reddit blocks direct fetching.
      Unblock via browser control against a logged-in session.
- [ ] Free-tier cap decided
- [ ] Share moment shipped
