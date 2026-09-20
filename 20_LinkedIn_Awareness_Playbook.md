# LinkedIn Awareness Playbook — Zero-Budget

**Date:** 2026-08-16
**Goal:** Build public awareness for roundz.ai and source trial users on LinkedIn, at zero spend.
**Companion docs:** `16_Seed_User_Sourcing_Model.md` (who to target), `08_Reddit_Engagement_Playbook.md` (parallel channel).

---

## 0. Why LinkedIn, and why now

Reddit sourcing was attempted first and **failed structurally**: r/leetcode and r/cscareerquestions
writeups come from auto-generated throwaway accounts with hidden post history. You cannot assess
posting habit — the #1 weighted signal in the sourcing model — on an anonymous account.

LinkedIn inverts every one of those problems:

| Requirement | Reddit | LinkedIn |
|---|---|---|
| Real identity | Rare (throwaways) | Default |
| Visible post history | Often hidden | Always, on the Activity tab |
| Follower count visible | No | Yes |
| Sharing is normal behavior | Sometimes | It is the entire point of the platform |

Reddit stays useful for **listening and engagement**. LinkedIn is the **sourcing** channel.

---

## 1. The core mechanic: comment before you post

At zero followers your own posts reach almost nobody. Posting daily into the void is the default
founder failure mode.

**What actually works from cold:** a substantive comment on someone else's post that already has
500 engaged readers puts your name in front of those 500 people *today*, free. Your profile then
does the converting.

**Correct order: Profile → Comments → DMs → Your own posts.**

Do not invert this. Content-first with no audience is 6 weeks of wasted effort.

---

## 2. Free-tier constraints (plan around these)

- **DMs to non-connections require InMail (paid).** The free path is a connection request with a
  300-character note, or getting them to engage with you first.
- **~100-200 connection requests/week** before throttling. Acceptance *rate* matters more than volume;
  a low acceptance rate gets the account restricted.
- **Free search has a monthly commercial-use limit.** Heavy prospect searching soft-blocks you until
  the 1st of the month. Search deliberately, not exploratorily.
- **Company pages get near-zero organic reach.** Post from the personal founder profile. Always.
- **Outbound links suppress reach.** Put the link in the first comment, not the post body.

Net: LinkedIn is a **precision channel** here, not a volume one. ~15 well-chosen people/week.

---

## 3. Step 1 — Profile as landing page (do this before anything else)

Every comment you leave drives traffic to your profile. If the profile is a résumé, that traffic dies.

| Field | Change to |
|---|---|
| **Headline** | State the wedge, not the title. e.g. *"Building the interview for engineers who work with AI \| roundz.ai"* |
| **Banner** | One sentence of positioning + the URL. Free to make. |
| **About** | Lead with the problem (interviews still test hand-written code while engineers direct agents). Then what you built. Then the invite to try it. |
| **Featured** | One item: a short recording of the agentic-coding round. This is the single strongest asset in the product. |
| **Creator mode / Follow** | Enable, so people can follow without connecting. |

---

## 4. Step 2 — The comment engine (highest-ROI free activity)

**Build a target list of ~20 accounts** whose audience is your audience:
- Engineering leaders posting about hiring and interviewing
- Technical recruiters and talent leads
- Dev creators posting about AI changing how engineering works

**Daily routine — 30 minutes:**
- 5-8 comments, prioritizing posts published in the **last hour** (early comments accumulate the most views)
- 2-3 sentences of genuine substance: a counter-example, a specific experience, a sharper question
- **Never** "Great post!" Never drop a link. Never pitch.

Your differentiated take — that interviews should measure how well someone *drives* an AI, not whether
they can hand-write a binary search — is a real opinion. Use it. Opinions get replies; agreement gets ignored.

Expect: 2 weeks of this before your own posts have a meaningful audience.

---

## 5. Step 3 — Trial-user sourcing (the warm sequence)

Use the search queries in `16_Seed_User_Sourcing_Model.md` §3.
**Critical: search the Posts tab, not People.** You are hunting for the act of posting, not for job titles.

Filters: **Past month**, sort by **Recent**.

### The 4-step warm sequence (do not skip to step 4)

1. **Day 0** — Find their post. Leave a real comment on it.
2. **Day 1-2** — React to one more of their posts. Check their Activity tab: do they post regularly,
   or was this a one-off? Score against the §1 model.
3. **Day 3** — Connection request **with a note** referencing the specific post:
   > *"Read your writeup on the [company] loop — the part about [detail] matched my experience exactly.
   > Building something in this space, would be good to connect."*

   No pitch in the note. The note exists only to earn the accept.
4. **After they accept** — Send the T2/T3 DM from `16_Seed_User_Sourcing_Model.md` §5.

**Why this beats a cold DM:** ~40-50% acceptance on a referenced note vs ~10% cold, and it costs nothing.
Cost is time, not money — which is the constraint you actually have.

**Throughput:** 15 prospects/week → the 50-name list in ~3-4 weeks, without tripping any limit.

---

## 6. Step 4 — Your own content (only after week 2)

Post 3x/week. The agentic-coding round is your entire content strategy — it is the one thing
competitors do not have (see `01-base-knowledge/Product_Ground_Truth.md` §4).

**Post types that work, in order:**

1. **The contrarian take.** "We give candidates an AI copilot during the interview — on purpose."
   Eng leaders will argue in the comments. Arguments are reach.
2. **The teardown.** Anonymized: what the AI-usage telemetry actually shows about how engineers
   prompt, accept, and reject suggestions. Nobody else has this data. It is genuinely new information.
3. **Build-in-public.** What broke, what you learned, real numbers. Cheap to write, high trust.
4. **The clip.** 30-60s of the AI interrupting a candidate mid-answer. Native video, captions burned in.

**Rules:**
- Hook in the first 2 lines — everything after is behind "…see more"
- Link in the first comment, never the body
- Reply to every comment within the first hour; it compounds distribution
- Never claim code execution or test-case pass rates (see Ground Truth §3 guardrails)

---

## 7. Weekly time budget

| Activity | Time | Output |
|---|---|---|
| Comment engine | 30 min/day | Awareness, profile traffic |
| Prospect sourcing + warm sequence | 2 hrs/week | 15 prospects |
| Content (write + reply) | 3 hrs/week | 3 posts |
| **Total** | **~8 hrs/week** | |

---

## 8. What to measure (weekly)

- **Profile views** — the real awareness metric. Comments should move this within days.
- **Connection acceptance rate** — below 30% means the note or the targeting is wrong.
- **DM reply rate** — target 30-40%. Below that, the message is too long or too pitchy.
- **Trial signups attributed to LinkedIn** — tag the URL, it is the only number that finally matters.

Do **not** optimize for post likes. Likes from the wrong audience are worse than nothing.

---

## 9. Prerequisites (unchanged from the sourcing model)

These gate the cohort, not the outreach — start §3 and §4 now, but these must land before trial users arrive:

1. **Free-tier cap decided** (2-3 interviews/month recommended) — still open
2. **End-of-session share moment shipped** — scorecard asset + in-product ask. Without it,
   20 impressed users produce zero public posts.
3. **Both flattering and humbling results shareable.** "The AI destroyed me on system design"
   outperforms a flattering score in dev culture.

---

## 10. Execution status

- [x] Playbook defined
- [ ] Profile rewritten (headline, banner, About, Featured clip)
- [ ] 20-account comment target list built
- [ ] Comment engine running daily
- [ ] 50-prospect sourcing list (via Posts search + warm sequence)
- [ ] First 3 posts published
