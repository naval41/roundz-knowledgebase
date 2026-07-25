# Roundz Market Research Deep Dive

**Prepared for:** Founder / GTM / Investor use
**Perspective:** Growth Head and market analyst, Roundz (roundz.ai)
**Status:** Pre-traction, epoch 1 (founder selling first deals)
**Date:** 2026-07-24

> **Read this first.** This is an analytical memo, not a set of audited facts. Every market-size figure, adoption statistic, and cost number in this document is either (a) a labeled third-party research anchor or (b) a bottom-up estimate built from stated assumptions. Estimates are marked as such and show their arithmetic so any reader can challenge the inputs. Nothing here should be presented externally as Roundz proprietary data. See the closing "Sources and Assumptions" note.

---

## 1. Executive Summary

Technical hiring is built on a signal that AI has quietly broken. For fifteen years the industry standard for screening engineers was the auto-graded coding test: give a candidate an algorithm problem, run their code against hidden test cases, and rank by pass rate. That signal worked because solving the problem correctly, alone, under time pressure, was hard and correlated (imperfectly) with engineering ability. Widely available AI coding assistants have collapsed that correlation. A mid-level candidate with a copilot can pass most take-home and auto-graded screens, so a "pass" no longer separates strong engineers from weak ones. The screens still run, but they measure less and less.

At the same time, the job itself has changed. Increasingly, professional software engineering is not typing every line by hand; it is directing AI tools well: decomposing a problem, prompting precisely, reviewing and correcting generated code, knowing when to trust the model and when to override it, and doing so efficiently. That skill, "how well do you direct AI to build correct software," is now a core competency and is almost entirely unmeasured by incumbent assessment tools. The market is testing the wrong thing at exactly the moment the right thing became measurable.

Roundz is built for this break. It runs a company's real technical interview loop with a live voice AI interviewer that watches the candidate's live code (Monaco editor) and system-design whiteboard (Excalidraw) as they work, and it produces explainable, level-aware (ENTRY / MID / SENIOR) rubric-scored reports ending in a hire verdict (STRONG_HIRE through STRONG_NO_HIRE). Its differentiated wedge is a unique agentic-coding round: the candidate solves a problem with an AI copilot, and Roundz scores how they direct the AI (prompt quality, problem decomposition, judgment, and token efficiency). Roundz evaluates approach, complexity, and correctness of reasoning rather than raw code-execution pass rates. The model is explicitly human-in-the-loop: Roundz filters the funnel and the employer meets only the pre-vetted top roughly 20 percent, then makes the final call (the "80/20 model"). It serves both sides of the market: candidates get realistic practice and confidence, employers get higher-signal, faster screening.

The "why now" is a convergence: (1) real-time voice AI has matured and dropped in cost enough to run natural spoken interviews at scale; (2) AI-native engineering has become the norm, making "directs AI well" a first-class hiring criterion; and (3) employers increasingly distrust gameable, static screens while remote-hiring fraud and impersonation rise. Incumbents can bolt AI features onto old formats, but their core artifact (the auto-graded coding score) is the thing losing signal. Roundz's thesis is that the next assessment standard measures reasoning and AI-direction under live observation, with explainable and defensible scoring, and that a technical founder shipping that product now has a timing advantage.

The near-term commercial question is not whether the market is large (it is, on any reasonable framing) but whether Roundz can convert the agentic-coding wedge into repeatable pilots and paid deals with mid-market, engineering-heavy companies. This memo sizes the opportunity bottom-up, maps the competitive field, and lays out the GTM implications and the honest open risks.

---

## 2. The Problem and the Market Shift

### 2.1 The old signal and why it worked

For most of the last two decades, screening software engineers at volume meant one of two artifacts:

- **Auto-graded coding challenges** (take-home or timed): candidate writes code, hidden test cases run, a pass-rate score ranks candidates.
- **Live human technical interviews:** an engineer spends 45 to 60 minutes on a call watching the candidate solve a problem.

The auto-graded approach won on cost and scale. It let a recruiter filter hundreds of applicants without occupying engineer time. Its signal rested on one assumption: producing a correct, efficient solution unaided, under time pressure, is hard and correlates with real ability.

### 2.2 The structural break: AI dissolved the unaided-difficulty assumption

That assumption no longer holds. AI coding assistants can produce correct solutions to the large majority of standard algorithmic and take-home prompts. The consequence is not subtle:

- **Score compression.** When many candidates can reach a passing score with assistance, the score stops discriminating. A "pass" becomes table stakes rather than signal.
- **Gameability and leakage.** Static problem banks were already vulnerable to memorization and answer-sharing; AI assistance makes casual circumvention trivial.
- **Fraud and impersonation.** Remote, asynchronous formats are susceptible to proxy interviewees, second-screen assistance, and identity fraud. Industry commentary (for example, Glider AI and other assessment vendors) reports that technical-interview and candidate fraud have risen alongside the shift to remote hiring. *(Third-party research / vendor commentary; directional, not a precise statistic.)*

The net effect: the cheapest, most scalable screening artifact is losing the very thing it was bought for, signal.

### 2.3 The cost of getting it wrong is high and rising

Three widely cited third-party anchors frame why hiring quality matters economically. All should be treated as external research, not Roundz data:

- **Cost of a bad hire:** commonly cited at up to roughly 30 percent of the employee's first-year earnings (attributed to US Department of Labor / SHRM-style figures). For an engineer, first-year fully loaded comp is large, so the dollar cost of a mis-hire is material. *(Third-party research anchor; verify current figure.)*
- **Speed matters:** top candidates are reported to be off-market quickly, on the order of roughly 10 days (Officevibe / LinkedIn-style talent research). Slow, low-throughput screening loses the best people. *(Third-party research anchor.)*
- **Engineer time is expensive and scarce:** research such as Stripe's "Developer Coefficient" argues that engineers and technical leaders lose significant time to low-value work; interviewing and low-signal screening are a recurring drain on that time. *(Third-party research anchor; directional.)*

Put together: employers are paying (in engineer hours and mis-hire risk) for a screen that increasingly does not discriminate.

### 2.4 The emergence of AI-native engineering work

The second half of the break is on the demand side of skills. The day-to-day of professional engineering has shifted toward directing AI tools. Increasingly the differentiating competency is not "can you write a binary search from memory," it is:

- Can you decompose an ambiguous problem into steps an AI can execute?
- Can you prompt precisely and iterate efficiently (token and time economy)?
- Can you review AI output critically, catch subtle errors, and know when to override the model?
- Can you reason aloud about tradeoffs, complexity, and design while orchestrating tools?

This is a real, observable skill, and it is almost entirely unmeasured by incumbent assessment products, whose core artifact is still an unaided coding score. That gap is the market opening. The right question to ask a 2026 engineering candidate is closer to "show me how you build correct software with the tools you will actually use," and the right thing to measure is the quality of their reasoning and direction, not whether an isolated function passes hidden tests.

### 2.5 Reframing the category

The category is shifting from **"coding assessment"** (score an artifact) to **"engineering judgment and AI-direction evaluation under live observation, with explainable output."** Roundz is positioned in that reframed category. The rest of this memo sizes and maps it.

---

## 3. Market Sizing (TAM / SAM / SOM)

> **All figures in this section are estimates.** They are built bottom-up from stated assumptions so the inputs can be challenged and replaced. Treat ranges, not point values, as the honest output. These are not audited market figures and should not be cited externally as fact.

### 3.1 Approach

We build three nested layers:

- **TAM (Total Addressable Market):** global spend on technical-hiring assessment plus interview software, the full category Roundz could theoretically touch.
- **SAM (Serviceable Addressable Market):** the realistically reachable slice given product, language, geography, and buyer fit (mid-market, engineering-heavy companies in target English-speaking geos to start).
- **SOM (Serviceable Obtainable Market):** a credible early wedge over roughly 3 years, expressed as (number of customers) x (illustrative annual contract value, ACV).

### 3.2 TAM: two independent lenses

**Lens A: category spend (top-down sanity check).**
Public analyst commentary places the pre-employment / technical assessment software market in the low single-digit billions USD annually, and the broader talent-acquisition / recruiting software market in the tens of billions. A defensible **TAM estimate for technical hiring assessment plus interview software is roughly USD 3 to 6 billion per year globally.** *(Estimate, synthesized from analyst-style category framing; verify with a current market report before external use.)*

**Lens B: bottom-up from company count (assumption-driven).**
- Assume there are on the order of **1,000,000 companies globally that hire software engineers with any regularity** (spanning startups to enterprises). *(Assumption.)*
- Assume the **average annual willingness-to-pay for technical screening / interview tooling is USD 3,000 to USD 6,000** across that mixed population (many pay little or nothing; a minority of high-volume hirers pay far more, so a blended average in the low thousands is deliberately conservative). *(Assumption.)*
- Bottom-up TAM = 1,000,000 x (3,000 to 6,000) = **USD 3 to 6 billion per year.**

