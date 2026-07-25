# Roundz: Product Ground Truth (Code-Verified)

> Built from a full read of all three codebases on 2026-07-24:
> - UI: `interview-networker-ui` (Next.js 14)
> - API: `interview-networker-api` (Node/Express + Prisma + Lambdas)
> - Interview engine: `mock-interview-api` (Python FastAPI + Pipecat)
>
> Purpose: a single source of what the product **actually does**, so sales/marketing
> claims stay defensible. Flags where the existing KB (`00_...md`) is inaccurate.

---

## 1. What is unambiguously TRUE and strong (market it hard)

| Capability | Evidence |
|---|---|
| **Live voice AI interviewer**: real-time, human-like turn-taking, interruptible | `mock-interview-api` Pipecat pipeline; Silero VAD + LocalSmartTurnAnalyzerV3; `interview_bot.py` |
| **Multi-phase structured interviews**: INTRO, BEHAVIORAL, CODING, SYSTEM_DESIGN, AI_ASSISTED_CODING, QNA, WRAP_UP | `WorkflowStepType`/`TaskType` across all 3 repos |
| **Live code + whiteboard co-awareness**: editor (Monaco) and Excalidraw stream to the agent in real time; agent reasons about the candidate's evolving solution | UI `CodeEditorPanel.tsx`/`DesignEditorPanel.tsx` → `ToolEvent.CODE_CONTENT`/`DESIGN_CONTENT`; engine `code_context_processor.py`/`design_context_processor.py` (30s debounce, diffing, Excalidraw→Mermaid) |
| **Agentic-coding assessment (the differentiator)**: in-interview AI copilot (chat + Cursor-style inline completions); every prompt/accept/reject/edit logged; 20k-token budget per session (HTTP 429 over budget); dedicated evaluation path | engine `ai_copilot_controller.py`, `ai_proxy_service.py`; models `ai_session.py`/`ai_interaction.py`; API `AiSession`/`AiInteraction`; eval `performAiAssistedEvaluation` → `competencyAssessment` |
| **Level-aware evaluation**: ENTRY/MID/SENIOR; weighted rubrics keyed by job level + question type | `EvaluationRubric`/`RubricCriteria`/`EvaluationCriteria`; `interviewAutoGenerationService.ts` |
| **Explainable, structured feedback**: technical + behavioral narrative, strengths/growth, per-criterion scores, verdict STRONG_HIRE→STRONG_NO_HIRE | `candidate-interview-evaluation` Lambda; `EvaluationFeedback(_StrengthGrowth)`, `EvaluationDetailedSummary` |
| **End-to-end employer hiring pipeline**: JobRack state machine SOURCING→ENHANCING→SCREENING→SHORTLISTING→CLOSED, Step Functions + SQS pollers | API `Jobrack.controller.ts`, `async/ingestion/*`, `screeningAssignment.service.ts` |
| **Semantic resume→JD matching**: Gemini skill extraction, profileMatchingScore, matched/missing skills | `matching-skill-score` Lambda (+ `skill2vec.csv`) |
| **Proctoring / anti-cheat**: MediaPipe gaze/face; keyboard/visibility/clipboard telemetry | UI `ProctorProvider.tsx`; API `ProctorEvents` |
| **Employer credit system**: packs, subscriptions, 1 credit/candidate-interview, full audit ledger | API `EmployerServicePack`/`EmployerCreditState`/`EmployerCreditAudit` |
| **Reliability engineering on the interviewer**: reconnection grace period; tested decision-policy guard so the AI won't abandon a candidate who goes quiet mid-problem | engine `interview_timer_monitor.py`; `tests/eval/` metrics `false_transition_rate`, `stuck_candidate_recall` |
| **Dual-audience product already in the UI**: candidate practice + employer hiring, with strong existing homepage copy | UI `src/utils/constants.ts` `HOME_HERO_COPY`, `HOME_AUDIENCE_CARDS` |
| **Curated content depth**: knowledge banks with hints, reference answers, per-language starter signatures (20+ languages) | `KnowledgeBank`, `QuestionCodeSignature`, `QuestionHints`, `QuestionAnswers` |

---

## 2. KB CLAIMS TO CORRECT (do not repeat these as written)

