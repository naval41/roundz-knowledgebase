> ⚠️ **LEGACY DOCUMENT (pre-2026-07 code review).** This file predates the code-verified `01-base-knowledge/Product_Ground_Truth.md`. It may contain claims flagged as inaccurate (for example: interviewer stack, unverified stats, "runs your code"). **Verify any claim against `Product_Ground_Truth.md` before using it externally.** Kept for historical/context value.

# Roundz.ai — Complete Knowledge Base

> Single-source-of-truth document covering product understanding, system architecture, Product Hunt launch strategy, UI/graphics plan, and go-to-market playbook.
>
> Last updated: 2026-04-30

---

# PART 1: PRODUCT UNDERSTANDING

## 1.1 Product Identity

| Field | Value |
|-------|-------|
| **Product Name** | Roundz.ai |
| **Tagline** | AI-Powered Technical Hiring Engine |
| **URL** | https://roundz.ai |
| **Employer Portal** | https://roundz.ai/employer |
| **Category** | B2B SaaS — HR Tech / AI Hiring |
| **Primary Buyer** | CTOs, VPs of Engineering at Series A–C startups (50–250 employees) |
| **Secondary User** | Software engineering candidates preparing for interviews |
| **Core Promise** | Screen 10x more candidates, spend 80% less engineering time on interviews |
| **Positioning** | "An engineering filter, not an HR tool" |

## 1.2 What Roundz Does

Roundz automates the end-to-end technical hiring pipeline:

1. **Enterprises post job roles** based on hiring needs
2. **AI enriches** the job description with semantic skill taxonomy
3. **Candidates apply** — AI matches resumes to roles using vector embeddings (not keywords)
4. **Top matches are shortlisted** based on AI-generated match scores
5. **AI Voice Agents conduct interviews** — DSA, System Design, LLD, HLD, Behavioral — 24/7
6. **AI evaluates performance** with explainable reasoning: strengths, growth areas, hire/no-hire verdict
7. **Only top 20%** of pre-vetted candidates reach the hiring manager

This is the **80/20 Model** — AI handles 80% of screening, humans handle 20% (the final decision).

Additionally, candidates can use Roundz independently for **mock interview preparation** with the same AI voice agents, paying per session.

## 1.3 Problems Solved

| Problem | Impact | How Roundz Solves It |
|---------|--------|---------------------|
| **Engineering bandwidth waste** | 5 out of 6 candidates pass screening but fail live interviews — CTOs spend 33% of time interviewing | AI conducts all technical rounds; CTO only sees pre-vetted top 20% |
| **Slow hiring cycles** | Average 45 days to hire; top candidates gone in 10 days | Reduces to 12 days — AI screens 24/7, no scheduling bottleneck |
| **Resume-based evaluation** | Keyword matching misses real talent; cheating tools inflate scores | Voice AI tests real reasoning in real-time; 92% fraud detection |
| **Bad hires** | One bad hire costs $90K+ in wasted roadmap, morale damage, re-hiring | Multi-round AI evaluation with standardized rubric catches false positives |
| **Bottleneck hiring manager** | CTO has two full-time jobs (ship product + hire people) | AI removes the screening burden; CTO focuses on building |

## 1.4 The Financial Case

| Cost Category | Annual Impact | Source |
|--------------|--------------|--------|
| Bad Hire Tax | $90,000+ per bad hire | US Dept of Labor |
| Vacancy Tax | $24,000/month per unfilled seat | Officevibe |
| CTO Time Tax | $225,000/yr (33% of bandwidth on screening) | Stripe Developer Coefficient |
| **Total Annual Loss** | **$555,000+** | Combined |
| Candidate Fraud Rate | 23% of unproctored candidates attempt to cheat | Glider AI |

## 1.5 Core Value Propositions

1. **10x Faster Screening** — AI voice agents conduct full technical interviews 24/7
2. **80% Less CTO Time** — engineering leaders only see the top 20% of pre-vetted candidates
3. **92% Fraud Detection** — real-time proctoring catches AI-assisted cheating, tab-switching, proxy interviewers
4. **$555K/yr Savings** — eliminates the compounding cost of bad hires, vacancy, and leadership time waste
5. **Explainable AI** — every score has transparent reasoning, no black-box decisions
6. **Human-in-the-Loop** — AI augments, never replaces; final hiring decision stays with your team

## 1.6 Ideal Customer Profile (ICP)

| Dimension | Profile |
|-----------|---------|
| **Stage** | Post-Series A to Pre-Series C ($5M–$20M ARR) |
| **Headcount** | 50–200 employees; engineering > 40% of headcount |
| **Verticals** | B2B SaaS, FinTech, AI Infrastructure |
| **Geo** | US/EU (high-cost labor) or remote-first (highest cheating risk) |
| **Trigger** | Just closed funding with mandate to double engineering team in 6 months; missed product milestones due to resource constraints |
| **Buyer** | CTO / VP of Engineering (not HR) |
| **Psychographics** | Overwhelmed, spend >30% of week on non-coding tasks, skeptical of black-box AI but desperate for time |

## 1.7 Competitive Positioning

| Competitor | Their Approach | Roundz Advantage |
|-----------|---------------|-----------------|
| **HackerRank / LeetCode** | Static coding tests that check output | Voice AI tests reasoning and communication; catches cheaters; senior-friendly |
| **Manual screening** | CTO/lead reviews every candidate | 24/7, 10x throughput, standardized rubric, no interviewer fatigue |
| **Recruitment agencies** | Pay 20-25% of salary per placement | No commission; higher signal-to-noise; faster |
| **ATS (Greenhouse/Lever/Ashby)** | Stores and organizes resumes | Evaluates, not just stores; semantic matching, not keyword matching |
| **Adding more recruiters** | Throw bodies at the problem | Solves the technical bottleneck, not just the volume problem |
| **PluralAI / Final Round AI** | AI-powered assessments | Full voice conversations (not text); complete hiring loop (not just screening); anti-cheat proctoring |

---

# PART 2: SYSTEM ARCHITECTURE (CODE-BACKED)

## 2.1 Tech Stack

