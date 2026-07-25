# Roundz: Investor Narrative and Deck Outline

**The AI interview engine for the AI-native era.**

*Stage: pre-seed / seed. Status: product built and demoable, early GTM, pre-traction.*
*Companion doc for market sizing: [../02-market-research/Market_Research_Deep_Dive.md](../02-market-research/Market_Research_Deep_Dive.md)*

> This is a working draft for the founder to refine. Traction figures are intentionally left as bracketed placeholders. Fill them with real, verifiable numbers only.

---

## Part A: Investor Narrative

### The one-line thesis

The way we screen engineers broke at exactly the moment the job of an engineer changed. Roundz runs a company's real technical interview loop with a live voice AI interviewer, watches the candidate code and design in real time, and adds a round no one else has: measuring how well an engineer directs an AI copilot. We filter for signal; the employer meets the top 20% and makes the call.

### The problem: the screening signal died

For fifteen years, technical hiring ran on a shared assumption: a candidate who can solve an algorithm puzzle unassisted, on a shared screen, is a proxy for a good engineer. That proxy is now broken in two directions at once.

First, the take-home and the online-assessment are trivially gameable. Any candidate with a second tab and a frontier model produces clean, optimal, well-commented solutions in seconds. Screening scores went up and their correlation with real ability went to zero. Remote interview fraud is now an industry-scale problem, not an edge case (see Glider AI and vendor reports referenced in the market doc).

Second, and more importantly, the job itself changed. The frontier engineer in 2026 does not write most lines of code by hand. They direct AI: decomposing problems, writing precise prompts, reviewing and correcting generated output, knowing when to trust the model and when to override it. None of the incumbent screening tools measure any of this. They test a skill that matters less each quarter and ignore the skill that now separates a great engineer from an average one.

Meanwhile the cost of getting it wrong is unchanged and brutal. A bad engineering hire runs roughly 30% of first-year compensation once you count ramp, management drag, and backfill (US DoL / SHRM estimates). And the best candidates are gone fast: the top-candidate hiring window is on the order of 10 days (Officevibe / LinkedIn). Engineering leaders are stuck between slow, high-signal human loops that lose candidates and fast, low-signal automated screens they no longer trust.

### The solution: run the real loop, keep the human at the top

Roundz is not another quiz bank. It runs a company's actual technical interview loop, end to end, with a live voice AI interviewer that holds a real conversation, probes reasoning, and adapts to the candidate's answers. While the candidate talks, Roundz watches their live code in a Monaco editor and their system-design work on an Excalidraw whiteboard, in real time, the way a human interviewer would.

Every interview produces an explainable, level-aware report: rubric-scored against ENTRY, MID, or SENIOR expectations, with a clear verdict from STRONG_HIRE to STRONG_NO_HIRE, and the evidence behind each score. Anti-cheat proctoring runs throughout. Semantic resume-to-JD matching sits at the top of the funnel so employers screen the right people in the first place.

The model is deliberately human-in-the-loop, what we call the 80/20 model: Roundz does the heavy, repeatable filtering work, and the employer spends their scarce human time only on the top ~20% and always makes the final hiring decision. We are not trying to remove the human. We are trying to make sure the human only meets people worth meeting.

### The wedge: the first interview that scores how you direct AI

Here is the insight competitors do not have. Roundz includes an agentic-coding round where the candidate solves a problem *with* an AI copilot, and the platform scores how well they direct it: prompt quality, problem decomposition, judgment about when to accept or reject the AI's output, and token efficiency. This is the first interview format built to measure the actual 2026 engineering skill.

This flips the AI-cheating problem on its head. Everyone else is losing an arms race trying to stop candidates from using AI. We make using AI the point, and we measure whether they are good at it. That reframing is the whole company: it turns the industry's biggest headache into our core signal, and it is live and demoable today.

### Why now

Three curves crossed at once. Voice AI matured to where a natural, low-latency spoken interview is finally possible. AI-native engineering became the norm, so "can you direct a copilot" is now the question that predicts on-the-job performance. And trust in the gameable screen collapsed under remote fraud. A tool that assumes AI is in the room, and grades on it, could not have been built or sold two years ago and will feel obvious two years from now.

### Why us

Founder-market fit is the honest core of this story. Roundz was built by a technical founder who shipped a genuinely deep product solo: real-time multi-modal interviewing, LLM-based evaluation, and a novel agentic-coding round that no funded competitor offers. This is not a deck in search of an engineer. The hard technical bet is already de-risked and demoable. What the round funds is turning a category-defining product into a category-defining company.

### The honest state of things

