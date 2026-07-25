# Roundz Knowledge Base

The single source of truth for Roundz go-to-market: product, market, sales, marketing, and investor materials.

**Roundz** is the AI interview engine for the AI-native era. It runs a company's real technical interview loop with a live voice AI interviewer, watches the candidate's live code and system-design whiteboard in real time, and includes a category-defining **agentic-coding round** that measures how well an engineer directs an AI copilot. It produces explainable, level-aware, rubric-scored reports so hiring teams meet only the pre-vetted top ~20% and always make the final call (the "80/20 human-in-the-loop" model).

---

## How this repo is organized

| Folder | What lives here | Primary audience |
|---|---|---|
| [`01-base-knowledge`](01-base-knowledge/) | What the product actually is. **Start with `Product_Ground_Truth.md` (code-verified).** | Everyone (read first) |
| [`02-market-research`](02-market-research/) | The problem, the market shift, sizing, competition, personas, regulation | Founders, investors, GTM |
| [`03-sales-pitch`](03-sales-pitch/) | The core sales narrative and pitch deck | Selling to employers |
| [`04-sales-toolkit`](04-sales-toolkit/) | Outreach, ICP, demo script, pricing, objections (the hands-on kit) | Whoever is selling |
| [`05-investor-pitch`](05-investor-pitch/) | Investor narrative and deck outline | Fundraising |
| [`06-marketing-and-launch`](06-marketing-and-launch/) | GTM/virality, ProductHunt, launch kit, UI/graphics | Marketing, launch |
| [`assets`](assets/) | Images, ProductHunt gallery, LinkedIn carousel | Design/launch |

---

## Suggested reading paths

- **New to Roundz:** `01-base-knowledge/Product_Ground_Truth.md` then `02-market-research/Market_Research_Deep_Dive.md`.
- **Going to sell:** `03-sales-pitch/Sales_Narrative_and_Deck.md` then the whole `04-sales-toolkit/`.
- **Raising money:** `05-investor-pitch/Investor_Narrative_and_Deck.md` (built on the market research).

---

## Honesty guardrails (apply to every document here)

These come from a full code review of all three Roundz codebases and are non-negotiable for external-facing use:

1. **No code-execution claims.** Roundz *evaluates approach, complexity, and correctness of reasoning*. It does not run test cases or compile code (there is no execution sandbox).
2. **Stats are industry research, not Roundz outcomes.** Cost/fraud/time figures come from third parties (US DoL/SHRM, Officevibe/LinkedIn, Stripe Developer Coefficient, Glider AI). Label them as such until we have our own pilot data.
3. **Get the stack right.** Interviewer brain = Google Gemini 2.5 Flash; evaluator = AWS Bedrock (Claude); resume matching = Gemini; STT = Deepgram; TTS = Kokoro; billing = Razorpay (credit model).
4. **No fabricated proof.** No invented logos, customers, testimonials, revenue, or traction. Use clearly marked placeholders.
5. **Human-in-the-loop, always.** Roundz filters; the customer decides.

Documents created before the July 2026 code review carry a **LEGACY** banner. Trust `Product_Ground_Truth.md` over any legacy claim.

## Status
- The product is built; the **agentic-coding round is live-demoable** (confirmed 2026-07-25).
- Stage: early GTM (founder-led). The open proof gap is customer/pilot data, which will replace the industry-research stats over time.

## Contributing
Keep the honesty guardrails. Do not use em-dashes in any document (use colons, commas, or parentheses). New documents should follow the naming and structure conventions of their folder.