| Layer | Technology | Codebase Path |
|-------|-----------|--------------|
| **Frontend** | Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS | `interview-networker-ui/src/` |
| **State Mgmt** | Zustand (client), TanStack React Query (server state) | `ui/src/stores/`, `ui/src/hooks/` |
| **Backend** | Node.js, Express, TypeScript | `interview-networker-api/src/` |
| **Database** | PostgreSQL via Prisma ORM (104 models) | `api/prisma/schema.prisma` |
| **AI Evaluation** | AWS Bedrock (Claude) | `api/src/utils/bedrock.ts` |
| **Skill Extraction** | Google Gemini API | `api/lambda/lambdas/matching-skill-score/` |
| **Voice AI** | Pipecat AI + Daily.co WebRTC | `ui/src/components/interview-session/` |
| **Code Editor** | Monaco Editor (50+ languages) | `ui/src/components/interview-session/panels/CodeEditorPanel.tsx` |
| **Design Tool** | Excalidraw whiteboard | `ui/src/components/interview-session/panels/DesignEditorPanel.tsx` |
| **Proctoring** | MediaPipe Vision (face/gaze) | `ui/src/components/interview-session/ProctorProvider.tsx` |
| **Payments** | Razorpay (UPI, cards, netbanking) | `ui/src/components/payment-checkout/` |
| **File Storage** | AWS S3 (resumes, logos) | `api/src/utils/s3.ts` |
| **Async Processing** | AWS SQS + Lambda + Step Functions | `api/src/async/`, `api/lambda/` |
| **Email** | Nodemailer + HTML templates | `api/src/utils/email.ts`, `api/src/templates/` |
| **Monitoring** | CloudWatch + Pino logger | `api/src/middlewares/cloudwatch.middleware.ts` |
| **Auth** | JWT (access 15min + refresh 7d) + Google OAuth2 | `api/src/middlewares/auth.middleware.ts` |
| **Feature Flags** | Custom per-user flags | `api/src/controllers/`, `ui/src/providers/featureFlagProvider.tsx` |

## 2.2 High-Level Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                       FRONTEND (Next.js 14)                       │
│  Candidate Portal  │  Employer Portal  │  Admin Portal           │
│  406+ components   │  33 hooks         │  32 services            │
└──────────┬────────────────┬────────────────┬─────────────────────┘
           │                │                │
     publicAxios     privateAxios    interviewAxios
     (no auth)       (JWT bearer)    (interview server)
           │                │                │
           └────────────────┼────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────────┐
│                     BACKEND (Express API)                         │
│  35+ route files  │  30+ controllers  │  Auth/Role middleware    │
└──────────┬────────────────┬────────────────┬─────────────────────┘
           │                │                │
           ▼                ▼                ▼
┌──────────────┐  ┌─────────────────┐  ┌───────────────────────┐
│  PostgreSQL  │  │  SQS Queues (4) │  │  External Services    │
│  (Prisma)    │  │  + Pollers      │  │  - Razorpay           │
│  104 models  │  │                 │  │  - S3                 │
└──────────────┘  └────────┬────────┘  │  - Google OAuth       │
                           │           └───────────────────────┘
                           ▼
┌──────────────────────────────────────────────────────────────────┐
│                     LAMBDA FUNCTIONS                              │
│  candidate-interview-evaluation  (Bedrock Claude)                │
│  matching-skill-score            (Gemini API)                    │
│  feedback-consolidation          (Bedrock Claude)                │
│  save-notification               (DB persistence)                │
└──────────────────────────────────────────────────────────────────┘
```

## 2.3 User Roles & Routes

### Candidate Portal
| Route | Feature |
|-------|---------|
| `/` | Landing page — hero, features, testimonials |
| `/login`, `/signup` | Email/password + Google OAuth |
| `/mock-interview` | Browse & purchase AI mock interviews |
| `/interview-session/[roomId]` | Live AI voice interview (code editor + whiteboard) |
| `/jobs` | Browse open positions, apply with resume |
| `/interviews`, `/groups` | Community — share experiences, join groups |
| `/profile` | Education, experience, projects, skills |
| `/pricing` | 3 tiers: DSA (free trial), LLD ($15), HLD ($15) |
| `/dashboard` | Analytics & user stats |
| `/blog` | Articles & resources |

### Employer Portal
| Route | Feature |
|-------|---------|
| `/employer` | Marketing landing page |
| `/employer/home` | Dashboard — pipeline overview, hiring metrics |
| `/employer/jobs` | Create/edit job postings with AI skill enrichment |
| `/employer/candidates` | View applicants, skill match scores, screening status |
| `/employer/loops` | Configure multi-round interview workflows |
| `/employer/interviews` | View AI-conducted interview results + evaluation artifacts |
| `/employer/pricing` | Purchase credit packages |
| `/employer/credit-audit` | Credit usage history & billing |
| `/employer/notifications` | Application & screening alerts |

### Admin Portal
| Route | Feature |
|-------|---------|
| `/manage` | Feature flags, user management, blog, email, workflows |

## 2.4 The 80/20 Hiring Pipeline (Step-by-Step)

```
Step 1: Create Job Description (Recruiter)
├── Recruiter defines role, requirements, evaluation criteria
├── JobRack created in DB (status: SOURCING)
└── Code: POST /api/employer/jobrack

Step 2: AI Enhances Skills (AI)
├── Roundz analyzes JD, enriches skill taxonomy
├── Lambda triggers via ENRICHING_SKILLS_QUEUE
├── Status transitions: SOURCING → ENHANCING
└── Code: EnrichingSkillsPoller → api/src/async/ingestion/

Step 3: Invite Candidates (Recruiter)
├── Public link or direct invitations shared
├── Candidates apply with resume
├── CandidateJobRackInfo records created (status: SOURCED)
└── Code: POST /jobdescription/submit

Step 4: Resume Validation & Matching (AI)
├── Lambda (matching-skill-score) extracts skills via Gemini API
├── Parses PDF/DOCX from S3
├── Compares extracted skills against enhanced job requirements
├── Assigns profileMatchingScore (0-100)
├── Status: SOURCED → SCREENING_SHORTLIST if score > threshold
└── Code: lambda/lambdas/matching-skill-score/

Step 5: Smart Shortlisting (Recruiter)
├── Recruiter reviews AI scores and candidate profiles
├── Shortlists top matches based on score + manual judgment
└── ~40 of 100 candidates shortlisted typically

Step 6: AI Voice Screening — 24/7 (AI)
├── Interview loop assigned (combination of DSA, LLD, HLD, Behavioral)
├── ScreeningPoller auto-creates CandidateInterview for each round
├── 1 employer credit deducted per candidate per screening
├── Pipecat AI Voice Agent conducts each round via Daily.co WebRTC
├── Proctoring active: face detection, gaze tracking, keyboard monitoring
├── Transcripts recorded per session
├── Invite emails sent to candidates
└── Code: api/src/async/ingestion/screening-poller.ts

Step 7: LLM Evaluates Results (AI)
├── Lambda (candidate-interview-evaluation) processes transcripts
├── Bedrock Claude evaluates per WorkflowStep
├── Multi-dimensional: technical skills, behavioral traits, communication
├── Uses tool_use for structured evaluation output
└── Code: lambda/lambdas/candidate-interview-evaluation/