We are early and pre-traction. We are not going to show you invented logos or fake revenue. The strength here is a built product with a unique wedge, a clear "why now," and a founder who can ship. The next 12 months are about converting product depth into design partners, a repeatable founder-led sales motion, and the first proprietary agentic-coding dataset that compounds into a durable moat.

---

## Part B: Slide-by-Slide Deck Outline

Target length: 14 slides plus two honesty appendices. Each slide lists the headline takeaway, the content to show, and a speaker note.

---

### Slide 1: Title / One-liner

**Headline:** Roundz: the AI interview engine for the AI-native era.

**Content:**
- Logo, roundz.ai, one clean line: "We run your real technical interview loop with a voice AI, and we're the only ones who measure how well an engineer directs AI."
- Stage tag: pre-seed / seed. [INSERT: raise amount once decided]
- Founder name and contact.

**Speaker note:** Open on the reframing, not the feature list. "Everyone is trying to stop candidates from using AI in interviews. We think that's backwards, and I'll show you why in three minutes."

---

### Slide 2: Problem

**Headline:** The screening signal died, and the job changed underneath it.

**Content:**
- Two-column contrast:
  - *Signal died:* take-homes and online assessments are trivially solvable with a second tab and a frontier model. Scores went up, correlation with real ability went to zero. Remote interview fraud is now industry-scale (Glider AI).
  - *Job changed:* frontier engineers direct AI (decompose, prompt, review, override). Incumbent tools measure none of it.
- Cost of getting it wrong: bad hire ~30% of first-year comp (US DoL / SHRM); top candidates gone in ~10 days (Officevibe / LinkedIn).

**Speaker note:** Land the double failure. Old tools test a fading skill AND are gameable. Hiring leaders feel this pain daily but have no tool built for the new reality.

---

### Slide 3: Why Now

**Headline:** Three curves just crossed.

**Content:**
- Voice AI maturity: natural, low-latency spoken interviews are finally viable.
- AI-native engineering is the norm: "can you direct a copilot" now predicts job performance.
- Collapse of trust in the gameable screen: remote fraud broke the old model.
- One-line: could not have been built or sold 2 years ago; obvious in 2 years.

**Speaker note:** Timing is the investor's real question. Make it visual: three rising lines intersecting at "now." This is a market that just became addressable.

---

### Slide 4: Solution

**Headline:** Run the real interview loop; keep the human at the top (the 80/20 model).

**Content:**
- Roundz runs your actual technical loop end to end: live voice AI interviewer, real-time awareness of the candidate's code (Monaco) and system design (Excalidraw), anti-cheat proctoring, semantic resume-to-JD matching.
- Output: explainable, level-aware (ENTRY / MID / SENIOR) rubric-scored report with a verdict (STRONG_HIRE to STRONG_NO_HIRE) and evidence.
- 80/20 model diagram: Roundz filters the funnel; employer meets the top ~20% and always makes the final call.
- Two-sided: candidates practice, employers hire.

**Speaker note:** Emphasize human-in-the-loop. We are not selling "AI decides who you hire." We are selling "your team only spends time on people worth their time." That framing disarms the compliance and bias objection early.

---

### Slide 5: The Wedge / Unfair Insight

**Headline:** The first interview that scores how well you direct AI.

**Content:**
- The agentic-coding round: candidate solves *with* an AI copilot; Roundz scores prompt quality, problem decomposition, judgment (when to accept vs. override the AI), and token efficiency.
- The reframe: competitors fight a losing arms race to block AI. We make using AI the test.
- This measures the actual 2026 skill, and no funded competitor has it.
- Callout: live and demoable today.

**Speaker note:** This is the centerpiece: slow down here. This one insight turns the industry's biggest problem (AI cheating) into our core signal. If they remember one slide, it should be this one.

---

### Slide 6: How It Works

**Headline:** Multi-modal, real-time, explainable, and mapped to buyer pain.

**Content:**
- Flow: resume-to-JD match, then live voice interview, then live code + design observation, then the agentic-coding round, then the level-aware scored report.
- Table mapping capability to buyer pain:

| Capability | Buyer pain it kills |
|---|---|
| Live voice AI interviewer | Interviewer hours don't scale; scheduling drag |
| Real-time code + design awareness | Static take-homes are gameable and low-signal |
| Agentic-coding round | No tool measures AI-direction skill |
| Level-aware rubric + verdict | Inconsistent, unexplainable hire/no-hire calls |
| Anti-cheat proctoring | Remote interview fraud |

- Honesty note: correctness is evaluated on approach, complexity, and reasoning quality against reference answers (no code execution / no test-case pass rates).

