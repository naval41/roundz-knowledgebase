> ⚠️ **LEGACY DOCUMENT (pre-2026-07 code review).** This file predates the code-verified `01-base-knowledge/Product_Ground_Truth.md`. It may contain claims flagged as inaccurate (for example: interviewer stack, unverified stats, "runs your code"). **Verify any claim against `Product_Ground_Truth.md` before using it externally.** Kept for historical/context value.

# Roundz.ai — Structured Product Knowledge Base

## 1. Product Identity

| Field | Value |
|-------|-------|
| **Product Name** | Roundz.ai |
| **Tagline** | AI-Powered Technical Hiring Engine |
| **URL** | https://roundz.ai |
| **Category** | B2B SaaS — HR Tech / AI Hiring |
| **Target Audience** | Engineering leaders (CTOs, VPs of Eng) at Series A–C startups (50–250 employees) |
| **Core Promise** | Screen 10x more candidates, spend 80% less engineering time on interviews |

---

## 2. Core Value Propositions

1. **10x Faster Screening** — AI voice agents conduct full technical interviews 24/7, replacing weeks of manual scheduling
2. **80% Less CTO Time** — Engineering leaders only see top 20% pre-vetted candidates
3. **92% Fraud Detection** — Real-time proctoring catches AI-assisted cheating, tab-switching, proxy interviewers
4. **$555K/yr Savings** — Eliminates the compounding cost of bad hires ($90K), vacancy tax ($24K/mo), and CTO time tax ($225K/yr)

---

## 3. System Architecture Overview

### Tech Stack
| Layer | Technology |
|-------|-----------|
| **Frontend** | Next.js 14 (App Router), React 18, TypeScript, Tailwind CSS |
| **State Management** | Zustand (client), TanStack React Query (server state) |
| **Backend** | Node.js, Express, TypeScript |
| **Database** | PostgreSQL via Prisma ORM |
| **AI/LLM** | AWS Bedrock (Claude) for evaluation, Google Gemini for skill extraction |
| **Voice AI** | Pipecat AI + Daily.co WebRTC transport |
| **Code Editor** | Monaco Editor (50+ languages) |
| **Design Tool** | Excalidraw (system design whiteboard) |
| **Proctoring** | MediaPipe Vision (face detection, gaze tracking) |
| **Payments** | Razorpay (UPI, cards, netbanking) |
| **File Storage** | AWS S3 (resumes, logos) |
| **Async Processing** | AWS SQS + Lambda + Step Functions |
| **Monitoring** | CloudWatch metrics, Pino structured logging |
| **Auth** | JWT (access + refresh tokens) + Google OAuth2 |

### High-Level Data Flow
```
Candidate/Employer → Next.js UI → Axios (with JWT interceptors) → Express API
                                                                      ↓
                                              PostgreSQL (Prisma) ←→ SQS Queues
                                                                      ↓
                                              Lambda Functions (evaluation, matching, consolidation)
                                                                      ↓
                                              Bedrock Claude / Gemini API → Feedback + Scoring
```

---

## 4. User Roles & Portals

### 4.1 Candidate Portal
| Feature | Route | Description |
|---------|-------|-------------|
| Landing | `/` | Hero, features, testimonials, CTAs |
| Auth | `/login`, `/signup` | Email/password + Google OAuth |
| Interview Prep | `/mock-interview` | Browse & purchase AI mock interviews |
| Live Interview | `/interview-session/[roomId]` | Voice AI interview with code editor + whiteboard |
| Job Board | `/jobs` | Browse open positions, apply with resume |
| Community | `/interviews`, `/groups` | Share interview experiences, join groups |
| Profile | `/profile` | Education, experience, projects, skills |
| Pricing | `/pricing` | 3 tiers: DSA (free trial), LLD ($15), HLD ($15) |