Step 8: Evaluation Artifacts Generated (AI)
├── Per-round: strengths, growth areas, detailed rubric scores
├── Lambda (feedback-consolidation) aggregates across all rounds
├── Final verdict: STRONG_HIRE / HIRE / LEANING_HIRE / NO_HIRE / STRONG_NO_HIRE
├── Saved to EvaluationFeedback + EvaluationDetailedSummary
├── Email sent to employer with results
└── Code: lambda/lambdas/feedback-consolidation/

Step 9: Final Human Decision (Your Team)
├── Top 20% (~20 candidates) presented in employer dashboard
├── Full evaluation reports with explainable AI reasoning
├── Hiring manager reviews and makes final call
└── Code: GET /api/employer/candidates + GET /api/consolidated-feedback/
```

## 2.5 Candidate Mock Interview Flow

```
1. Browse → /mock-interview (select DSA, LLD, or HLD)
2. Payment → Razorpay checkout ($0 for free trial, $10-$15 for paid)
3. CandidateInterview created (PENDING)
4. Enter room → /interview-session/[roomId]
5. Daily.co WebRTC connection established
6. Pipecat AI voice agent begins conversation
7. Candidate uses:
   - Voice for discussion + follow-up answers
   - Monaco Editor for live coding (DSA/LLD)
   - Excalidraw whiteboard for system design (HLD)
8. Proctoring active:
   - Face detection (FACE_NOT_FOUND, MULTIPLE_FACES)
   - Gaze tracking (LOOKING_AWAY, SUSPICIOUS_EYE_MOVEMENT)
   - Keyboard/clipboard monitoring
   - Events logged to ProctorEvents table
9. Interview completes → status: REVIEW_IN_PROGRESS
10. Lambda evaluates transcript via Bedrock Claude
11. Structured feedback: technical + behavioral assessment
12. Email sent with detailed report → status: COMPLETED
```

## 2.6 Interview Types

| Type | DB Code | Duration | Tools Available | What's Evaluated |
|------|---------|----------|----------------|-----------------|
| Data Structures & Algorithms | CODING | 60 min | Voice + Monaco Editor | Problem solving, time/space complexity, code quality, think-aloud |
| Low-Level Design | LLD | 60 min | Voice + Monaco Editor | OOP, SOLID, design patterns, code extensibility, maintainability |
| High-Level Design | SYSTEM_DESIGN | 60 min | Voice + Excalidraw | Architecture, scalability, failure handling, trade-offs, component design |
| Behavioral | BEHAVIORAL | Varies | Voice only | Communication, leadership, conflict resolution, culture fit |

## 2.7 Key Database Domains (104 Prisma Models)

| Domain | Key Models | State Machines |
|--------|-----------|---------------|
| **Users** | User, UserProfile, Education, Experience, Project, Client | Roles: USER, EMPLOYER, ADMIN |
| **Job Pipeline** | JobRack, JobProfile, JobRole, CandidateJobRackInfo | SOURCING → ENHANCING → SCREENING → SHORTLISTING → CLOSED |
| **Interviews** | MockInterview, CandidateInterview, SessionDetails, Transcript | PENDING → IN_PROGRESS → REVIEW_IN_PROGRESS → COMPLETED |
| **Workflows** | Workflow, WorkflowStep, CandidateInterviewPlanner | Steps: INTRO, CODING, SYSTEM_DESIGN, BEHAVIORAL, QNA, WRAP_UP |
| **Evaluation** | EvaluationFeedback, EvaluationFeedback_StrengthGrowth, EvaluationDetailedSummary | Verdicts: STRONG_HIRE → STRONG_NO_HIRE |
| **Knowledge** | KnowledgeBank, InterviewQuestion, QuestionCodeSignature, QuestionHints, QuestionAnswers | 10,000+ questions: 1,100+ coding, 80+ LLD, 50+ HLD |
| **Loops** | Loop, LoopMapping, CandidateLoopEntry | Maps interview rounds to job screening |
| **Candidate Commerce** | Service, Order, OrderLine, Payment, Invoice, FreeTrialUsage | Free trial abuse detection via IP/user-agent |
| **Employer Billing** | EmployerService, EmployerServicePack, EmployerOrder, EmployerSubscription, EmployerCreditState, EmployerCreditAudit | Tiers: Starter, Growth, CustomPack, Small, Medium, Large |
| **Proctoring** | ProctorEvents | Types: KEYBOARD, VISIBILITY, GAZEOFFSCREEN |
| **Community** | CommunityGroup, GroupMembership, GroupPost, GroupPostComment, GroupPostVote | Post types: TEXT, LINK, IMAGE, VIDEO, POLL, INTERVIEW_SHARE, JOB_SHARE |
| **System** | Achievement, FeatureFlag, FeatureFlagAssignment, Notification, Blog, WaitList | Achievement types: CONTRIBUTION, ENGAGEMENT, MILESTONE, SPECIAL, COMMUNITY |

## 2.8 API Endpoints (35+ Route Files)

| Domain | Key Endpoints | Auth Required |
|--------|--------------|---------------|
| **Auth** | `POST /api/auth/register, /login, /google, /refresh-token, /forgot-password, /reset-password, /logout` | Public |
| **Users** | `GET/PUT /api/user/profile, POST /api/user/education, /experience, /project` | JWT |
| **Mock Interviews** | `POST /api/mock-interviews/start-interview, GET /my-interviews, /interview/:id, /question/:id, POST /proctor-event` | JWT |
| **Evaluation** | `GET /api/evaluation-feedback/:id, GET /api/consolidated-feedback/:id` | JWT |
| **Employer Jobs** | `CRUD /api/employer/jobrack, GET /:id/candidates, POST /:id/enrich` | JWT + Employer |
| **Employer Loops** | `CRUD /api/employer/loops, POST /:id/start-screening` | JWT + Employer |
| **Employer Billing** | `GET /api/employer/services, POST /orders, POST /orders/:id/verify-payment, GET /credit-state, /credit-audit` | JWT + Employer |
| **Candidate Orders** | `POST /api/orders/create, POST /verify-payment, GET /invoice` | JWT |
| **Community** | `CRUD /api/groups, /posts, POST /comments, /upvote, /downvote` | JWT |
| **Interviews (Community)** | `CRUD /api/interviews, POST /comments, /upvote, /downvote` | JWT |
| **Admin** | `GET /api/admin/users, /companies, CRUD /feature-flags, POST /notifications` | JWT + Admin |

## 2.9 Async Processing Architecture

```
PollerManager (starts on server boot — api/src/async/poller-manager.ts)
│
├── EnrichingSkillsPoller (ENRICHING_SKILLS_QUEUE_URL)
│   └── AI enriches job description skill taxonomy
│
├── CandidateSourcingPoller (CANDIDATE_SOURCING_QUEUE_URL)
│   └── Triggers Lambda: resume parsing → skill extraction (Gemini) → match scoring
│
├── ScreeningPoller (SCREENING_QUEUE_URL)
│   ├── Fetches JobRack + shortlisted candidates
│   ├── Creates CandidateInterview per round
│   ├── Deducts employer credits
│   ├── Sends invite emails
│   └── Uses StepFunction taskTokens for orchestration
│
└── EvaluationPoller (EVALUATION_QUEUE_URL)
    └── Triggers Lambda: transcript evaluation via Bedrock Claude
