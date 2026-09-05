# Recruiter & Founder Subreddit Map — Trial Recruitment

**Date:** 2026-08-14
**Goal:** Find recruiters (potential trial users) and founders (potential distribution partners) on Reddit for Roundz trials.
**Method:** Subscriber counts and rule text fetched live from `about.json` / `about/rules.json` on 2026-08-14.
**Companion docs:** `08_Reddit_Engagement_Playbook.md` (Parts 1, 2, 4), `16_Seed_User_Sourcing_Model.md`

---

## 0. Headline finding — read before doing anything

**Every recruiter/HR subreddit on Reddit bans exactly the thing you want to do.** This is not a
"be careful" caveat; the rules were fetched and checked one by one. There is no recruiter sub
where "we built an AI interview tool, who wants to trial it" is permitted as a post, a comment,
or a DM solicitation.

Compounding it: **our account already has a mod warning on record in r/recruiting** (see
Playbook Part 2, legacy table). That sub is the single largest recruiter community and it is the
one place we are already flagged.

So the recruiter side is a **listen-and-learn channel, not an acquisition channel.** The founder
side is where trial recruitment can legitimately happen — and one of those subs
(r/alphaandbetausers) exists precisely for this.

---

## 1. Recruiter / HR / TA subs — verified

| Subreddit | Size | Type | Promo verdict | Rule evidence |
|---|---|---|---|---|
| **r/recruiting** | 212k | public | **DO NOT ENTER** | Mod warning already on our account. Largest sub, highest cost if we burn it. |
| **r/AskHR** | 1.85M | public | Comments only, zero promo | "AI Posts will result in an instant Ban." Also: no surveys/research, no asking for DMs. Our comments must not read as AI-written. |
| **r/humanresources** | 236k | public | Comments only, zero promo | "No advertising" + "No straight AI copy/paste posts or comments" + "No surveys or research" + **"No Requests or Offers to Communicate via DM."** That last rule kills the DM-to-trial play outright. |
| **r/askrecruiters** | 18k | public | Comments only, zero promo | Two separate rules: "No product promotion" and "Moderator discretion: no politics or promotions." Small, but the cleanest recruiter audience we can reach. |
| **r/recruitinghell** | 1.45M | public | **Listener only, forever** | An AI interview tool is the villain of this community. Confirmed unchanged. |
| **r/TalentAcquisition** | 771 | **restricted** | Can't post without approval | Tiny and gated. Not worth the approval request. |
| **r/recruiters** | 1.1k | **restricted** | Can't post without approval | Same. |
| r/HRTech, r/sourcing, r/staffing, r/recruitingtech | — | **do not exist** | n/a | Checked; no such subs. Don't chase them. |

### What the recruiter subs are actually good for

1. **Pain-language mining.** Read r/recruiting and r/askrecruiters weekly and lift the exact
   phrasing recruiters use about screening load. That language belongs in the cold email
   sequence (`11_Cold_Email_Sequence.md`) and landing copy, where there are no promo rules.
2. **Named-lead sourcing.** People who post detailed screening-volume complaints in
   r/askrecruiters are qualified leads. Do **not** DM them from Reddit — r/humanresources
   explicitly bans DM offers, and cold DMs are the fastest route to a sitewide spam report.
   Instead, treat the post as a signal and reach the person through the normal channel
   (LinkedIn / email, per the seed-sourcing model).
3. **Nothing else.** No posts, no mentions, no "would anyone be interested in" feelers.

---

## 2. Founder / builder subs — verified

These are where trial recruitment is actually allowed. Audience is founders and indie builders,
not our core ICP, but many of them **are hiring** and several will have a recruiter or HR contact
they can hand us. Treat it as distribution + warm referral, not direct ICP.