### 4.2 Employer Portal
| Feature | Route | Description |
|---------|-------|-------------|
| Landing | `/employer` | Marketing page for enterprises |
| Dashboard | `/employer/home` | Pipeline overview, hiring metrics |
| Job Management | `/employer/jobs` | Create/edit job postings with AI skill enrichment |
| Candidate Pipeline | `/employer/candidates` | View applicants, skill match scores, screening status |
| Interview Loops | `/employer/loops` | Configure multi-round interview workflows |
| Interview Review | `/employer/interviews` | View AI-conducted interview results + artifacts |
| Billing | `/employer/pricing`, `/employer/credit-audit` | Purchase credits, track usage |
| Notifications | `/employer/notifications` | Application & screening alerts |

### 4.3 Admin Portal
| Feature | Route | Description |
|---------|-------|-------------|
| Management | `/manage` | Feature flags, user management, blog, email, workflows |

---

## 5. Core Workflows

### 5.1 Employer Hiring Pipeline (The 80/20 Model)

```
Step 1: Create Job Description
  → Recruiter defines role, requirements, evaluation criteria
  → JobRack created (status: SOURCING)

Step 2: AI Enhances Skills
  → Roundz analyzes JD, enriches skill taxonomy
  → Lambda triggers via ENRICHING_SKILLS_QUEUE
  → Status: ENHANCING

Step 3: Invite Candidates
  → Public link or direct invitations
  → 100 candidates apply → CandidateJobRackInfo records created

Step 4: Resume Validation & Matching
  → Lambda (matching-skill-score) extracts skills from resume via Gemini
  → Compares against enhanced job skills
  → Assigns profileMatchingScore (0-100)
  → Status: SOURCED → SCREENING_SHORTLIST

Step 5: Smart Shortlisting
  → Recruiter reviews AI scores, shortlists top matches
  → ~40 of 100 shortlisted by match score

Step 6: AI Voice Screening (24/7)
  → Interview loop assigned (DSA + LLD + HLD rounds)
  → Pipecat AI Voice Agent conducts each round
  → Real-time proctoring: face detection, gaze tracking, keyboard monitoring
  → Transcripts recorded per session
  → 1 credit deducted per candidate per screening

Step 7: LLM Evaluates Results
  → Lambda (candidate-interview-evaluation) processes transcripts
  → Bedrock Claude evaluates per workflow step
  → Multi-dimensional assessment: technical, behavioral, communication

Step 8: Evaluation Artifacts
  → Strengths, growth areas, hire reasoning generated
  → Final verdict: STRONG_HIRE / HIRE / LEANING_HIRE / NO_HIRE / STRONG_NO_HIRE
  → Lambda (feedback-consolidation) aggregates across rounds

Step 9: Final Human Decision
  → Top 20% (~20 candidates) presented to hiring team
  → Full evaluation reports with explainable AI reasoning
  → Team makes final call
```

### 5.2 Candidate Mock Interview Flow

```
1. Browse mock interviews on /mock-interview
2. Select type: DSA (free trial), LLD ($15), HLD ($15)
3. Payment via Razorpay (or free trial)
4. CandidateInterview created (PENDING)
5. Enter interview room → Daily.co WebRTC connection
6. Pipecat AI agent begins conversation
7. Candidate uses:
   - Voice for discussion
   - Monaco Editor for coding (DSA/LLD)
   - Excalidraw for system design diagrams (HLD)
8. Proctoring active: face detection, gaze tracking
9. Interview completes → status: REVIEW_IN_PROGRESS
10. Lambda evaluates transcript via Bedrock Claude
11. Structured feedback delivered via email + dashboard
12. Status: COMPLETED
```

### 5.3 Interview Types Supported

| Type | Code | Duration | What's Tested |
|------|------|----------|--------------|
| **Data Structures & Algorithms** | CODING | 60 min | Problem solving, time/space complexity, live coding |
| **Low-Level Design** | LLD | 60 min | OOP, SOLID principles, design patterns, code extensibility |
| **High-Level Design** | SYSTEM_DESIGN | 60 min | Architecture, scalability, failure handling, trade-offs |
| **Behavioral** | BEHAVIORAL | Varies | Communication, leadership, conflict resolution |
| **Intro/Wrap-up** | INTRO/WRAP_UP | Varies | Opening/closing segments |

