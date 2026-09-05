# Reddit Trial-Recruitment Post Drafts

**Date:** 2026-08-14
**For:** Manual posting by Vivek.
**Sub selection and rules:** `17_Recruiter_And_Founder_Sub_Map.md`
**Writing rules applied:** `08_Reddit_Engagement_Playbook.md` Part 5 (no em dashes, no marketing words, soft framing, vary structure between posts).
**Claim accuracy:** every capability below is checked against `01-base-knowledge/Product_Ground_Truth.md`. No code-execution claims, no invented metrics, correct framing of the AI-assisted coding round.

---

## ASSUMPTION TO CONFIRM BEFORE POSTING

The drafts say **"free during the beta, no card."** That is my read of the T1 offer in
`16_Seed_User_Sourcing_Model.md` ("Free unlimited access, no conditions"). If the real offer is
capped (N interviews, time-limited, credits), tell me and I will correct all three, since an
overstated free offer is the one thing here that would damage trust rather than just underperform.

---

## 1. r/alphaandbetausers — post first, zero risk

**Title:**
> [Beta] Voice AI interviewer that scores how you use an AI copilot, not how fast you type

**Body:**

We built Roundz and we are looking for people to run a session and tell us where it falls apart.

What it is: a live voice interview, not a chatbot with a record button. The AI interviewer talks
with you in real time and you can interrupt it. It also watches your code editor and your
whiteboard while you work, so it can ask about the approach you are actually taking rather than
waiting for a finished answer. Rounds cover behavioral, coding, system design and a Q&A.

The part we most want broken is the AI-assisted coding round. You get an AI copilot inside the
interview and the task is to solve the problem with it. We score prompt quality, how you break the
problem down, and whether you catch a bad suggestion instead of accepting it. It is the newest
thing we do and therefore the most likely to be wrong.

Two honest limits: there is no code execution sandbox, so correctness is judged by a model reading
your code and it can misread an unusual solution. And voice latency suffers on a weak connection.

Free during the beta, no card. Useful whichever side you are on: if you are interviewing you get
written feedback, and if you are hiring you can run it as a first screen.

roundz.ai. Criticism in the comments is welcome, that is what I am here for.

---

## 2. r/betatests — post second

Read the "Requirements to Post" sticky first and match its required format. Deliberately shorter
and structured differently from the r/alphaandbetausers draft so the two do not read as one
template.

**Title:**
> Looking for testers: AI voice interviewer with an agentic-coding round

**Body:**

**What it is:** a live voice AI technical interview. Real-time turn-taking, you can interrupt it,
and it reads your editor and whiteboard as you work so it can follow your reasoning mid-problem.

**What I need tested:** the AI-assisted coding round. You are given an AI copilot during the
interview and scored on how well you direct it, not on how fast you type. Nobody has stress-tested
it outside our own team yet.

**Who it suits:** anyone interviewing for engineering roles, or anyone who screens candidates.

**Time:** roughly 30 to 45 minutes for a full session.

**Cost:** free during the beta, no card.

**Known gaps:** no code sandbox, so correctness is model-judged from your written code. Latency
degrades on poor connections.

**Feedback I want:** did the interviewer ever talk over you or lose the thread, and did the written
evaluation match how the session actually felt.

roundz.ai

---

## 3. r/indiehackers — the one-shot post, spend it carefully

Sub rule: self-promotion is allowed **once**, with the Self Promotion flair, and framed as feedback
and critique rather than advertisement. Do not post a second one later. Separate rule: any MRR
claim needs proof, so this draft makes no revenue claim at all.

**Flair:** Self Promotion

**Title:**
> Built an AI interviewer that grades how candidates use AI. Three things we got wrong first.

**Body:**

Roundz is a live voice AI interviewer. Candidates practise on it, employers run it as a first
screen. Posting for critique rather than signups, so here is the unflattering half first.

**We built the wrong differentiator for about a year.** The pitch was faster screening, which is
what every tool in this category says, and it earns no attention. The thing that actually makes
people lean in is a round where the candidate is handed an AI copilot and the task is to solve the
problem with it. We log the prompts, the decomposition, and whether they accept or reject each
suggestion, then score judgment rather than typing speed. That was a side feature. It should have
been the product.