The two lenses land in the same range, which increases confidence in the order of magnitude (single-digit billions), while explicitly not claiming precision.

### 3.3 SAM: the reachable segment

Roundz's realistic near-to-mid-term buyer is a **mid-market, engineering-heavy company in target geographies (initially English-language markets such as US, Canada, UK, plus India for engineering volume), hiring engineers at enough volume to feel screening pain but not so locked into enterprise procurement that a young vendor cannot land.**

Bottom-up SAM:
- Assume **~60,000 to 100,000 companies globally fit "mid-market, engineering-heavy, in reachable geos, hiring engineers at meaningful volume."** *(Assumption; derived as a low-single-digit percentage of the 1M-company TAM universe that both hires engineers at volume and sits in reachable segments/geos.)*
- Assume an **achievable blended ACV of USD 15,000 to USD 40,000** for this segment (higher than the TAM blended average because these buyers hire more and value throughput and signal; priced as a per-seat or per-interview-volume subscription). *(Assumption.)*
- SAM = 80,000 (midpoint) x (15,000 to 40,000) = **roughly USD 1.2 to 3.2 billion per year.**

**SAM estimate: on the order of USD 1 to 3 billion per year.**

### 3.4 SOM: a credible early wedge (3-year)

SOM is where honesty matters most for a pre-traction company. We express it as a customer-count ramp against illustrative ACV, not a market-share percentage.

- **ACV assumption (early):** USD 20,000 blended per customer per year (a mid-market annual subscription; some smaller pilots below this, some larger above). *(Assumption.)*
- **Customer ramp assumption (design target, not a forecast):**
  - Year 1: land **10 paying customers** (founder-led sales out of pilots). 
  - Year 2: **50 paying customers** (early repeatability, first non-founder rep or channel).
  - Year 3: **150 paying customers** (a working, if still narrow, sales motion).

| Layer | Basis | Estimated annual value |
|---|---|---|
| TAM | ~1,000,000 eng-hiring companies x ~$3–6K blended | ~$3–6B / yr |
| SAM | ~60–100K mid-market eng-heavy cos in reachable geos x ~$15–40K | ~$1–3B / yr |
| SOM Year 1 | 10 customers x ~$20K ACV | ~$0.2M ARR |
| SOM Year 2 | 50 customers x ~$20K ACV | ~$1.0M ARR |
| SOM Year 3 | 150 customers x ~$20K ACV | ~$3.0M ARR |

*All values are estimates built on the stated assumptions above. Change any assumption (company count, ACV, ramp) and the output changes; these are planning anchors, not promises.*

### 3.5 How to read the sizing

- The **order of magnitude of the opportunity is single-digit billions TAM, one-to-three billion SAM.** That is large enough to matter and does not require heroic assumptions.
- The **SOM is deliberately modest** and expressed as an execution ramp. At epoch 1, the binding constraint is not market size; it is proving repeatable pilot-to-paid conversion. A ~$3M ARR run-rate by Year 3 on ~150 mid-market logos is a credible "we found a motion" milestone, not a ceiling.
- **Expansion optionality (not counted above):** the candidate side (practice / preparation, potentially freemium-to-paid) is a second revenue surface and a top-of-funnel growth engine. It is intentionally excluded from the SOM arithmetic to keep the estimate conservative, but it materially changes the long-run TAM story if the two-sided flywheel works.

---

## 4. Buyer and Segmentation

### 4.1 The two-sided market

Roundz is a two-sided platform, and the sides reinforce each other:

- **Employer side (primary monetization at epoch 1):** buys higher-signal, faster, defensible technical screening. This is where the enterprise-value ACV sits.
- **Candidate side (top-of-funnel and future monetization):** engineers who want realistic practice, feedback, and confidence, especially practice at the new skill of directing AI. Candidates who experience Roundz as a fair, useful interview become advocates and a distribution channel back to employers ("we interviewed on Roundz and it was actually good"). This is a classic two-sided flywheel, but employer revenue should lead.

### 4.2 Employer ICP segments