| Subreddit | Size | Promo verdict | Rule evidence / play |
|---|---|---|---|
| **r/alphaandbetausers** | 42k | ✅ **Free — purpose-built for this** | No custom rules at all. Explicitly exists for beta recruiting. **Start here.** Zero risk, low traffic. |
| **r/SideProject** | 793k | ✅ Disclosed "I built X" is the norm | Already our primary owned-post home. Established in the playbook. |
| **r/betatests** | 16k | ✅ Allowed, with a posting checklist | Rules are just: content policy, be respectful, no low-effort, "Requirements to Post." Read the requirements sticky before posting. |
| **r/indiehackers** | 187k | ✅ **One post, Self Promotion flair** | Explicit: self-promo permitted once, with the flair, and framed as **feedback/critique, not advertisement.** We get one shot — spend it on a real writeup, not a launch blurb. |
| **r/B2BSaaS** | 27k | ⚠️ "Limit Self-Promotion" + "Provide Value" | Small but exactly the right frame. Value post with the ask at the end. |
| **r/EntrepreneurRideAlong** | 720k | ⚠️ Journey posts with real numbers | Build-in-public framing works; a bare trial ask does not. |
| **r/StartUpIndia** | 440k | ⚠️ **Saturdays only** | Hard rule: startup promotion and surveys/market research are allowed **only on Saturdays**; Sun–Fri they go in the Weekly Pinned Megathread. Good India-audience fit — just calendar it. |
| **r/microsaas** | 207k | ⚠️ Real writeup required | "No Low-Effort Self-Promotion." Already in the playbook. |
| **r/Entrepreneur** | 5.3M | ⚠️ Heavily moderated, low signal | Huge but noisy; promo gets removed fast. Low priority. |
| **r/SaaS** | 780k | ⚠️ Verify sticky before posting | Big, promo-saturated. Medium priority. |
| **r/ycombinator** | 200k | ❌ **No** | "No self promotion" + "No solicitation of surveys, DMs, external groups" + feedback confined to megathreads. Megathread only. |
| **r/growmybusiness** | 145k | ❌ **No** | "No Selling or Upselling" + **"No External Surveys/Feedback Requests."** Both of our asks are named. |
| **r/startups** | 2.1M | ❌ Monthly sticky for promo; ✅ **discussion posts allowed** | Promo only in the "Share Your Startup" sticky. But Rule 3 explicitly permits discussing strategies and experiences "WITHOUT tying them directly to your own project using its name or URL", which is what makes the §5 discussion post legitimate. **Two hard posting gates, see §2b.** |
| r/Startup_Ideas | 327k | ⚠️ No rules defined | Zero custom rules, but ideas-stage audience, weak fit. |

---

## 2b. Posting gates that remove a post before anyone reads it

These are not content rules. They are automated gates that delete a compliant post on submission,
and they are invisible until they fire. Check for them in any new sub before spending a draft.

### r/startups — two gates, both learned the hard way