---

## 6. Key Database Entities (104 Prisma Models)

### Core Domains

**User Management:** User, UserProfile, Education, Experience, Project, Client (multi-tenant employer org)

**Job Pipeline:** JobRack (SOURCING → ENHANCING → SCREENING → SHORTLISTING → CLOSED), JobProfile, JobRole, CandidateJobRackInfo (with skill matching & hire decision)

**Interview System:** MockInterview (template), CandidateInterview (session: PENDING → IN_PROGRESS → REVIEW_IN_PROGRESS → COMPLETED), SessionDetails, Transcript, Workflow, WorkflowStep

**Evaluation:** EvaluationFeedback, EvaluationFeedback_StrengthGrowth, EvaluationDetailedSummary

**Knowledge Bank:** KnowledgeBank, InterviewQuestion, QuestionCodeSignature, QuestionHints, QuestionAnswers, QuestionSolution

**Interview Loops:** Loop, LoopMapping, CandidateLoopEntry

**Commerce:** Service, Order, OrderLine, Payment, Invoice, FreeTrialUsage (with abuse detection)

**Employer Billing:** EmployerService (Starter/Growth/CustomPack/Small/Medium/Large), EmployerServicePack, EmployerOrder, EmployerSubscription, EmployerCreditState, EmployerCreditAudit

**Proctoring:** ProctorEvents (KEYBOARD, VISIBILITY, GAZEOFFSCREEN)

**Community:** CommunityGroup, GroupMembership, GroupPost, GroupPostComment, GroupPostVote

---

## 7. API Architecture

### Key Endpoint Groups (35+ route files)

| Domain | Endpoints | Auth |
|--------|-----------|------|
| Auth | `/api/auth/*` (register, login, Google OAuth, refresh, forgot/reset password) | Public |
| Mock Interviews | `/api/mock-interviews/*` (CRUD, start session, transcript, proctor events) | JWT |
| Evaluation | `/api/evaluation-feedback/*`, `/api/consolidated-feedback/*` | JWT |
| Employer Jobs | `/api/employer/jobrack/*` (CRUD, enrich, candidates) | JWT + Employer role |
| Employer Loops | `/api/employer/loops/*` (create, start-screening) | JWT + Employer role |
| Employer Billing | `/api/employer/services/*`, `/api/employer/orders/*`, `/api/employer/credit-*` | JWT + Employer role |
| Candidate Orders | `/api/orders/*` (create, verify-payment, invoice) | JWT |
| Community | `/api/groups/*`, `/api/posts/*` | JWT |
| Interviews | `/api/interviews/*` (community interview experiences) | JWT |
| Admin | `/api/admin/*` (users, companies, feature flags, notifications) | JWT + Admin role |

### Async Processing Pipeline (SQS Pollers)
```
PollerManager (starts on server boot)
├── EnrichingSkillsPoller → Enriches job descriptions with AI
├── CandidateSourcingPoller → Resume parsing + skill extraction (Gemini)
├── ScreeningPoller → Auto-assigns interview loops, deducts credits
└── EvaluationPoller → Triggers interview evaluation (Bedrock Claude)
```

---

## 8. Multi-Tenancy & Security

| Feature | Implementation |
|---------|---------------|
| **Multi-Tenancy** | clientId on User/Client; all employer data scoped to clientId |
| **Auth** | JWT access token (15min) + refresh token (7d, HTTP-only cookie) |
| **Roles** | USER, EMPLOYER, ADMIN with middleware enforcement |
| **Passwords** | bcryptjs with salt |
| **Proctoring** | MediaPipe face detection, gaze tracking, keyboard monitoring |
| **Content Moderation** | leo-profanity filter on interview submissions |
| **Free Trial Abuse** | IP/user-agent tracking, blacklist mechanism |
| **Credit Controls** | Soft limit — deduct before interview to prevent overspend |
| **Feature Flags** | Per-user feature flag assignments for gradual rollout |

---

## 9. Employer Credit System