| Segment | Size / stage | Hiring volume | Why they buy | Sales motion |
|---|---|---|---|---|
| **Seed / early startup** | <50 people | Low but spiky | Founders hire engineers themselves, hate wasting their own time screening; want signal fast | Founder-to-founder, self-serve, low ACV |
| **Growth-stage / mid-market (PRIMARY ICP)** | ~50–1,000 people, eng-heavy | Steady, meaningful | Have a real hiring funnel, feel screen-quality pain, engineer time is expensive, no deep enterprise procurement lock-in | Founder-led then repeatable sales; best land zone |
| **Enterprise** | 1,000+ | High | Care about compliance, integrations, audit-ability; long procurement | Later; requires security/compliance maturity |
| **Recruiting agencies / staffing / interviewing-as-a-service** | Varies | High, per-client | Need to vet candidates fast to place them; could resell or embed | Channel / partnership potential |

**Primary beachhead: growth-stage, engineering-heavy mid-market.** They have enough volume to feel the pain and enough agility to adopt a new vendor without a 9-month procurement cycle.

### 4.3 The economic buyer and where budget sits

- **Economic buyer:** typically **VP Engineering, CTO, or Head of Engineering** for the "is this the right signal" decision, often co-signed by **Head of Talent / Recruiting** who owns funnel throughput and tooling budget. In smaller companies it is the **founder/CEO** directly.
- **Champion vs. buyer:** engineers and hiring managers are natural champions (they feel the pain of low-signal screens and wasted interview loops); talent leaders often hold the budget line.
- **Where budget currently lives:**
  - **Assessment tools budget** (HackerRank / CodeSignal / Codility-type spend): the most direct budget to displace or reallocate.
  - **Interviewing-as-a-service budget** (Karat-type outsourced interviews): a larger per-interview spend Roundz can undercut on cost while adding the AI-direction dimension.
  - **ATS / recruiting software budget:** adjacent; Roundz is more likely to integrate with the ATS than replace it.
  - **Engineer time (shadow budget):** the unpriced but very real cost of engineers running screens themselves. Roundz's ROI story monetizes reclaimed engineer hours even where no line-item "assessment" budget exists.

### 4.4 Buying triggers

- A **painful mis-hire** (recent bad technical hire) that makes screen quality a board-level topic.
- **Scaling hiring** (new funding, new team) that overwhelms manual engineer-run screening.
- **Loss of trust in current screens** (candidates gaming coding tests; suspected fraud).
- **Explicit desire to hire AI-native engineers** and no way to measure that skill today.

---

## 5. Competitive Landscape

> Competitor size, funding, and revenue references below are labeled "reported / estimated" and are directional. Do not cite them as audited facts. The goal is fair categorization, not disparagement; several of these are strong products with real customers.

### 5.1 Category map

**(a) Coding assessment / auto-graded challenges**
HackerRank, CodeSignal, Codility. Large installed bases in technical screening. Strengths: scale, question banks, integrations, brand familiarity with recruiters. Core artifact: auto-graded coding scores and structured assessments. This is precisely the artifact most exposed to AI-assisted score compression. Some are adding AI features (AI-assisted interviewing, plagiarism/AI-use detection, "AI copilot" assessment modes), which validates the shift but also puts their legacy signal under pressure. *(HackerRank and CodeSignal are reported to be well-funded / late-stage private companies; treat specific figures as reported/estimated.)*

**(b) Live technical interviewing / interviewing-as-a-service**
Karat (and Karat-like outsourced-interview providers), Interviewing.io, Filo, BarRaiser. These provide human (or human-plus-tooling) live interviews, often as a managed service or a structured live platform. Strengths: real live signal, structured rubrics, offloading engineer time. Tradeoffs: human interviewing-as-a-service is expensive per interview and capacity-constrained; it does not natively measure AI-direction skill. *(Karat is reported to have raised substantial venture funding; treat as reported/estimated.)*

**(c) AI-interview / async video / candidate-side AI**
HireVue (established async video and structured interview vendor, historically more general/behavioral than deep-technical, with its own history of bias-audit scrutiny) and a wave of newer AI-interviewer startups building voice/agent interviewers. On the candidate side, tools like Final Round AI help candidates prepare for (and in some framings, assist during) interviews, which is itself a driver of employer demand for harder-to-game, proctored formats. Strengths of the AI-interviewer cohort: scalability, cost. Common gaps: many are behavioral/general rather than deep live-technical, and few (if any) natively assess agentic-coding skill with explainable, level-aware rubrics.