| KB says | Reality | Why it matters |
|---|---|---|
| "Voice AI: **Pipecat + Daily.co**"; "**Bedrock Claude** conducts interviews" | Interviewer brain is **Google Gemini 2.5 Flash**; STT **Deepgram**; TTS **local Kokoro-82M** (fallbacks Deepgram/ElevenLabs); transport Pipecat over **Daily/WebRTC**. **Bedrock Claude is the EVALUATOR, not the interviewer.** | A technical buyer / Show HN crowd will catch a wrong stack claim. Use the correct architecture. |
| Implies coding is run/tested ("check if code runs") | **No code execution sandbox** anywhere. Correctness is **LLM-judged** from written code + reference answers. | Never claim "runs your code / passes test cases." Claim "evaluates reasoning, approach, correctness of logic." |
| "104 Prisma models" | ~90 models + ~40 enums (~130 declared types). "100+ data models" is safe. | Minor; keep claims directionally honest. |
| ~~Copilot/agentic feature not fully shipped end-to-end~~ **(RESOLVED 2026-07-25: it IS demoable)** | **Fully shipped end-to-end**: backend + interview engine instrumented AND the candidate-facing agentic-coding round is live-demoable (founder-confirmed). | Feature it as the live-demo centerpiece. The #1 GTM wedge, see §4. No caveat needed. |
| "10,000+ interview questions (1,100 coding, 80 LLD, 50 HLD)" | Not verified against live DB counts in code; these are marketing figures. | Verify against production before using specific counts in sales assets. |
| Payments / metrics like "92% fraud detection", "45→12 days", "$555K/yr" | Payments = **Razorpay only** (confirmed). The stat figures are **sourced from third-party research/estimates**, not Roundz's own measured results. | Attribute them as industry research (they are), not as Roundz outcomes, until you have customer data. |

---

## 3. Honesty guardrails for all sales/marketing copy

1. **Don't claim code execution / test-case pass rates.** Say "assesses approach, complexity, and correctness of reasoning."
2. **Fraud/ROI stats are industry research**, not Roundz-measured outcomes, cite the source (Glider AI, Stripe, Officevibe, US DoL) or label "industry avg."
3. **Interviewer = Gemini, Evaluator = Claude/Bedrock, Matching = Gemini.** Get the stack right in technical content.
4. ~~Confirm the copilot candidate-UI is live before featuring it in a demo video.~~ **RESOLVED 2026-07-25: the agentic-coding round is live-demoable; feature it freely.**
5. **Verify question-bank counts** against prod before printing specific numbers.

---

## 4. The most under-exploited asset: the agentic-coding interview

The KB positions Roundz almost entirely as an **employer screening engine**. But the code shows a
**category-defining capability that competitors (HackerRank, Karat, CodeSignal, Final Round) do not have**:

- A workflow-step type `AI_ASSISTED_CODING` where the candidate is **given an AI copilot** and the
  task is to solve a problem *with* it.
- Full telemetry of **how they drive the AI**: prompt text, decomposition into sub-prompts, accept/reject/edit
  of suggestions, token efficiency (a hard 20k budget), latency, code-context deltas.
- A dedicated evaluation path scoring **prompt quality + problem decomposition + judgment**, not typing speed.

This directly matches the market shift the founder described: engineers now *direct agents* rather than
hand-write code, so the interview should measure **"can you get correct results out of AI tools"**.
This is a **"why now" wedge** and a PR/thought-leadership goldmine ("the first interview built for the
AI-native engineer"). It deserves to be a headline, not a footnote, pending the UI confirmation in §2.

---

## 5. Three-app architecture (accurate)

```
interview-networker-ui (Next.js 14)  ── candidate + employer + admin surfaces
   │  Pipecat client / Daily WebRTC ; Monaco ; Excalidraw ; MediaPipe proctoring
   ▼
mock-interview-api (Python FastAPI + Pipecat)  ── LIVE INTERVIEW ENGINE
   │  Deepgram STT → Gemini 2.5 Flash interviewer → Kokoro TTS ; Silero VAD + smart-turn
   │  AI copilot proxy (Gemini) ; transcript + code/design + AI-usage capture
   │  on completion → SQS → evaluation
   ▼
interview-networker-api (Node/Express + Prisma + Lambdas)  ── SYSTEM OF RECORD
      Postgres (Prisma) ; JobRack pipeline (Step Functions + SQS pollers)
      Lambdas: candidate-interview-evaluation (Bedrock Claude), feedback-consolidation
      (Bedrock Claude), matching-skill-score (Gemini), save-notification
      Razorpay billing ; S3 ; Google OAuth + JWT ; email (SMTP)
```