**Speaker note:** If asked "do you run the code?": be direct. We evaluate approach, complexity, and correctness of reasoning against reference answers, which is exactly how a strong human interviewer assesses a whiteboard solution. That is a feature for judgment-heavy and design questions, not a gap.

---

### Slide 7: Product Depth / Demo

**Headline:** It's built. Watch it run.

**Content:**
- Screenshots: live interview view, real-time code/whiteboard, sample explainable report with verdict.
- [INSERT: 90-second demo video link] and [INSERT: live demo booking link].
- Emphasis: this is shipped software, not mockups, including the live agentic-coding round.

**Speaker note:** For a pre-seed, a working demo is the strongest possible de-risker. Offer a live run. The "solo technical founder already shipped this" subtext should be loud here.

---

### Slide 8: Market

**Headline:** A large, active spend pool inside technical hiring and assessment.

**Content:**
- TAM / SAM / SOM pulled from [../02-market-research/Market_Research_Deep_Dive.md] (label all as estimates; do not invent new figures here).
- Beachhead SOM: tech-hiring teams feeling the AI-screening pain first.
- Supporting cost drivers (labeled estimates): bad-hire cost ~30% first-year comp; ~10-day top-candidate window; developer-time cost (Stripe Developer Coefficient).

**Speaker note:** Do not freelance numbers on stage. Cite the market doc's build-up. Frame the wedge (AI-native teams) as the entry point into the broader assessment spend.

---

### Slide 9: Competition

**Headline:** Everyone tests the old skill; we test the new one.

**Content:**
- 2x2: X-axis = static/gameable to live/interactive; Y-axis = measures rote coding to measures AI-direction + reasoning. Roundz sits top-right, alone.
- Comparison table (no trash-talk):

| | Coding-assessment incumbents | Interview outsourcing / agencies | ATS + screening | Roundz |
|---|---|---|---|---|
| Live voice reasoning interview | Limited | Human (costly, unscalable) | No | Yes |
| Agentic-coding round | No | No | No | Yes (unique) |
| Explainable, level-aware scoring | Partial | Subjective | No | Yes |
| Human-in-the-loop 80/20 | n/a | Yes | n/a | Yes |

**Speaker note:** Respect incumbents: they built the last era's category well. Our claim is narrow and defensible: only Roundz measures AI-direction, combines it with live voice reasoning, and returns explainable scoring.

---

### Slide 10: Business Model

**Headline:** Employer credit model plus subscriptions, land-and-expand from a pilot.

**Content:**
- Employers buy interview credits (Razorpay-backed credit model, already built) and/or subscribe.
- Two-sided funnel: candidate practice drives top-of-funnel and word of mouth; employer hiring is the revenue engine.
- Land-and-expand: start with one team's pilot loop, expand to more roles and teams.
- [INSERT: pricing per credit / seat tiers once validated with design partners]

**Speaker note:** Credit model lowers the buyer's first-purchase risk (pay for what you run) and gives a clean expansion path. Note the billing primitive is live, not roadmap.

---

### Slide 11: Go-To-Market

**Headline:** Founder-led motion, agentic-coding as the beachhead.

**Content:**
- Epoch 1: founder-led sales to AI-native engineering teams who feel the screening-signal pain most acutely.
- Wedge message: "the only interview that measures how your candidates direct AI."
- Motion: warm network plus targeted cold outreach; free/low-friction pilot offer to convert design partners.
- Reference the sales toolkit / founding-sales playbook for cadence and scripts.
- Candidate-side practice as a low-cost acquisition and content loop.

**Speaker note:** Be explicit that early GTM is founder-led and hands-on, which is correct for this stage. The wedge doubles as the marketing hook.

---

### Slide 12: Traction & Pipeline

**Headline:** Early, honest, and building.