**(d) ATS-adjacent**
Greenhouse, Lever, Ashby and similar applicant tracking systems. These own the funnel and workflow but are not technical evaluators; they are integration surfaces and partners more than head-to-head competitors. Roundz should plug into them, not fight them.

### 5.2 Comparison on the axes that matter

Legend: Yes / Partial / No / Varies. Cells reflect the analyst's directional read of typical product positioning, not a certified feature audit; verify per vendor and per current release.

| Capability | Coding assessment (HackerRank / CodeSignal / Codility) | Live / interviewing-as-a-service (Karat / Interviewing.io / BarRaiser) | AI-interview / async (HireVue / newer AI startups) | **Roundz** |
|---|---|---|---|---|
| Real live **voice** interview | No / Partial | Partial (human-led) | Varies (some voice AI) | **Yes (live voice AI interviewer)** |
| **Live code + system-design awareness** (watches Monaco + Excalidraw in real time) | Partial (records code) | Partial (human watches) | Rarely | **Yes (both, in real time)** |
| **Agentic-coding assessment** (scores how candidate directs an AI copilot) | No | No | No / rare | **Yes (unique wedge)** |
| **Explainable, level-aware** scoring (ENTRY/MID/SENIOR rubric, hire verdict) | Partial (scores) | Partial (rubrics) | Partial | **Yes (explainable, level-aware, verdict)** |
| Anti-cheat **proctoring** | Partial / Yes | Partial | Yes | **Yes** |
| **Human-in-the-loop** by design (employer meets top ~20% and decides) | N/A (tool) | Yes (human interviewers) | Varies | **Yes (80/20 model, explicit)** |
| Semantic **resume to JD** matching | Varies | Varies | Varies | **Yes** |

### 5.3 Where Roundz differentiates and where it does not

**Differentiated (the column that is hard to copy quickly):**
- The **agentic-coding round** is the standout. Measuring prompt quality, decomposition, judgment, and token efficiency, i.e., *how well the candidate directs AI*, is the capability aligned to the new nature of engineering work and is largely absent across all four incumbent categories.
- **Live voice reasoning + real-time awareness of both code and design surfaces**, combined into **explainable, level-aware reports with a verdict**, is a genuinely integrated evaluation rather than a score plus a transcript.
- **Human-in-the-loop by design** is both a quality and a trust/compliance advantage (see Section 8).

**Honest competitive realities:**
- Incumbents have **distribution, brand, integrations, and installed bases** Roundz does not. They can add "agentic" or "AI copilot" assessment modes; the question is whether their core artifact and go-to-market can pivot as cleanly as a purpose-built product.
- **Interviewing-as-a-service** already delivers trusted live signal; Roundz's argument there is cost, scale, consistency, and the AI-direction dimension, not "humans are bad at interviewing."
- Being **fair and specific** about competitors is strategically correct: buyers use these tools today, and the pitch is "the signal you bought is decaying and here is what the job actually needs now," not "your current vendor is bad."

---

## 6. Why Now (Timing)

The investment-grade timing argument rests on three converging tailwinds that were not simultaneously true even a couple of years ago:

1. **Real-time voice AI has matured and dropped in cost.** Running a natural, low-latency spoken interview that can follow a candidate's reasoning was impractical/expensive not long ago. It is now feasible at a unit cost that supports a scalable interview product. This is the enabling technology for "live voice interviewer," not a nice-to-have.

2. **AI-native engineering is the norm, so AI-direction is now a hiring criterion.** Because engineers now build with AI copilots daily, "how well do you direct AI" has become a real, board-legible competency. That makes the agentic-coding round *relevant to the buyer's actual job description*, not a novelty. The skill became both important and measurable at the same moment.

3. **Employer distrust of gameable screens plus rising remote-hiring fraud.** The same AI wave that created the new skill also broke the old screen. Employers increasingly suspect their coding tests are gamed and worry about impersonation and second-screen assistance in remote loops (per vendor commentary such as Glider AI; treat as directional third-party research). Demand for harder-to-game, proctored, reasoning-based, live evaluation is rising.

The convergence is the point: the technology to run the new interview, the reason employers now need it, and the failure of the thing it replaces all arrived together. A technical founder shipping a purpose-built product into that window has a timing edge over incumbents who must retrofit and over later entrants who missed the opening.

---

## 7. Trends, Tailwinds, and Headwinds

### 7.1 Tailwinds

