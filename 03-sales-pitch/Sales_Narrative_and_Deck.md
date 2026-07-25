# Roundz: Sales Narrative & Pitch Deck (Employer / CTO motion, agentic-coding wedge)

> Built on `08_Product_Ground_Truth.md` (code-verified) + `Founding_Sales_Playbook_Notes.md`.
> Audience: CTO / VP Eng / Head of Eng at 50–250-person, post-Series-A→C companies.
> Positioning frame: **"An engineering filter for the AI-native era, not an HR tool."**
> Honesty rules enforced: interviewer = Gemini, evaluator = Claude; NO code-execution claims;
> third-party stats labeled as industry research, not Roundz outcomes.

---

## PART A: THE COHESIVE NARRATIVE (the spine of everything)

This is the story told the same way in the deck, the cold email, the demo, and the website.
Structure (Kazanjy): **Problem → Cost of status quo → What changed → Solution → How it works → Proof → Ask.**

### 1. The Problem (make them nod)
> "Hiring engineers is broken in a new way. Your screening tools test whether code *runs*,
> but in 2026, anyone can make code run with an AI. So the signal you get at the top of the
> funnel is worthless: candidates sail through HackerRank, then fail the live round. Your best
> engineers burn their week interviewing people who were never going to make it, and the
> senior engineers you actually want refuse to do LeetCode at all."

Two truths a CTO already feels:
- **The signal collapsed.** Static coding tests measure output; AI generates correct output
  without understanding. Pass-the-screen-fail-the-onsite is now the norm.
- **The job itself changed.** Engineers now *direct AI agents* to write code. You're still
  interviewing for hand-written algorithms, a skill that's being abstracted away, instead of
  for the skill that now matters: **getting correct results out of AI tools.**

### 2. The Cost of the Status Quo (agitate: use as industry research)
- **Bad hire:** up to 30% of first-year comp; for engineers, broken code compounds (US Dept of Labor / SHRM).
- **Vacancy:** top candidates gone in ~10 days; slow process loses them (Officevibe / LinkedIn).
- **Leadership time:** technical leaders lose ~a third of their week to low-signal screening (Stripe Developer Coefficient).
- **The new risk:** candidate fraud up sharply since remote hiring; unproctored cheating is common (Glider AI).
> Framing line: *"Doing this manually isn't free, the industry data puts the all-in cost of
> broken technical hiring in the hundreds of thousands per year per team."*
> (Label as industry estimate. Once you have customer data, replace with your own.)

### 3. What Changed / Why Now (the wedge)
> "Two things became possible at once. Voice AI got fast enough to hold a real technical
> conversation, probing *why*, not just *what*. And AI became the way engineers actually work.
> So for the first time you can run a real interview at the top of the funnel AND test the skill
> that matters now: how well someone directs an AI to solve a hard problem."

### 4. The Solution (the paradigm, one sentence)
> "Roundz is an AI interview engine that runs your real technical loop, voice-driven,
> code- and design-aware, with an AI copilot round that measures how a candidate thinks *with*
> AI, and hands your team explainable, rubric-scored reports on only the pre-vetted top candidates."

### 5. How It Works (features → use case → business value; never feature-listing)
| What it does | How it works (verified) | Why the CTO cares |
|---|---|---|
| **Voice interview that probes reasoning** | Live voice agent (real-time, human-like turn-taking) asks follow-ups, adapts Socratically | Catches the "passed the test, can't explain it" candidate at step 1, not week 3 |
| **Watches them work** | Streams their live code (Monaco) and system-design whiteboard (Excalidraw) to the agent as they build | Signal on approach and communication, not just a final answer |
| **Agentic-coding round (the wedge)** | Candidate solves *with* an AI copilot; every prompt, decomposition, accept/reject/edit and token-efficiency is captured and scored | Measures the 2026 job: can they get correct results out of AI? No competitor tests this |
| **Level-aware rubric scoring** | ENTRY/MID/SENIOR rubrics, weighted per skill + question type | Matches *your* bar, consistently, every time, no interviewer variance |
| **Explainable report** | Strengths, growth areas, per-criterion scores, hire verdict (STRONG_HIRE→STRONG_NO_HIRE) with reasoning | Defensible decisions, not a black-box number |
| **Anti-cheat proctoring** | Gaze/face (MediaPipe) + keyboard/clipboard telemetry | Confidence the signal is real in a remote world |
| **Full hiring pipeline + credits** | Post → semantic resume match → shortlist → AI screen (1 credit/candidate) → evaluate → you decide | Runs 24/7; your team only meets the pre-vetted top slice |

**Human-in-the-loop, always:** Roundz filters; your team closes. This is the objection-killer, so
lead with it.

### 6. Proof (what we have TODAY, honestly)
- **Product depth as proof:** the agentic-coding telemetry, the tested "won't abandon a candidate
  who goes quiet" reliability guard, level-aware rubrics, show the actual evaluation report in the demo.
- **Candidate-side signal:** candidates report the AI feedback is detailed and accurate (they agree
  with it). Turn this into a quote/short testimonial.