```

### Lambda Functions

| Function | Trigger | AI Used | Output |
|----------|---------|---------|--------|
| **candidate-interview-evaluation** | EVALUATION_QUEUE | Bedrock Claude | EvaluationFeedback + detailed rubric scores per WorkflowStep |
| **matching-skill-score** | CANDIDATE_SOURCING_QUEUE | Gemini API | profileMatchingScore (0-100) + matchingSkills array |
| **feedback-consolidation** | CONSOLIDATE_FEEDBACK_QUEUE | Bedrock Claude | Aggregated hire/no-hire recommendation across all interview rounds |
| **save-notification** | NOTIFICATION_QUEUE | None | Persists notifications to DB, optionally sends email/SMS |

## 2.10 Security & Multi-Tenancy

| Feature | Implementation |
|---------|---------------|
| **Multi-Tenancy** | `clientId` on User/Client; all employer queries scoped to clientId; admin bypasses scoping |
| **Authentication** | JWT access token (15 min TTL) + refresh token (7 day, HTTP-only cookie); auto-refresh via Axios interceptors; cross-tab sync via BroadcastChannel API |
| **Authorization** | authMiddleware → adminMiddleware / employerMiddleware; roles: USER, EMPLOYER, ADMIN |
| **Passwords** | bcryptjs with salt |
| **Proctoring** | MediaPipe face detection, gaze tracking, keyboard monitoring; violations: FACE_NOT_FOUND, MULTIPLE_FACES, LOOKING_AWAY, MOBILE_USAGE, SUSPICIOUS_EYE_MOVEMENT |
| **Content Moderation** | leo-profanity filter on interview submissions |
| **Free Trial Abuse** | IP/user-agent tracking per FreeTrialUsage record; blacklist mechanism |
| **Credit Controls** | Deduct before interview start (soft limit prevents overspend); EmployerCreditAudit logs every transaction |
| **Feature Flags** | Per-user FeatureFlagAssignment for gradual rollout and A/B testing |
| **Domain Restrictions** | Employer signup blocks personal email domains |

## 2.11 Frontend Component Architecture

| Area | Component Count | Key Technologies |
|------|----------------|-----------------|
| **Interview Session** | 30+ components | Pipecat AI, Daily.co WebRTC, Monaco Editor, Excalidraw, MediaPipe, WebGL audio visualizers |
| **Employer Portal** | 50+ components | Job wizard, candidate pipeline, loop management, credit dashboard |
| **Payment** | 10+ components | Razorpay integration, free trial handling, invoice display |
| **Community** | 20+ components | Groups, posts, comments, voting |
| **Auth** | 10+ components | Login, signup, OAuth, email verification, password reset |
| **Shared/UI** | 100+ components | Radix UI primitives, Tailwind-styled, Framer Motion animations |

### Key Custom Hooks (33 total)
`useApiQuery`, `useApiMutation`, `useUser`, `useConversation`, `useDebounce`, `useFeatureFlag`, `usePayment`, `useKeyboardViolation`, `useClipboardViolation`, `useGuestLimit`, `useInfiniteList`, `usePersistentTempState`

## 2.12 Employer Credit System

```
Employer purchases a service package (Starter / Growth / CustomPack / etc.)
    ↓
EmployerOrder created → Razorpay payment verified
    ↓
EmployerSubscription activated with validity period
    ↓
EmployerCreditState initialized: { total, remaining, used }
    ↓
On each AI screening:
    1 credit deducted (source: AI_SCREENING)
    EmployerCreditAudit log entry created
    ↓