- **Secular growth in AI-assisted development** keeps expanding the "measure AI-direction skill" need.
- **Cost pressure on hiring teams** favors tools that reclaim expensive engineer time (ties to the Developer Coefficient anchor).
- **Two-sided flywheel potential:** candidates who like the experience become advocates and a funnel back to employers.
- **Category reframing in Roundz's favor:** as buyers accept that auto-graded scores are decaying, the definition of "good screening" moves toward reasoning + AI-direction, exactly Roundz's turf.

### 7.2 Headwinds and risks

- **Incumbents adding AI features.** HackerRank/CodeSignal-type vendors can ship "AI copilot" or "AI interview" modes and lean on distribution. Mitigation: depth and integration of the agentic-coding evaluation, plus explainability/level-awareness, are harder to bolt on than to build purpose-first.
- **"AI interviewing" skepticism and candidate backlash.** Some candidates dislike being interviewed by AI and worry about fairness. Mitigation: the human-in-the-loop 80/20 model (a human always makes the final call), explainable feedback, and a genuinely useful candidate experience directly address this.
- **Enterprise procurement and compliance friction.** Security reviews, data handling, and vendor risk assessments slow enterprise deals. Mitigation: start mid-market; invest in compliance posture before moving upmarket.
- **Model-cost volatility.** Voice + LLM inference costs can move; margins depend on them. Token efficiency (which Roundz already scores) is also relevant to its own unit economics. Mitigation: model-agnostic architecture, cost monitoring, pricing that accommodates variance.
- **Signal-validity scrutiny.** Buyers will (rightly) ask whether Roundz's scores predict on-the-job performance. Until Roundz has outcome data, this is answered with rubric transparency and pilot results, not claims. This is an open question (Section 10), not a solved one.

---

## 8. Regulatory and Ethical Considerations

> The specifics below are stated as of general knowledge and may have changed. **Verify current legal status before relying on any of this externally.** This is not legal advice.

AI in hiring is a regulated and scrutinized area, and the direction of travel is toward more oversight. Key reference points:

- **NYC Local Law 144:** requires bias audits and candidate notification for automated employment decision tools used for NYC roles. *(As of general knowledge; verify current status and scope.)*
- **EU AI Act:** classifies AI systems used in employment/recruitment among high-risk categories, implying obligations around risk management, transparency, human oversight, and documentation. *(As of general knowledge; verify current status, timelines, and applicability.)*
- **US EEOC guidance:** has signaled that AI-driven selection tools remain subject to anti-discrimination law (adverse-impact analysis under Title VII, ADA considerations). *(As of general knowledge; verify current guidance.)*

**Why this is a constraint AND a moat for Roundz.** Regulation raises the bar for any AI-in-hiring product, which is a cost and a diligence burden. But the emerging regulatory expectations (transparency, explainability, human oversight, defensibility) map directly onto how Roundz is built:

- **Explainable, rubric-based scoring** supports the transparency and documentation expectations far better than opaque black-box scores.
- **Level-aware rubrics** support defensibility (evaluating against role-appropriate criteria).
- **Human-in-the-loop by design (the 80/20 model)** directly satisfies "human oversight / human makes the final decision," a recurring regulatory theme, and is a strong answer to candidate-fairness objections.

The strategic read: as compliance requirements tighten, black-box or purely-automated approaches face growing friction, while a platform architected around explainability and human oversight can turn compliance into a selling point. This should be an explicit part of the enterprise pitch, with the caveat that Roundz still needs real bias-audit and validation work (Section 10), not just an architecture that is compatible with it.

---

## 9. Go-to-Market Implications

The research points to a clear early strategy. Details belong in the sales and investor docs; here are the market-driven implications.

- **Wedge = the agentic-coding round.** It is the one capability no incumbent category offers and the one most aligned to how engineering now works. Lead with it. It is the "only Roundz does this" hook that earns the meeting and reframes the category on Roundz's terms.
- **Beachhead segment = growth-stage, engineering-heavy mid-market** in reachable geos. Enough hiring pain and volume to care, enough agility to buy from a young vendor. Avoid enterprise procurement early; avoid the lowest end where willingness-to-pay is thin.
- **Positioning = "your coding screen is losing signal; the job is now directing AI; measure that, with explainable, human-in-the-loop evaluation."** Anchor with the third-party research (bad-hire cost, speed-to-hire, engineer time drain, rising fraud), never with fabricated Roundz metrics.
- **Sequencing:**
  1. **Epoch 1 (now):** founder-led pilots. Instrument everything (pilot outcomes, employer reactions, candidate NPS, win/loss reasons). The goal of epoch 1 is *learning and proof*, not scale.
  2. **Convert pilots to paid** and extract the first repeatable pitch, ICP refinements, and ACV reality.
  3. **Layer the candidate side** as a top-of-funnel and advocacy engine once employer value is proven.
  4. **Then** invest in compliance posture and integrations to move upmarket.