- **Logic-of-value proof** (until customer ROI exists): walk the CTO through their own numbers live.
- **What to build:** 1–3 design-partner case studies from the first pilots (see the pilot offer).

### 7. The Ask
> "Give us one open req. We'll screen your next batch of candidates this week and show you the
> reports side-by-side with your own read. If the top-20% we surface isn't better signal than your
> current screen, you've lost nothing."
De-risked, specific, small first commitment, but **priced** (a paid pilot / credit pack), not free-forever.

---

## PART B: THE PITCH DECK (chapter-structured, ~14 slides + appendix)

Each slide: **headline = the takeaway** (not a label), one visual, minimal text. Speaker notes below each.

### Chapter 1: Frame
**Slide 1: Title**
- Roundz. "The AI interview engine for the AI-native era."
- Sub: Run your real technical loop with voice AI, meet only the pre-vetted top 20%.
- Notes: 10-sec context: who you are, that you'll keep it to X minutes, and that by the end you'll
  jointly decide if a pilot makes sense (up-front contract).

### Chapter 2: Problem (agitate)
**Slide 2: "Your screening signal just died."**
- Visual: funnel where "passed HackerRank" and "passed live" have diverged.
- Point: AI makes code run without understanding → top-of-funnel signal is noise.
- Notes: get the nod. Ask: "How many of your last onsite failures had passed the coding screen?"

**Slide 3: "And the job itself changed."**
- Visual: engineer directing an AI agent vs. hand-writing an algorithm.
- Point: you're testing a skill that's being abstracted away; not testing the one that now matters.

**Slide 4: "What it's costing you." (industry data)**
- Visual: four cost tiles (bad hire / vacancy / leadership time / fraud), labeled *industry research*.
- Notes: don't over-claim; anchor the pain, then say "let's put your real numbers on it later."

### Chapter 3: Why Now
**Slide 5: "Two shifts made a new kind of interview possible."**
- Voice AI fast enough for real technical dialogue + AI became how engineers work.

### Chapter 4: Solution
**Slide 6: "Roundz runs your real loop: and meets you at the top 20%."**
- One-sentence solution + the 80/20 human-in-the-loop model as a simple diagram.

**Slide 7: "The round no one else has: interviewing *with* AI."** ← the wedge, spend time here
- Visual: the copilot round, prompts, decomposition, token budget, accept/reject, and the
  competency score it produces.
- Point: we measure how they *direct* AI (prompt quality, problem decomposition, judgment, efficiency).
- Notes: this is the "teach them something they didn't know" Challenger moment.

### Chapter 5: How it works (map to their pains)
**Slide 8: The pipeline** (post → match → shortlist → AI screen → evaluate → you decide), 24/7, credit-metered.
**Slide 9: The interview** (voice + live code + whiteboard awareness + proctoring).
**Slide 10: The report** (real screenshot: strengths/growth, per-criterion scores, verdict + reasoning).
- Notes: land "explainable, matches your bar, consistent every time."

### Chapter 6: Proof / Trust
**Slide 11: "Human-in-the-loop. You always make the call."** (objection pre-empt)
**Slide 12: Proof** (candidate feedback quote + product-depth proof; design-partner logos once you have them).

### Chapter 7: Pricing / Ask
**Slide 13: "Start with one req." (the pilot)**
- The de-risked, priced pilot; what they give (1 open role), what they get (reports this week).
**Slide 14: Next steps** (concrete: pilot start date, which req, who's involved). Book it before the call ends.

### Appendix (build a slide each time a question recurs >once)
- Anti-cheat detail · Stack/security (Gemini interviewer, Claude evaluator, proctoring, data handling)
  · Interview types & levels · Rubric methodology · "Does it replace my team?" · vs HackerRank/Karat/CodeSignal
  · Candidate experience · Integrations/ATS · Data privacy/SOC2 posture.

---

## PART C: Objection handling (deck appendix + demo)
| Objection | Response |
|---|---|
| "AI can't judge like my staff engineer." | Correct, that's why it *filters*, not *closes*. You still meet the top 20%; we just make sure you're not wasting the meeting. |
| "Candidates will hate being interviewed by a bot." | Frame as the fast-pass: 24/7, no scheduling, honest feedback. Senior candidates skip the LeetCode grind. |
| "Is this just keyword resume matching?" | No, semantic skill matching (embeddings), and the real signal is the live interview + copilot round, not the resume. |
| "Does it run/grade my exact code?" | We assess reasoning, approach, and correctness of logic from the code and the conversation, we don't just check if it compiles (that's the trap that's failing you today). |
| "Why should I trust the score?" | Every score is explainable with per-criterion reasoning against your rubric and level, not a black-box number. |
| "Not now / no budget." | Isolate: is it timing or fit? Opportunity cost accrues every open week. Pilot is one req, priced small, results this week. |

---

## PART D: Taglines / one-liners (pick + A/B test)
- "The AI interview engine for the AI-native era."
- "Interview for how engineers actually work now, with AI."
- "Your screening tests if code runs. We test if the *engineer* does."
- "Meet only the top 20%. Let AI vet the rest, and keep the final call."
- "The first interview that measures how well you direct AI."