Dashboard: /employer/credit-audit shows full transaction history
```

## 2.13 Landing Page Structure (roundz.ai/employer)

The employer landing page uses a dark theme with cyan/blue accents and consists of these sections:

| # | Section | Content |
|---|---------|---------|
| 1 | **Hero** | Rotating headlines ("Stop losing top talent to slow processes" / "Stop wasting $555K/year on broken hiring" / "Stop burning out your engineering team" / "Stop screening candidates all day") + CTAs: Book a Demo, See How It Works |
| 2 | **Stats Bar** | 10x Faster Screening · 80% Less CTO Time · 92% Fraud Detection |
| 3 | **Platform Stats** | 10,000+ Interview Questions · 45 min Deep Screening · 24/7 Global Availability |
| 4 | **Hidden Cost of Manual Hiring** | 4 cost cards: Bad Hire Tax ($90K+), Vacancy Tax ($24K/mo), CTO Time Tax ($225K/yr), Total ($555K+) |
| 5 | **Before/After Comparison** | "From Hiring Chaos to Hiring Clarity" — 7 metrics with before/after values |
| 6 | **9-Step Workflow** | "From 100 Applicants to Top 20%" — visual pipeline: JD → AI Enrich → Apply → Match → Shortlist → AI Interview → Evaluate → Artifacts → Human Decision |
| 7 | **Evaluation Sample** | "What You Get for Every Candidate" — Strengths, Growth Areas, Hire Reason, No-Hire Reason, Final Verdict |
| 8 | **Feature Grid** | 6 features: Voice AI That Tests Reasoning, Multi-Round Coverage, Anti-Cheat Technology, Explainable AI Reports, Semantic Skill Matching, 24/7 Global Screening |
| 9 | **Trust Section** | "Built for Enterprise Trust" — Human-in-the-Loop, Enterprise-Grade Privacy (SOC 2), Full Transparency, Better Candidate Experience |
| 10 | **FAQ** | 8 questions: Will AI replace hiring team? Anti-cheat? Interview types? Accuracy? Candidate experience? Setup time? vs HackerRank? Company size? |
| 11 | **Final CTA** | "Ready to Fix Your Hiring Funnel?" + Book a Demo, See Pricing. "No credit card required. Screen your first candidate within 24 hours." |

## 2.14 Candidate Pricing

| Plan | Price | Duration | Key Features |
|------|-------|----------|-------------|
| **DSA** | 1 free trial, then $10 | 60 min | Live coding, think-aloud, seniority-based difficulty, follow-up questions |
| **Low-Level Design** | $15 (was $20) | 60 min | OOP/SOLID, design patterns, class design, code extensibility review |
| **High-Level Design** | $15 (was $20) | 60 min | Interactive design playground (Excalidraw), architecture scoring, scalability analysis |

Payment via Razorpay: UPI (Google Pay, PhonePe, Paytm), Netbanking, RuPay, credit/debit cards. Prices in USD, auto-converted to INR at checkout.

## 2.15 Key Metrics & Claims

- 10,000+ interview questions (1,100+ coding, 80+ LLD, 50+ HLD)
- 45-minute deep screening sessions
- 24/7 global availability across all time zones
- Time-to-hire: 45 days → 12 days (73% reduction)
- Top candidate drop-off: 60% → under 15% (4x improvement)
- CTO involvement: every screen → final round only (80% reduction)
- Screening time: 40+ hrs/week → 4 hrs/week (10x reduction)

---

# PART 3: PRODUCT HUNT LAUNCH STRATEGY

## 3.1 How Product Hunt Works

Products launch at **12:01 AM PT** and compete for upvotes until midnight. The ranking algorithm weighs:

1. **Unique upvotes from real accounts** — aged accounts with history weigh more than new ones
2. **Comment quality and quantity** — genuine discussions rank higher than "Great product!"
3. **Engagement velocity** — steady stream throughout the day beats a spike-then-drop
4. **Hunter reputation** — well-known hunters give more initial visibility
5. **Account authenticity** — PH penalizes vote manipulation and burner accounts

Top products earn **Product of the Day** badge → drives signups, press, investor attention, SEO backlinks, and lasting social proof.

## 3.2 Pre-Launch Checklist (4-6 Weeks Before)

### Week 1-2: Foundation
- [ ] Create maker account on Product Hunt
- [ ] Follow 200+ relevant makers in HR-tech, AI, developer tools
- [ ] Comment genuinely on 3-5 products daily to build account credibility
- [ ] Identify and contact a **top Hunter** (1000+ followers, hunts AI/HR-tech products)
- [ ] Prepare all assets (see Section 3.4)
- [ ] Set up "Coming Soon" page on PH to collect followers

### Week 2-3: Community Building
- [ ] Build launch list of 300+ supporters (team, advisors, investors, beta users, tech community)
- [ ] Start teasing on social media (behind-the-scenes, problem stats, interview clips)
- [ ] Share the $555K stat, the 5-out-of-6 stat, anti-cheating insights

### Week 3-4: Content & Outreach
- [ ] Write supporting blog posts:
  - "Why We Built an AI Interviewer" (founder story)
  - "The $555K Hidden Cost of Manual Hiring" (data-driven)
  - "How AI Voice Agents Are Replacing HackerRank" (thought leadership)
  - "92% of Cheaters Caught" (technical deep-dive)
- [ ] Prepare social media posts for launch day (X, LinkedIn, Reddit, HN)
- [ ] Draft personalized DMs for launch list
- [ ] Pitch tech journalists: TechCrunch, VentureBeat, Hacker News
- [ ] Pitch newsletters: HR Brew, People Managing People, Dev.to, Hashnode

## 3.3 Launch Day Hour-by-Hour Plan

**Best day:** Tuesday, Wednesday, or Thursday. Launch at 12:01 AM PT sharp.

| Time (PT) | IST | Actions |
|-----------|-----|---------|
| 12:00 AM | 12:30 PM | Go live. Post Maker's Comment immediately. Notify team. |
| 12:00-6:00 AM | 12:30-6:30 PM | Wave 1: Personal DMs to strongest supporters (India timezone advantage). Post on X/Twitter. |
| 6:00-9:00 AM | 6:30-9:30 PM | Wave 2: US contacts wake up. LinkedIn founder story post. Reply to every PH comment within 10 min. |
| 9:00 AM-12:00 PM | 9:30 PM-12:30 AM | Peak PH traffic. Show HN post. Email blast. Reddit (r/startups, r/recruitinghell). |
| 12:00-6:00 PM | 12:30-6:30 AM | Sustain: Second LinkedIn post (different angle). Dev.to/Hashnode. Wave 3 DMs. |
| 6:00-11:59 PM | 6:30 AM-12:30 PM | Final push. Thank supporters. Share ranking screenshots on social. |

### Critical Rules
1. **NEVER ask for upvotes** — say "would love your feedback" or "check it out"
2. **NEVER send PH direct links in mass emails** — PH detects referral patterns
3. **Reply to every comment** — engagement rate directly impacts ranking
4. **Keep comments substantive** — "Great product!" from new accounts hurts you
5. **Never buy votes** — PH fraud detection is sophisticated; you get banned

## 3.4 Product Hunt Listing Assets

### Required Assets
| Asset | Spec | Status |
|-------|------|--------|
| **Logo** | 240x240px, clear on light background | Needed |
| **Tagline** | Under 60 characters | Ready (see options below) |
| **Gallery images** | 1270x760px, 6-8 images | 5 created (see `assets/producthunt-gallery/`) |
| **Product video** | 1920x1080, 1-2 minutes | Needed — script ready (see Section 3.6) |
| **Description** | See below | Ready |
| **Maker's comment** | See below | Ready |

### Tagline Options
- **A:** "AI voice agents that screen engineers 10x faster"
- **B:** "Stop losing top talent to slow hiring — AI interviews 24/7"
- **C:** "Your AI hiring engine: from 100 applicants to top 20% automatically"

### Description (for PH listing)
```
Roundz is an AI-powered hiring engine that handles 80% of technical screening
so your engineering team can focus on building product, not interviewing.

HOW IT WORKS:
1. Post a job → AI enriches skill requirements
2. Candidates apply → AI matches resumes to role (semantic, not keyword)
3. Top matches get AI voice interviews — DSA, System Design, LLD, Behavioral
4. AI generates detailed evaluation: strengths, growth areas, hire/no-hire verdict
5. Your team only sees the top 20% of pre-vetted candidates

WHY TEAMS SWITCH:
→ 10x faster screening (45 days → 12 days time-to-hire)
→ 80% less CTO interview time
→ 92% fraud detection (catches AI-assisted cheating in real-time)
→ 24/7 global availability — screen across every time zone
→ Explainable AI — every score has transparent reasoning

The average Series A-C startup loses $555K/year to broken hiring.
Roundz gives your engineering leaders their time back.

Free demo available — screen your first candidate within 24 hours.
```

### Maker's First Comment (post immediately at launch)
```
Hey PH! I'm [Name], founder of Roundz.

We built Roundz because we lived the pain ourselves. As engineers, we spent
30%+ of our time interviewing candidates — and 5 out of 6 who passed the
initial HackerRank screen would fail the live interview anyway.

The breaking point? When our CTO spent an entire Sunday screening resumes
instead of shipping features for a board deadline.

So we built what we wished existed: an AI voice agent that conducts real
technical interviews — not just coding tests, but actual conversations that
test how candidates think, communicate, and reason through problems.