**We assumed people wanted a code sandbox.** We do not have one, and correctness is judged by a
model reading the submitted code. I expected that to be the first objection in every demo. It has
not come up once, because the buyers we talk to already stopped believing that passing test cases
predicts anything.

**We underestimated how much the voice layer decides everything.** If the interviewer talks over
someone or goes silent while they are thinking, nothing downstream matters. More engineering has
gone into turn-taking and into not abandoning a candidate who has gone quiet mid-problem than into
the evaluation logic.

What I would like torn apart: is "we score how you use AI" a real wedge, or is it a feature that
HackerRank ships in a quarter and erases us.

Free during the beta if you want to run a session yourself, roundz.ai. Founder, so treat the above
accordingly.

---

## 4. Posting notes

- **One post per session, and leave at least a full day between subs.** Three near-identical
  writeups going out in one evening is the pattern spam detection is built to catch.
- **Reply to every comment within a few hours, short.** Per Part 5, a thread with no founder
  replies reads worse than no thread.
- **Do not crosspost.** Each of these is written separately on purpose.
- **Log each one in `09_Reddit_Activity_Log.md`** with the same DRAFT-nnn convention, since these
  are the account's first owned posts and the outcome data matters more than for a comment.
- **Recruiter subs stay off limits.** None of this copy goes anywhere near r/recruiting,
  r/humanresources, r/AskHR or r/askrecruiters, in any form.
- **r/StartUpIndia and r/B2BSaaS drafts** are not written yet. StartUpIndia needs a Saturday and a
  different, India-market framing; B2BSaaS needs a value-first post with the ask at the end.

---

## 5. Discussion post: "we cannot get first users" (approved format)

**Proposed 2026-08-14 by Vivek:** forget the product for now, post a genuine question about the
distribution problem itself and collect views. **Verdict: yes, run this.** It is the only format
proposed so far that is *explicitly permitted* rather than merely tolerated.

### Why it clears the rules

**r/startups** Rule 3, fetched 2026-08-14, reads: "Submissions are for discussing methodologies,
experiences, strategies, techniques, markets, and other such things **WITHOUT tying them directly to
your own project using its name or URL**." That is a description of this exact post. Same logic
holds in r/EntrepreneurRideAlong, r/indiehackers and r/SaaS. It also **does not consume the single
r/indiehackers self-promo slot**, because it is not self-promotion.

Note the contrast with the rejected §4b format: what made that one fail was the *DM solicitation
and hidden pitch*, not the absence of a product name. Remove the ask and it becomes legitimate.

### The real risk is not rules, it is being ignored

"How do I get my first users" is close to the most-posted question in every one of these subs.
r/SaaS has a rule for it ("No Low-Effort / Low-Quality Content") and r/microsaas has another
("avoid vague motivational posts"). A generic version gets removed or gets generic answers: post on
Product Hunt, do cold outreach, talk to users.

**Specificity is the entire difference.** The post must carry what we built (category only), what we
have already tried, real numbers, and one sharp question. That is also what makes it honest.

### What we actually get out of it

Be clear-eyed: most replies will be mediocre. The value is in the second-order effects, and both are
already documented in the playbook.

1. **Profile views.** Playbook Part 4 identifies the profile funnel as this account's conversion
   mechanism. A question post that lands drives far more profile clicks than a comment does.
2. **Self-identified ICP in the comments.** People who reply with "I had this exact problem selling
   to recruiters" are leads. Reply publicly, and continue privately only if they open that door.
3. **Someone will ask what the product is.** That is the good outcome, not a problem. Answering a
   direct question with a disclosed founder note is clean under every rule here. Have the reply
   ready before posting.

### Draft — r/startups (best fit, post here first)

Rules to respect: no name, no URL, 250+ character minimum, clear descriptive title.

**Title:**
> We solved the technical problem and completely underestimated distribution. What actually got you your first 20 users?

**Body:**

We spent about a year building an AI voice interviewing tool. The engineering was hard and we got
it working. Then we discovered we had optimised for the wrong difficulty, because getting twenty
people to simply try the thing has been harder than everything that came before it.

Whenever you go looking for advice on this, more or less the same list comes back:

- Go where your users already are and be genuinely useful for a few months before you mention
  anything you have built.
- Do one-to-one outreach by hand, unscalably, until something works.
- Launch somewhere with a built-in audience and hope for a spike.
- Publish content and wait for search to compound.
- Give it away free and trust that usage produces word of mouth.
- Find one person who already has the audience you want and get them to vouch for you.

Every item on that list is reasonable, and the list is useless, because it does not tell you which
one to bet the next three months on. They also have wildly different payback periods, and at this
stage you only get to be wrong once or twice.

So the two things I would genuinely like to hear:

1. **Did your first twenty users come from one channel, or from twenty separate conversations?**
   Most advice describes a channel. Almost every founder I have actually asked describes the
   conversations. I would like to know which is more common.
2. **If you sell into a category people are sceptical of, what earned you the first yes?** A free
   trial does not solve scepticism, because trying something still costs someone half an hour and a
   bit of professional risk if they recommend it internally and it disappoints.

Not linking anything, this is not a plug. I would rather hear how you did it.

### Before you post to r/startups (both confirmed 2026-08-14)

1. **Clear the Read The Rules gate first.** Attempt 1 ([1vo6229](https://www.reddit.com/r/startups/comments/1vo6229/))
   was auto-removed by the `read-the-rules` app before any human saw it, purely because the account
   had not submitted a rules acknowledgement. Three-dot menu on the subreddit or on any post there
   → **"Read The Rules"** → submit. New Reddit web or mobile app only; the item does not render on
   old.reddit.com. Nothing was wrong with the post itself, so repost it unchanged.
2. **Append ` - I will not promote` to the title.** Required on every r/startups submission. Full
   title as it should go out:
   > We solved the technical problem and completely underestimated distribution. What actually got you your first 20 users? - I will not promote

### Notes on running it

- **No numbers in this draft, on purpose.** Checked 2026-08-14: cold email Batch 1 is scheduled for
  Tue 18 Aug (`13_Cold_Email_Launch_Plan.md`) and the send-tracking table is still empty, so there
  are no send or reply figures in existence. Every claim above is one we can stand behind. Once
  Batch 1 has run, adding one real line ("n sent, n replies") would strengthen the post materially,
  so this is worth reposting elsewhere later rather than padding now.
- **r/startups first.** Wait for the result before adapting it for r/EntrepreneurRideAlong or
  r/indiehackers, and rewrite rather than crosspost.
- **Skip r/Entrepreneur for now.** Its "Posting requirements and contribution standards" rule
  requires participating in other posts' comments first, and this account has no history there.
- **Answer every reply.** A question post whose author does not respond reads as karma farming and
  gives up the entire profile-funnel benefit.
- **Prepare the "what is it?" reply** in advance: one paragraph, disclosed as founder, describes the
  product without a link unless someone asks for one.

---

## 6. Co-founder search post — r/Entrepreneurship (ready to post manually)

**Different objective from everything above.** Sections 1 to 5 recruit trial users. This one recruits
a **GTM co-founder from recruitment, talent acquisition or staffing** who would own the customer
side. Vivek's brief, 2026-08-14.

### Where this can and cannot go (all rule text fetched live 2026-08-14)

| Sub | Size | Verdict |
|---|---|---|
| **r/Entrepreneurship** | 140k | ✅ **Chosen.** No rule against co-founder posts, no flair required, no submit-text gate. The two rules that govern it are "No Self Promotion" and "Low Effort Post" (which names "an attempt to sell a product, push a service"). Hence: no product name, no link, and the post must give the community something before it asks. |
| **r/cofounder** | 61k | ✅ Purpose-built. DMs are the expected channel (rule 9). Title may name **one** primary skill only; rule 4 requires a real business plan, so vagueness reads as a scam signal; rule 2 favours older, higher-karma accounts. |
| **r/cofounderhunt** | 56k | ✅ Purpose-built. Requires a **"Looking for Cofounder"** flair and an explicit compensation tag (Sweat Equity Only / Equity Available / paid). |
| r/indianstartups | 125k | ⚠️ "No direct sales, advertisements, or promotion." A partner search is not sales, but it is grey. Good if an India-based partner is wanted. |
| r/StartUpIndia | 440k | ⚠️ Has a Hiring rule, so permitted in principle, but hiring posts "need to include monetary details (in numbers)" and commission-based solicitation is banned. "Open on structure" fails this as written; needs a real number. |
| **r/sales** | 597k | ❌ Rule **"No Recruiting Users."** Also 10 community karma to post. This was the most promising audience and it is a hard no. |
| **r/advancedentrepreneur** | 79k | ❌ Three separate rules: "No requesting DMs", "This is not a place for asking for investors or partners", "No AI or crypto businesses". |
| r/startup (315k), r/techsales (62k), r/SaaSSales (34k) | | ❌ "No Solicitations" / "No Self Promotion". |
| r/ycombinator, r/Entrepreneur, r/startups | | ❌ Already documented in `17_Recruiter_And_Founder_Sub_Map.md`. |

### The draft

**Title:**
> Technical founder with a live product and no route to the buyer. Looking for a co-founder from recruitment or staffing.

**Body:**

I am a technical founder. Over the past year I built an AI voice interviewing platform end to end,
the real-time voice pipeline, the evaluation system and the product around them. It works and it is
live.

I cannot sell it. The reason is more specific than "I am bad at sales", so I will put it plainly in
case it is useful to anyone else here.

The buyers are recruiters and hiring teams. I do not know how they buy. I do not know what their
year looks like, when budget gets decided, who else has to be convinced besides the person who likes
the demo, or what makes a hiring lead willing to put their name on a new tool internally. Those are
not things you learn from research. They are things you know because you have sat in that chair.

Three things I have worked out the slow way:

- Building it was the part I could brute force alone. Distribution needs relationships I do not have,
  and no amount of engineering substitutes for them.
- Every week I spend becoming a mediocre salesperson is a week I am not doing the thing I am
  actually good at.
- A first sales hire does not fix this yet, because there is nothing to hand them. The motion itself
  still has to be invented, and that is founder work.

So I am looking for a co-founder who comes from recruitment, talent acquisition or staffing. Someone
who understands how hiring teams buy, has relationships in the space, and wants to own the
go-to-market and customer side as a genuine partner rather than as a first hire. I keep product and
engineering. You own the customer.

The honest state of things: the product works, there are no paying customers yet, and that is
exactly the problem I want a partner for. I would rather say it now than have us discover we
disagree about it in month three.

Structure is open. Equity, paid, or a mix, whatever suits the right person. I would happily start
with something small and defined so we both find out whether it works before either of us commits to
anything.

If that sounds like you, or someone you know, send me a DM.

And if you have been through this from either side, a technical founder who found a commercial
partner or a commercial person who joined one, I would genuinely like to hear how you structured it
and what you would do differently.

### Why it is built this way

- **No product name, no link.** "No Self Promotion" is the rule most likely to catch this post.
- **The closing question is load-bearing.** It converts a classified ad into a discussion post, which
  is what earns a pass under the "Low Effort Post" rule and also draws replies from people who are
  not themselves candidates.
- **"No paying customers yet" stays in.** Anyone worth partnering with asks in the first message.
  Volunteering it is the difference between this and the many vague co-founder posts these subs see.
- **No credential claim.** An earlier version said "senior engineer at a FAANG company". Removed:
  nothing in the knowledge base supports it, and it is not a claim to publish unverified when someone
  may weigh a career decision on it. What replaced it (built the voice pipeline and evaluation system
  end to end) is fully backed by `01-base-knowledge/Product_Ground_Truth.md` and lands harder with a
  technical reader anyway.

### Before posting

- **Not on 2026-08-14.** The account took a sitewide Reddit spam-filter removal that day. A
  DM-soliciting post is the worst possible follow-up to a filter hit. Wait 24 to 48 hours.
- Reply to every comment, quickly and briefly.
- If it works, adapt separately for r/cofounder (one skill in the title) and r/cofounderhunt
  ("Looking for Cofounder" flair). Rewrite each; do not crosspost, and leave days between them.

---

## 7. Still open

- Confirm the free-trial terms (see the assumption block at the top).
- Confirm which account these post from. The existing account has comment history but no owned
  posts, and low karma may trip AutoModerator minimums in the larger subs.