```
Buy Credits → EmployerOrder + EmployerSubscription
                ↓
EmployerCreditState tracks: total / remaining / used
                ↓
On Screening: 1 credit per candidate (AI_SCREENING source)
                ↓
EmployerCreditAudit logs every transaction
```

Service tiers: Starter, Growth, CustomPack, Small, Medium, Large

---

## 10. Frontend Architecture

### Key Libraries
- **Pipecat AI + Daily.co** — AI voice interview sessions
- **Monaco Editor** — Live coding during interviews
- **Excalidraw** — System design whiteboard
- **MediaPipe Vision** — Cheating detection (face/gaze tracking)
- **Razorpay** — Payment processing
- **TanStack React Query** — Server state management
- **Zustand** — Client state (view limits, counters)
- **Radix UI** — Accessible UI primitives
- **Framer Motion** — Animations
- **Recharts** — Analytics dashboards

### Data Fetching Pattern
```
Components → useApiQuery/useApiMutation (TanStack wrappers)
                ↓
Axios instances: publicAxios / privateAxios / interviewAxios
                ↓
Interceptors: auto-attach JWT, handle 401 refresh, cross-tab sync
```

---

## 11. Landing Page Structure (roundz.ai/employer)

| Section | Content |
|---------|---------|
| **Hero** | Rotating headlines ("Stop losing top talent...", "Stop wasting $555K/yr...", "Stop burning out your engineering team...", "Stop screening candidates all day") + CTAs (Book a Demo, See How It Works) |
| **Stats Bar** | 10x Faster Screening, 80% Less CTO Time, 92% Fraud Detection |
| **Social Proof** | 10,000+ Interview Questions, 45 min Deep Screening, 24/7 Global Availability |
| **Hidden Cost** | 4 cost cards: Bad Hire Tax ($90K+), Vacancy Tax ($24K/mo), CTO Time Tax ($225K/yr), Total ($555K+) |
| **Before/After Table** | "From Hiring Chaos to Hiring Clarity" — 7 metrics compared |
| **9-Step Workflow** | Visual pipeline from Job Description → AI Screening → Top 20% |
| **Evaluation Artifacts** | Sample AI output (Strengths, Growth, Hire Reason, Verdict) |
| **Feature Grid** | 6 features: Voice AI, Multi-Round, Anti-Cheat, Explainable AI, Semantic Matching, 24/7 |
| **Trust Section** | Human-in-the-Loop, Enterprise Privacy, Full Transparency, Better Candidate Experience |
| **FAQ** | 8 questions for engineering leaders |
| **CTA** | "Ready to Fix Your Hiring Funnel?" + Book a Demo |

---

## 12. Candidate Pricing

| Plan | Price | Features |
|------|-------|----------|
| **DSA** | Free trial (then $10) | 60 min, live coding, think-aloud, seniority-based difficulty |
| **Low-Level Design** | $15 (was $20) | 60 min, OOP/SOLID, design patterns, code review |
| **High-Level Design** | $15 (was $20) | 60 min, interactive design playground, architecture scoring |

Payment: Razorpay (UPI, cards, netbanking). Prices in USD, auto-converted to INR for India.

---

## 13. Competitive Positioning

| vs. | Roundz Advantage |
|-----|-----------------|
| **HackerRank/LeetCode** | Voice AI tests reasoning, not just code output. Catches cheaters. Senior-friendly. |
| **Manual Screening** | 24/7, 10x throughput, standardized rubric, no interviewer fatigue |
| **Agencies** | No 20-25% salary commission. Higher signal-to-noise. |
| **ATS (Greenhouse/Lever)** | Evaluates, not just stores. Semantic matching, not keyword matching. |
| **Adding More Recruiters** | Solves the technical bottleneck, not just the volume problem |

---

## 14. Key Metrics & Claims

- 10,000+ interview questions in knowledge bank (1,100+ coding, 80+ LLD, 50+ HLD)
- 45-minute deep screening sessions
- 24/7 global availability
- Reduces time-to-hire from 45 days to 12 days
- Top candidate drop-off: from 60% to under 15%
- CTO involvement: from every screen to final round only