What makes Roundz different from HackerRank/Codility:
- Voice AI that asks follow-up questions like a senior engineer
- Covers DSA + System Design + LLD + Behavioral in one platform
- Anti-cheat: catches AI-assisted cheating with 92% accuracy
- Explainable: every score shows WHY, not just a number

We're offering the PH community a free demo — screen your first
candidate within 24 hours. Would love your honest feedback!

What's the worst part of your current hiring process? Curious to hear
from other engineering leaders here.
```

## 3.5 Gallery Images (Created)

Five 1270x760px images saved in `assets/producthunt-gallery/` — PNGs + editable HTML source files:

| # | File | Content |
|---|------|---------|
| 1 | `01_Hero_Main.png` | Main hero — "Screen Engineers 10x Faster with Voice AI Agents" + 3 stats + 80/20 funnel card |
| 2 | `02_Hidden_Cost.png` | "$555K/yr Hidden Cost of Manual Hiring" — 4 cost cards with dollar amounts |
| 3 | `03_Before_After.png` | "From Hiring Chaos to Hiring Clarity" — 7-metric comparison table with improvement badges |
| 4 | `04_Evaluation_Features.png` | "Every Decision Fully Explainable" — sample evaluation report (HIRE) + 6 feature cards |
| 5 | `05_Live_Interview.png` | AI interview simulation — voice transcript + code editor side by side |

**Recommended additions:**
- Image 6: Animated GIF showing the AI voice interview workflow
- Image 7: Customer testimonial / social proof slide
- Image 8: "How to get started in 24 hours" onboarding slide

## 3.6 Product Video Script (1-2 Minutes)

| Time | Scene | Content |
|------|-------|---------|
| 0:00-0:15 | **Hook** | "Your CTO spent 33% of last quarter interviewing candidates. 5 out of 6 failed the live round anyway. That's $555K a year in broken hiring." |
| 0:15-0:30 | **Promise** | "Roundz is an AI hiring engine. Voice AI agents that conduct real technical interviews — not just coding tests." |
| 0:30-1:00 | **Demo** | Screen recording: employer creates job → AI enriches skills → candidates apply → resume matching scores appear → AI voice interview in action (waveform, follow-ups, code editor) → evaluation report |
| 1:00-1:20 | **Results** | "Teams using Roundz screen 10x more candidates in 80% less time. Time-to-hire drops from 45 days to 12." |
| 1:20-1:40 | **Trust** | "92% fraud detection. Explainable AI. Human-in-the-loop — you always make the final call." |
| 1:40-2:00 | **CTA** | "Screen your first candidate within 24 hours. No credit card required. Try Roundz free." |

Production notes: Use real screen recordings (not mockups). Voiceover should be confident and technical. PH community values authenticity over polish.

## 3.7 Common Mistakes to Avoid

| Mistake | Consequence |
|---------|------------|
| Launching on Monday/Friday | Low traffic |
| Mass email with direct PH link | PH detects patterns, demotes you |
| Asking for "upvotes" | Against TOS, community flags it |
| Not replying to comments | Kills engagement score |
| Generic gallery images | First image determines click-through |
| No product video | Video products get 2-3x engagement |
| No pre-built audience | Day-of outreach alone rarely wins PotD |
| Only new PH accounts supporting | Votes from new accounts heavily discounted |
| Launching incomplete product | PH community is brutally honest |
| Generic tagline ("AI hiring tool") | Blends in with 100 others |

## 3.8 Post-Launch (Days 2-30)

### Days 2-7
- [ ] "Thank you" post on X/LinkedIn with results and ranking
- [ ] Email all PH upvoters with onboarding offer
- [ ] Publish "lessons learned" blog post (meta-content gets shared widely)
- [ ] Follow up with every commenter who asked a question
- [ ] Submit to: BetaList, AlternativeTo, G2, Capterra

### Days 7-30
- [ ] Leverage PH badge in all marketing materials
- [ ] Press outreach with "Ranked #X on Product Hunt" angle
- [ ] Create case studies from early PH users
- [ ] Weekly social content building on launch momentum

## 3.9 Success Metrics

| Metric | Good | Great | Product of the Day |
|--------|------|-------|-------------------|
| Upvotes | 200+ | 400+ | 600+ |
| Comments | 30+ | 60+ | 100+ |
| Website visits (launch day) | 2,000+ | 5,000+ | 10,000+ |
| Signups (launch day) | 100+ | 300+ | 500+ |
| Demo bookings | 10+ | 25+ | 50+ |

---

# PART 4: UI & GRAPHICS RECOMMENDATIONS

## 4.1 Current UI Assessment

### What Works Well
- Dark theme with cyan/blue accents — premium, developer-friendly
- Rotating hero headlines — each addresses a different pain point
- The 9-step workflow visualization — excellent visual storytelling
- Before/After comparison table — concrete, compelling data
- Cost cards ($90K, $24K/mo, $225K/yr, $555K total) — hard-hitting financial framing
- Evaluation artifacts sample — makes the AI output tangible
- FAQ accordion — addresses real objections from engineering leaders

### Critical Issues to Fix

**1. Empty dark sections (HIGH PRIORITY)**
Large portions of the page appear nearly black — content exists but is extremely low contrast against the dark background. When PH reviewers screenshot your product or users have different brightness settings, sections look broken or empty.

Fix: Add subtle gradient backgrounds or section separators. Increase body text contrast to minimum `#C0C0C0`. Add background textures/grid lines to break up emptiness.

**2. No social proof from real companies**
No customer logos, testimonials, or case study references visible. "10,000+ Interview Questions" is a product stat, not customer validation.

Fix: Add a "Trusted by" logo bar. Add 1-2 testimonials (can be anonymized: "CTO at Series B Fintech"). Add real usage metric: "X candidates screened" or "Y hours saved."

**3. No product demo/video**
For a voice AI product, seeing and hearing is believing. There's no embedded video or interactive demo showing the AI interview in action.

Fix: Embed a 60-second demo video in or just below the hero. Show the AI agent speaking, asking follow-ups, evaluating code.

**4. Hero CTAs could be stronger**
Current: "Book a Demo" + "See How It Works"

Better: "Screen Your First Candidate Free" (lower friction) + "Watch 2-Min Demo" (for those not ready). Add: "Set up in 24 hours, no credit card required."

**5. Page is very long (8000+ px)**
Users scroll through vast dark sections, especially on mobile.

Fix: Compress sections, reduce whitespace between content blocks, make workflow section horizontally scrollable on mobile.

## 4.2 Quick Wins (Before PH Launch)

1. **Add sticky "Book a Demo" bar** — CTA should be visible at all scroll positions
2. **Add live counter** — "X candidates screened this week" (dynamic social proof)
3. **Compress page length** — remove redundant whitespace between sections
4. **Add "Watch Demo" button in navbar** — most important action for employer visitors
5. **Increase text contrast** across all sections on the dark background
6. **Add section background variation** — alternate between pure dark and slightly lighter sections