- **Two-sided leverage:** every candidate who has a good Roundz interview is a potential advocate and a warm intro to their employer. Design the candidate experience as a growth channel, but keep employer revenue in the lead.
- **Honesty as positioning:** the pitch's credibility depends on not overclaiming (no code-execution pass-rate claims; "evaluates approach, complexity, and correctness of reasoning"). In a market wary of AI-hiring hype, disciplined honesty is a differentiator with technical buyers.

---

## 10. Key Risks and Open Questions

Honest list of what could break the thesis and what data Roundz still needs.

**Market / demand risks**
- Will mid-market buyers pay for a new screening layer, or fold "AI-direction" into existing tools once incumbents ship it?
- Is the agentic-coding wedge a "must have" for buyers today, or still "interesting" (ahead of budget)?

**Product / signal-validity risks (most important to validate)**
- **Does the Roundz score predict on-the-job performance?** This is the core unproven claim. Needs outcome data over time.
- Does the agentic-coding rubric measure durable skill or just familiarity with current tools?
- Does explainability hold up under adversarial scrutiny (candidates, auditors, regulators)?

**Competitive risks**
- Incumbents' distribution advantage if they ship credible AI-direction assessment.
- New well-funded AI-interviewer entrants targeting the same wedge.

**Execution / operational risks**
- Model-cost volatility compressing margins.
- Proctoring/anti-cheat arms race as candidates adapt.
- Compliance/security readiness gating enterprise expansion.

**Data Roundz still needs (the epoch-1 measurement agenda)**
- **Pilot outcomes:** did employers agree with Roundz's top ~20%? Did those hires perform?
- **Win rate and sales-cycle length** by segment.
- **Realized ACV** vs. the $20K assumption.
- **Candidate NPS / completion rates / fairness feedback.**
- **Unit economics** per interview (voice + inference cost vs. price).
- **Bias / adverse-impact data** to support compliance claims.

Until these exist, the sizing and GTM in this memo are informed hypotheses, not validated facts. Epoch 1 exists to convert hypotheses into evidence.

---

## 11. Sources and Assumptions Note

**On the numbers.** Every market-size figure (TAM/SAM/SOM), adoption statistic, and cost figure in this document is either a labeled third-party research anchor or an estimate built from explicitly stated assumptions. The TAM/SAM/SOM values are planning estimates derived from stated company-count and ACV assumptions and, in the TAM case, cross-checked against analyst-style category framing. They are ranges and order-of-magnitude anchors, not audited market data. Change any input assumption and the outputs change.

**Third-party research anchors cited (all external, none are Roundz data; verify current figures before external use):**
- Cost of a bad hire up to roughly 30 percent of first-year earnings (US Department of Labor / SHRM-style figures).
- Top candidates off-market in roughly 10 days (Officevibe / LinkedIn-style talent research).
- Engineers and technical leaders lose significant time to low-value work / low-signal screening (Stripe "Developer Coefficient").
- Rising technical-interview and candidate fraud with remote hiring (Glider AI and similar assessment-vendor commentary).

**On competitors.** All references to competitor size, funding, valuation, or revenue are labeled "reported / estimated" and are directional. The feature comparison reflects the analyst's directional read of typical product positioning, not a certified per-release audit. Verify per vendor before external citation.

**On regulation.** Regulatory references (NYC Local Law 144, EU AI Act, EEOC guidance) are stated as of general knowledge and may have changed. Verify current legal status; this is not legal advice.

**On Roundz claims.** This memo makes no code-execution or test-case pass-rate claims: Roundz evaluates approach, complexity, and correctness of reasoning. No customer names, logos, testimonials, funding, or revenue for Roundz are asserted, because at epoch 1 they would be fabricated.

**Recommended action before any external use (board, investor, sales):** replace the assumption inputs with any hard numbers Roundz obtains from pilots, and validate the TAM/SAM range against a current third-party market report.