**Gate 1: the Read The Rules acknowledgement (one time, per account).**
Confirmed 2026-08-14. Our first discussion post
([1vo6229](https://www.reddit.com/r/startups/comments/1vo6229/)) was removed within moments by the
automated `read-the-rules` app, not by a moderator and not for its content:

> "Your post on r/startups was removed by the Read The Rules app because you need to submit an
> acknowledgement that you have read the rules."

To clear it: open the three-dot menu on the subreddit, or on any post or comment in it, choose
**"Read The Rules"**, and submit the acknowledgement. Then repost. It is a Devvit app, so the menu
item **only appears on new Reddit web or the mobile app** — it is invisible on old.reddit.com.
No penalty attaches to this kind of removal; repost rather than appeal.

**Gate 2: the "I will not promote" title suffix (every post, forever).**
Every r/startups submission must carry the phrase **"I will not promote"**. Convention is to append
it to the title: `<your title> - I will not promote`. Vivek got this right unprompted on the first
attempt; it was missing from the original draft and would have caused a second removal.

### Generalise this

Before the first post in **any** new sub, check for: a rules-acknowledgement app, a required title
phrase or flair, and account age or karma minimums (r/betatests, for instance, needs a 24-hour-old
account and 2 combined karma). A removal costs a day and, in some subs, a strike.

---

## 3. Recommended sequence

**Week 1 — free wins, no risk**
1. r/alphaandbetausers — disclosed beta-recruiting post. Nothing to lose.
2. r/betatests — read the posting-requirements sticky, then post.

**Week 2 — the one-shot posts**
3. r/indiehackers — the single Self-Promotion-flair post. Frame it as "here's what we built and
   what we got wrong, tear it apart," with the trial offer as the last line.
4. r/SideProject — already-established home, standard disclosed post.

**Week 3 — India + B2B**
5. r/StartUpIndia — **Saturday only.**
6. r/B2BSaaS — value-first post.

**Ongoing, in parallel, no posting**
7. Weekly read of r/askrecruiters + r/recruiting for pain language and named leads. Extract to
   the cold-email swipe file. Never post, never DM.

---

## 4. Things that will get the account banned

- Any promo, mention, or "anyone interested?" comment in a recruiter/HR sub.
- Reddit DMs offering a trial to r/humanresources members — explicitly rule-banned.
- Posting the same writeup across founder subs in one session (crosspost spam detection).
- AI-sounding prose in r/AskHR, r/humanresources, or r/csMajors — all three have explicit
  anti-AI-content rules with instant-ban language.
- A second self-promo post in r/indiehackers. One is the limit.

---

## 4b. Evaluated and rejected: the unnamed "volunteers wanted, DM me" post

**Proposed 2026-08-14 by Vivek:** post in founder / business / recruiter subs asking for volunteers
to validate and try the product, **without naming the product**, with interested people replying
**by DM**. Verdict after fetching the rule text of all 20 candidate subs: **do not run this.** It is
riskier than the named version while producing fewer and worse respondents.

### The format is banned by name in almost every sub on the target list

Not "probably counts as promo." Named, in the rule text, fetched 2026-08-14:

| Sub | Size | Rule text |
|---|---|---|
| **r/Entrepreneur** | 5.3M | "Do not use this community to sell, promote, **recruit**, hire, job-seek, solicit investment, or drive traffic to your profile... No dropping URLs, **asking users to DM you**, telling people to check your..." — three separate parts of the plan named in one rule |
| **r/startups** | 2.1M | Rule titled **"Do Not Solicit PM Requests / Post DM Notices."** "The purpose of making a submission or comment is to engage in a public discussion... It is not to request a PM/DM from someone." |
| **r/microsaas** | 207k | Rule titled **"No DM ME."** "Any post or comment requesting private messaging will be removed." |
| **r/humanresources** | 236k | "No Requests or Offers to Communicate via DM" **and** "No surveys or research: this subreddit is not a place for... conducting market research for your product." |
| **r/AskHR** | 1.85M | "Do not ask for PM's in comments and do not PM contributors of the subreddit directly." |
| **r/ycombinator** | 200k | "No solicitation of surveys, **DMs**, external groups, etc." |
| **r/smallbusiness** | 2.5M | "No market research posts — not for developing apps, **not for AI**, not for business offerings." |
| **r/StartUpIndia** | 440k | Promotion and surveys: Saturdays only, regardless of format |

That is the entire founder-and-business list except r/alphaandbetausers and r/betatests, and the
entire recruiter list without exception.

### Omitting the product name does not avoid the promo rules

**r/LeetcodeDesi** states the general principle explicitly: "Self promotion of any kind is not
allowed. **Even if it's surrogate or if no link is provided.**" Mods classify by intent, not by
whether a URL appears. An unnamed post that routes to a DM where the pitch happens is the textbook
surrogate case, and it is the pattern mod tooling is tuned for. So the format pays the full cost of
promoting while giving up the only defence a promo post has, which is being openly disclosed.

### It also inverts the trust equation

"I have a product, I won't say what it is, DM me" is the shape of lead-gen spam and of scams. The
proposed audience, founders, is the single most pattern-matched group on Reddit for exactly this.
The named drafts in `18_Reddit_Trial_Recruitment_Drafts.md` work *because* they open with the
unflattering parts; anonymity removes every credibility signal they rely on.

### The DM channel is the account-risk one

A subreddit rule break costs a post removal. An unsolicited DM pitch gets marked "report spam,"
which is a **sitewide** Reddit action, not a subreddit one. Given this account's history (mod
warning on record at r/recruiting, thin karma, no owned posts yet) that is the wrong risk to take
first. Note the asymmetry: inbound DMs from someone who read a disclosed post are fine and carry
none of this risk. It is the solicitation that is the problem.

### It selects for the wrong respondents

Vagueness filters *for* people who reply to anything and *against* people with a real reason to
care. Per `16_Seed_User_Sourcing_Model.md`, the binding constraint is share propensity, and the
respondents we want are those who see "AI-assisted coding round" and self-select in. They cannot
self-select into a post that withholds the subject.

### And the supposed benefit does not exist

The only reason to drop the name is to slip past self-promotion rules. But the two subs where a
disclosed beta-recruitment post is **already fully permitted** (r/alphaandbetausers, no custom
rules; r/betatests, requirements are only a 24-hour-old account and 2 karma) allow the named
version outright. There is nothing to route around.

### What to do instead

The instinct behind the idea, ask for help rather than attention, is right. Keep it, change the mechanism:

1. **Beta subs, named and disclosed.** r/alphaandbetausers then r/betatests. Drafts are written.
2. **Let DMs come inbound.** Never request them in a post. Add one line inviting comments, and
   answer DMs that arrive on their own.
3. **Founder subs: earn it, once.** r/indiehackers permits exactly one self-promo post framed as
   critique. That draft exists. It is worth more than ten anonymous asks.
4. **Recruiters: not through Reddit.** Every recruiter sub bans both promo and DM solicitation.
   Mine them for pain language and named leads, then reach those people by email or LinkedIn.

---

## 5. Open items

- r/betatests posting requirements sticky — not yet read.
- r/SaaS and r/Entrepreneur stickies — not yet read; verify before spending a post there.
- r/StartUpIndia Saturday megathread mechanics — confirm the exact flair/thread on a Saturday.