## 4.3 Medium-Term UI Improvements

1. **Interactive demo** — let visitors try a 2-minute AI interview without signing up
2. **Case studies page** — linked from employer landing page
3. **ROI calculator** — "Enter team size + hiring volume → see savings" (gated behind email)
4. **Customer testimonial video** — even one 60-second clip from a real user

## 4.4 Graphics Asset Checklist

| Asset | Spec | Purpose | Priority |
|-------|------|---------|----------|
| PH Logo | 240x240px | Product Hunt listing | Critical |
| Gallery images (5 done) | 1270x760px | PH carousel | Done |
| Gallery images (3 more) | 1270x760px | GIF, testimonial, onboarding | High |
| Product video | 1920x1080, 1-2min | PH listing + landing page | High |
| OG image (social share) | 1200x630px | Twitter/LinkedIn cards | High |
| Animated GIF | 800x450px | PH listing + tweets | Medium |
| Email banner | 600x200px | Launch announcement email | Medium |
| Social media cards (5 variants) | 1200x675px | X, LinkedIn posts | Medium |

---

# PART 5: GO-TO-MARKET & VIRALITY STRATEGY

## 5.1 Strategic Positioning

**One-liner:** "The AI hiring engine that gives your CTO their time back."

**Frame:** Don't sell "AI interviewing." Sell velocity insurance for engineering teams. Roundz isn't an HR tool — it's an engineering capacity multiplier.

**Key hooks for virality:**
| Hook | Why It Spreads | Where to Use |
|------|---------------|-------------|
| "$555K/yr hidden cost" | Shocking, specific, shareable | Everything — hero, social, PH, ads |
| "5 out of 6 fail" | Visceral — every hiring manager has felt this | Social posts, PH description |
| Voice AI (not text tests) | Novel, easy to demo, audibly compelling | Video content, demos |
| "92% fraud detection" | Taps into universal frustration about cheating | Technical blog posts, PH |
| "The 80/20 model" | Simple framework, easy to remember and repeat | All messaging — becomes the brand |

## 5.2 Pre-Launch Content Engine (Weeks 1-4)

### "The Broken Hiring Series" — 5 pieces to establish authority before launch:

| # | Title | Platform | Hook |
|---|-------|----------|------|
| 1 | "We Analyzed 10,000 Technical Interviews. Here's Why 83% of Screening Fails." | LinkedIn + X thread | Data-driven, contrarian |
| 2 | "The $555K Tax: What Broken Hiring Actually Costs Your Startup" | Blog + LinkedIn | The specific dollar figure stops scrolling |
| 3 | "Why Senior Engineers Hate LeetCode — And What We Should Do Instead" | X thread + Dev.to + HN | Universal developer frustration — designed to go viral |
| 4 | "I Spent 33% of Q1 Interviewing Instead of Shipping. Never Again." | LinkedIn (founder post) | Authentic founder story, relatable to every CTO |
| 5 | "The Cheating Epidemic: 1 in 4 Candidates May Be Faking It" | X thread + blog | Provocative, data-backed, creates urgency |

### Community Engagement (Non-Spammy)
- **Hacker News**: Comment genuinely on hiring/AI threads (build karma for Show HN)
- **Reddit**: Participate in r/cscareerquestions, r/recruitinghell, r/startups, r/ExperiencedDevs
- **Twitter/X**: Engage with CTOs, VPs of Eng, hiring-related discussions daily
- **LinkedIn**: Connect with 200+ engineering leaders, comment on their posts
- **Discord/Slack**: Join Rands Leadership, CTO Craft, engineering communities

### Email List Target: 500+ subscribers before launch day
- Gate content: "Download: The True Cost of Manual Hiring Calculator"
- Add "Get Early Access" form on landing page

## 5.3 Launch Day Multi-Platform Blitz

### Twitter/X Posts (Ready to Use)

**Post 1 (12:15 AM PT):**
```
We just launched @roundzai on @ProductHunt

Your CTO spent 33% of last quarter interviewing candidates.
5 out of 6 who passed the screening still failed the live interview.

So we built an AI voice agent that conducts the technical interviews for you.

→ 10x faster screening
→ 80% less CTO time
→ 92% fraud detection

[PH link]
```

**Post 2 — Thread (9:00 AM PT):**
```
The average startup loses $555K/year to broken hiring.

Here's the breakdown (and how we fix it):

1/ Bad Hire Tax: $90,000+
One wrong hire costs salary, recruiter fees, severance — plus 6 months of damaged roadmap.

2/ Vacancy Tax: $24,000/month
Good candidates are gone in 10 days. If your process takes 30, you lose the best ones.

3/ CTO Time Tax: $225,000/year
Your highest-paid technical leader spends 33% of their time screening, not shipping.

4/ Total: $555,000+ per year

5/ How Roundz fixes this:
AI voice agents conduct real technical interviews — DSA, System Design, Behavioral.
100 applicants → AI screens → Top 20% to your team. CTO only interviews pre-vetted candidates.

Just launched on Product Hunt → [link]
```

**Post 3 — Engagement (12:00 PM PT):**
```
Hot take: LeetCode is broken for hiring.

Candidates hate it. Seniors refuse it. Juniors cheat with ChatGPT.

The fix isn't better coding tests.
The fix is AI that asks "why did you make that choice?" in real time.

Built this. Launched today → [link]
```

### LinkedIn Posts

**Post 1 — Founder story (7:00 AM PT):**
Personal narrative about the pain of spending Sundays screening resumes. End with the 80/20 model explanation and a link. Tag 5-10 CTOs/VPs of Eng.

**Post 2 — Data post (12:00 PM PT):**
Different angle — ask engineering leaders to share their worst hiring story. Creates engagement in comments.

### Hacker News — Show HN (9:00 AM PT)
Technical post covering: the problem, the approach (voice AI vs text tests), how it works (Pipecat + Daily.co + Bedrock Claude), tech stack overview. Invite technical questions.

### Reddit
- r/startups: Founder journey angle
- r/recruitinghell: "We're trying to fix this" (tread carefully — snarky sub)
- r/cscareerquestions: "What if AI interviews were actually good?"

## 5.4 Built-In Viral Loops

### Loop 1: Candidate → Employer (Primary)
```
Candidate takes AI interview → Gets detailed feedback →
Shares on LinkedIn ("Just did an AI interview, here's what I learned") →
CTO sees post → "We should try this for our hiring" →
Employer signs up
```
Amplify: Make feedback reports shareable. Add "Share Your Experience" prompt after every mock interview.

### Loop 2: Employer → Candidate (Secondary)
```
Employer uses Roundz → Candidates get screened →
Candidates experience the platform →
Candidates tell others → More sign up for mock interviews
```
Amplify: Every screened candidate gets an email — "Practice for your next interview with Roundz — 1 free mock interview."