**Content (PLACEHOLDERS: fill with real, verifiable numbers only):**
- [INSERT: # design partners in conversation / signed]
- [INSERT: # pilots run or scheduled]
- [INSERT: waitlist size]
- [INSERT: LOIs or verbal commitments]
- [INSERT: candidate-side usage / interviews completed, if any]
- [INSERT: notable qualitative feedback quotes]

**Speaker note:** Do not invent anything. If a box is empty, leave it empty or delete the line. Pre-seed investors reward honesty and a built product far more than fabricated metrics. Pair this slide with the demo: proof of product substitutes for proof of revenue at this stage.

---

### Slide 13: Moat / Why We Win

**Headline:** Product depth today, a data flywheel and compliance edge over time.

**Content:**
- Product depth: real-time multi-modal interviewing plus the unique agentic-coding round is hard to replicate.
- Data flywheel: every agentic-coding round builds a proprietary dataset on how strong engineers direct AI, calibrating scoring in a way latecomers cannot easily copy.
- Explainable + level-aware scoring as a regulatory moat: as hiring-AI regulation tightens, defensible, auditable, evidence-backed scoring becomes a requirement, not a nicety.
- Founder-market fit: technical founder who already shipped the hard parts.

**Speaker note:** Sequence the moat by time: depth now, data over months, compliance as regulation lands. Investors want to know why this is not a weekend clone: the answer is the accumulating agentic dataset plus explainability.

---

### Slide 14: Team

**Headline:** Founder-market fit: the hard technical bet is already shipped.

**Content:**
- [INSERT: founder bio: technical background, why this founder builds this product]
- Proof point: shipped a deep multi-modal, LLM-evaluated interview platform with a novel agentic round, solo / small team.
- [INSERT: advisors, early hires, key domain experts]
- [INSERT: planned first hires the round funds]

**Speaker note:** Lead with what is already built as evidence of execution. Be candid that the team is small; frame the raise as adding the go-to-market and product muscle around a proven builder.

---

### Slide 15: The Ask

**Headline:** [INSERT: raise amount] to convert a built product into a category.

**Content (template, fill with real plan):**
- Raise: [INSERT: $ amount] [INSERT: SAFE / priced round, target valuation or cap]
- Use of funds (illustrative split, adjust to plan):

| Area | ~% | What it buys |
|---|---|---|
| Product / engineering | [INSERT %] | Harden agentic-coding round, employer dashboard, integrations |
| GTM / sales | [INSERT %] | Founder-led pilots into repeatable motion, first GTM hire |
| Key hires | [INSERT %] | [INSERT: roles] |
| Infra / model costs | [INSERT %] | Voice, evaluation, and transport compute at pilot scale |
| Runway buffer | [INSERT %] | [INSERT: months of runway] |

- Milestones this round buys: [INSERT: # paying design partners, [INSERT: usage / revenue target], repeatable sales motion, agentic dataset v1].

**Speaker note:** Tie every dollar to a milestone that de-risks the next round: paying design partners, a repeatable motion, and the first proprietary dataset. Give the number and the destination, not just the number.

---

## Appendix A: What makes this fundable at pre-seed (honesty box)

> **The bet in plain terms.** This is early and pre-traction. What is de-risked is the hard part most pre-seed decks only promise: a deep, multi-modal, AI-native interview product is *built and demoable*, including a genuinely novel agentic-coding round no funded competitor has. The remaining risk is commercial (will teams buy, how fast, at what price), which is exactly the risk this round is designed to retire. You are underwriting a proven builder with a timely, unique wedge, not a slide deck. That is the honest case, and it is a strong one.

---

## Appendix B: Risks and how we de-risk

| Risk | Why it's real | How we de-risk |
|---|---|---|
| No traction yet | Pre-traction, early GTM | Founder-led pilots with a free/low-friction offer; convert to paying design partners in the round period |
| No code-execution sandbox | Correctness is LLM-judged from written code + reference answers, not test-case pass rates | Position as approach/reasoning evaluation (mirrors strong human interviewers); reference answers + level-aware rubric keep it defensible; sandbox is a possible later addition, not a blocker |
| AI-hiring bias / regulation | Automated hiring is under increasing scrutiny | Human-in-the-loop 80/20 (employer decides); explainable, evidence-backed, level-aware scoring built for auditability |
| Incumbents copy the agentic round | Big players have distribution | First-mover data flywheel + product depth; the proprietary AI-direction dataset compounds and is hard to replicate |
| Solo / small team execution risk | Bandwidth limits | Hard technical bet already shipped; round funds first GTM and product hires |
| LLM / infra cost and dependency | Reliance on third-party models (Gemini, Bedrock/Claude, Deepgram, etc.) | Credit pricing covers variable cost; modular provider layer allows swapping models as economics shift |

---

## Appendix C: Real architecture (for technical diligence)

Use this for the tech/moat conversation. State it accurately.

| Layer | Technology |
|---|---|
| Live voice interviewer | Google Gemini 2.5 Flash |
| Evaluation / scoring | AWS Bedrock (Claude) |
| Resume ↔ JD matching | Gemini (semantic) |
| Speech-to-text | Deepgram |
| Text-to-speech | Kokoro |
| Real-time transport | Pipecat over Daily / WebRTC |
| System of record | Node/Express + Prisma + Postgres + AWS Lambdas |
| Billing | Razorpay (credit model) |
| Code / design capture | Monaco editor + Excalidraw whiteboard |

**Note on correctness:** there is no code-execution sandbox. Correctness is LLM-judged from the candidate's written code and reference answers: the platform evaluates approach, complexity, and correctness of reasoning. Do not claim test-case pass rates.