### Loop 3: Content Virality (Amplifier)
```
Publish anonymized interview data →
"Did you know 23% of candidates attempt to cheat?" →
Gets shared in engineering circles →
Roundz brand = hiring intelligence authority → Inbound leads
```

## 5.5 Growth Hacks

| # | Tactic | How It Works |
|---|--------|-------------|
| 1 | **Free Screening Offer** | Give every new employer 3 free candidate screenings. Product sells itself once they see the evaluation output. |
| 2 | **"Hire or Don't Pay" Guarantee** | If AI screening doesn't improve pipeline quality in 30 days, full refund. Eliminates risk. |
| 3 | **ROI Calculator Tool** | Free tool: "How much is broken hiring costing you?" Input team size → personalized estimate. Gate behind email. Top-of-funnel engine. |
| 4 | **Interview Transparency Movement** | Publish insights: "10 Most Common System Design Mistakes", "What Separates Senior from Staff Engineers". Position as authority. |
| 5 | **"Bad Hire Insurance" Framing** | Reframe pricing: not "cost of AI screening" but "insurance against a $90K bad hire." ROI is 100x+. |
| 6 | **University/Bootcamp Partnerships** | Free mock interviews for graduating cohorts. Create lifelong users who eventually refer employers. |
| 7 | **Annual Anti-Cheat Report** | "The 2026 Interview Fraud Report" — becomes the most cited document in HR-tech, drives massive backlinks. |

## 5.6 Channel Strategy

| Channel | Focus | Frequency |
|---------|-------|-----------|
| **LinkedIn** | Founder personal brand, engineering leadership content, employee advocacy | 3x/week founder, 1x/week team |
| **Twitter/X** | "Hiring is broken" discussions, anti-cheating insights, build-in-public | Daily engagement, 2x/week posts |
| **Hacker News** | Technical credibility, architecture posts, Show HN | Monthly post, weekly comments |
| **YouTube** | Demo videos, "Watch an AI Interview", tutorials | 2x/month |
| **Dev.to/Hashnode** | Technical deep-dives (voice AI architecture, Pipecat integration) | 2x/month |
| **Reddit** | Participate in hiring/engineering discussions | Weekly |
| **LinkedIn Ads** (post-launch) | Target CTOs/VPs of Eng at 50-250 person companies | Ongoing |

## 5.7 Post-Launch Engagement (Days 2-30)

| Timeframe | Focus | Actions |
|-----------|-------|---------|
| **Days 2-3** | Ride the wave | Share PH results publicly; tag supporters |
| **Days 4-5** | Meta content | Publish "Behind the Scenes of Our PH Launch" (gets shared widely) |
| **Days 6-7** | Convert | Personalized follow-up to every PH commenter; offer free demo |
| **Week 2** | Case studies | Create stories from early PH users; reach out to press with ranking |
| **Week 3** | Paid experiments | LinkedIn ads targeting CTOs; Google Ads on "AI interview" keywords |
| **Week 4** | Assess | Review all metrics; double down on what works; plan Month 2 |

## 5.8 90-Day Roadmap

| Week | Focus | Key Milestones |
|------|-------|---------------|
| W1-2 | Content engine | 5 foundational pieces published, 500 email subscribers |
| W3-4 | Community | 200+ connections, PH coming soon page live, 300+ launch list |
| W5 | Launch prep | All assets ready, video done, list primed, DMs drafted |
| **W6** | **LAUNCH** | Product Hunt launch, multi-platform blitz, PR outreach |
| W7-8 | Convert | Follow up PH leads, publish case studies, podcast applications |
| W9-10 | Paid growth | LinkedIn/Google ads, A/B test messaging |
| W11-12 | Scale | Double down on top channels, hire growth person |
| W13 | Assess | Full metrics review, Q2 strategy |

## 5.9 Success Metrics

### Launch Day Targets
| Metric | Target |
|--------|--------|
| PH upvotes | 300+ |
| Website visits | 5,000+ |
| Candidate signups | 200+ |
| Employer demo bookings | 20+ |
| Social media impressions | 50,000+ |

### Month 1 Targets
| Metric | Target |
|--------|--------|
| Total signups | 1,000+ |
| Paid mock interviews | 100+ |
| Employer demos completed | 30+ |
| Employer conversions | 5+ |
| MRR | $5,000+ |

### Virality Metrics (Ongoing)
| Metric | Target |
|--------|--------|
| Viral coefficient (K) | > 0.3 |
| Referral signups | 20%+ of total |
| Social mentions/week | 50+ |
| Content shares/post | 25+ average |
| Organic search growth | 10% MoM |

---

# APPENDIX

## A. File Locations

| Resource | Path |
|----------|------|
| Knowledge Base | `/Users/nrabadiy/Documents/Rnd/Roundz_Product_KB/` |
| PH Gallery Assets | `assets/producthunt-gallery/` (5 PNGs + 5 editable HTMLs) |
| UI Codebase | `/Users/nrabadiy/Documents/Rnd/Codebase/UI/interview_networker_ws/interview-networker-ui/` |
| API Codebase | `/Users/nrabadiy/Documents/Rnd/Codebase/UI/interview_networker_ws/interview-networker-api/` |
| Existing Docs | `Roundz Master Doc.md`, `Why Roundz.md`, `Roundz Pitch Deck Preparation.md`, `Group_Discussion.md` |

## B. Referenced Research

| Source | Finding | Used In |
|--------|---------|---------|
| US Dept of Labor | Bad hire costs up to 30% of first-year earnings | Cost analysis |
| Officevibe | Top 10% candidates off market in 10 days | Urgency messaging |
| Stripe Developer Coefficient | 33% of dev time on technical debt / low-value work | CTO Time Tax |
| Glider AI | Candidate fraud risen 92% since remote hiring | Anti-cheat positioning |
| LinkedIn | 57% of candidates drop out due to slow process | Speed messaging |
| SHRM | Cost of bad hire data | Financial case |
| Karat | Engineering interview trends 2026 | Market context |

## C. Existing KB Documents Summary

| Document | Content |
|----------|---------|
| `Roundz Master Doc.md` | Problem definition, cost analysis, buyer persona ("Engineering Eric"), ICP, current solutions gap analysis, "what changed" narrative |
| `Why Roundz.md` | 6-point argument for voice AI over HackerRank — reasoning, signal quality, bandwidth, cheating resistance, bias reduction, consistency |
| `Roundz Pitch Deck Preparation.md` | SPSIL storytelling framework for pitch deck; positions Roundz as "flight simulator" for interviews |
| `Group_Discussion.md` | Recruiter perspective on SME hiring failures — unicorn JDs, LeetCode disconnect, process chaos, bias, equity delusion |
