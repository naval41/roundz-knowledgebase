> ⚠️ **LEGACY DOCUMENT (pre-2026-07 code review).** This file predates the code-verified `01-base-knowledge/Product_Ground_Truth.md`. It may contain claims flagged as inaccurate (for example: interviewer stack, unverified stats, "runs your code"). **Verify any claim against `Product_Ground_Truth.md` before using it externally.** Kept for historical/context value.

# Roundz.ai — UI & Graphics Recommendations for Product Hunt

## 1. Current UI Assessment

### What Works Well
- **Dark theme with cyan/blue accents** — premium, developer-friendly aesthetic
- **Rotating hero headlines** — each addresses a different pain point (talent loss, $555K waste, burnout, screening overload)
- **The 9-step workflow visualization** — excellent storytelling, walks through the entire funnel
- **Before/After comparison table** — concrete, compelling data
- **Cost cards** — $90K, $24K/mo, $225K/yr, $555K total — hard-hitting financial framing
- **Evaluation artifacts sample** — makes the AI output tangible (Strengths, Growth, Hire Reason, Verdict)
- **FAQ section** — addresses real objections from engineering leaders

### Critical Issues Found

#### Issue 1: Massive Empty Dark Sections (HIGH PRIORITY)
**Problem:** The full-page screenshot reveals multiple large sections that appear almost entirely black/empty. Content sections below the fold (workflow, features, trust section) are barely visible — text and elements are extremely low contrast against the dark background.

**Impact:** On Product Hunt, reviewers will screenshot your product. If sections look empty or broken, it kills credibility. Also, many users have brightness settings that will make dark-on-darker content invisible.

**Fix:**
- Add subtle gradient backgrounds or section separators between content blocks
- Increase contrast on all text — body text should be at minimum `#C0C0C0` on dark backgrounds
- Add background textures, patterns, or subtle grid lines to break up empty space
- Consider a light-mode option (PH audience skews light-theme)

#### Issue 2: No Social Proof from Real Companies
**Problem:** No customer logos, testimonials, or case study references visible on the employer landing page.

**Impact:** B2B buyers need social proof. "10,000+ Interview Questions" is a product stat, not customer validation. PH reviewers will specifically look for this.

**Fix:**
- Add a "Trusted by" logo bar (even 3-5 logos)
- Add 1-2 short testimonials from beta users (can be anonymized: "CTO at Series B Fintech")
- Add a real metric: "X candidates screened" or "Y hours saved"

#### Issue 3: No Product Demo/Video on Landing
**Problem:** No interactive demo, embedded video, or GIF showing the AI interview in action. For an AI voice product, seeing/hearing is believing.

**Fix:**
- Embed a 60-second demo video in the hero or just below it
- Show the AI agent actually speaking, asking follow-ups, evaluating code
- Include audio — voice AI's magic is in the conversation

#### Issue 4: Hero CTAs Could Be Stronger
**Current:** "Book a Demo" (primary) + "See How It Works" (secondary)

**Improvement:**
- Primary: "Screen Your First Candidate Free" (lower friction, immediate value)
- Secondary: "Watch 2-Min Demo" (for those not ready to commit)
- Add urgency: "Set up in 24 hours, no credit card required"

#### Issue 5: Mobile Experience
**Observation:** The page is long (8000+ px tall). On mobile, users will scroll through vast dark sections.

**Fix:**
- Compress sections on mobile — less whitespace between content blocks
- Make the workflow section horizontal-scrollable on mobile (it's the most important section)
- Ensure all interactive elements are thumb-friendly (44px minimum touch targets)

---

## 2. Product Hunt Gallery Images (5 Required)

Product Hunt shows images in a carousel. The first image is the hero — it's what appears in the feed and determines whether people click through. All images should be **1270x760px** (recommended) or similar 16:9 ratio.

### Image 1: Hero (THE Most Important)

**Concept: "The $555K Problem — Solved"**

```
Layout:
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│    [Roundz Logo]                                            │
│                                                             │
│    AI Voice Agents That Screen                              │
│    Engineers 10x Faster                                     │
│                                                             │
│    ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│    │   10x    │  │   80%    │  │   92%    │               │
│    │  Faster  │  │ Less CTO │  │  Fraud   │               │
│    │Screening │  │   Time   │  │Detection │               │
│    └──────────┘  └──────────┘  └──────────┘               │
│                                                             │
│    From 100 applicants → AI screens → Top 20% to your team │
│                                                             │
│    [Mini product screenshot showing interview interface]    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Design notes:**
- Dark background with blue/cyan accents (matches brand)
- Large, bold headline
- Three stats prominently displayed
- Small product screenshot for credibility
- Clean, not cluttered

### Image 2: The 80/20 Workflow

**Concept: "From 100 Applicants to Top 20%"**
- Clean version of the 9-step workflow from the landing page
- Horizontal flow: 100 candidates → AI Match → 40 Shortlisted → AI Interview → 20 Recommended → Your Team decides
- Show the funnel narrowing with numbers at each stage
- Use icons to represent each step (recruiter, AI, interview, evaluation)

### Image 3: AI Interview in Action

**Concept: "See the AI Interview"**
- Split screen showing:
  - Left: AI voice agent waveform + conversation transcript
  - Right: Monaco code editor with candidate's code
- Or: screenshot from the actual `/interview-session` page
- Include the Excalidraw system design view as an inset
- Caption: "Voice AI conducts DSA, System Design, LLD, and Behavioral rounds"

### Image 4: Evaluation Artifacts

**Concept: "Transparent AI — Every Decision Explained"**
- Show the actual evaluation output:
  ```
  Strengths: Strong system design, clean code patterns
  Growth Areas: Time complexity optimization
  Hire Reason: Deep architecture knowledge, practical approach
  Final Verdict: ✅ HIRE
  ```
- Include a sample detailed rubric with scores
- Caption: "Explainable AI — your hiring managers see exactly WHY"

### Image 5: Before vs After

**Concept: "From Hiring Chaos to Hiring Clarity"**
- Two-column comparison table (from landing page):
  - Time to screen: 40+ hrs/week → 4 hrs/week
  - Time to hire: 45 days → 12 days
  - Candidate drop-off: 60% → under 15%
  - CTO involvement: Every screen → Final round only
  - Fraud detection: Manual → AI-verified real-time
  - Availability: Business hours → 24/7
- Make the "With Roundz" column pop with green/cyan highlights

---

## 3. Product Video (1-2 Minutes)

### Script Outline

**[0:00-0:15] The Hook**
"Your CTO spent 33% of last quarter interviewing candidates. 5 out of 6 failed the live round anyway. That's $555K a year in broken hiring."

**[0:15-0:30] The Promise**
"Roundz is an AI hiring engine. Voice AI agents that conduct real technical interviews — not just coding tests."

**[0:30-1:00] The Demo**
- Show: Employer creates a job posting
- Show: AI enriches skill requirements
- Show: Candidates applying, resume matching scores appearing
- Show: AI voice interview in action (voice waveform, follow-up questions, code editor)
- Show: Evaluation report generated (strengths, verdict)

**[1:00-1:20] The Results**
"Teams using Roundz screen 10x more candidates in 80% less time. Time-to-hire drops from 45 days to 12."

**[1:20-1:40] Trust & Differentiators**
"92% fraud detection. Explainable AI — every score shows WHY. Human-in-the-loop — you always make the final call."

**[1:40-2:00] CTA**
"Screen your first candidate within 24 hours. No credit card required. Try Roundz free."

### Production Notes
- Screen recordings of the actual product (not mockups)
- Voiceover: confident, technical tone (not salesy)
- Background music: subtle, modern, tech-feel
- Show real UI — PH community respects authenticity over polish

---

## 4. Branding Recommendations for PH Launch

### Color Palette (Current — Keep)
| Color | Hex | Usage |
|-------|-----|-------|
| Background (dark) | `#0A0F1C` or similar | Primary background |
| Cyan/Blue accent | `#00B4D8` or `#0EA5E9` | CTAs, highlights, stats |
| Orange/amber | `#F59E0B` | Warnings, cost figures, secondary accent |
| Text primary | `#E2E8F0` | Headings |
| Text secondary | `#94A3B8` | Body text |

### Typography
- Keep the current modern sans-serif
- Ensure headings are bold/heavy weight for PH gallery readability
- Gallery images text should be minimum 24px for readability at thumbnail size

### Logo for PH
- Current logo works but needs a **240x240px square version**
- On PH it appears as a small icon — must be recognizable at 40x40px
- Consider: just the "R" logomark on dark background, or the bolt/signal icon

---

## 5. Additional UI Improvements Before Launch

### Quick Wins (Do Before Launch)

1. **Add a sticky "Book a Demo" bar** on the employer page — users scroll 8000px, the CTA should always be visible

2. **Add a live counter** — "X candidates screened this week" or "X interviews conducted today" — dynamic social proof

3. **Compress page length** — the 8000px page is too long. Consider:
   - Collapsing the FAQ (already accordion-style, good)
   - Making the workflow section more compact
   - Removing redundant sections

4. **Add interactivity to the workflow** — instead of a static timeline, make each step clickable to expand details

5. **Add a "Watch Demo" button in the nav** — most important action for employer visitors

### Medium-Term (Post-Launch)

6. **Build an interactive demo** — let visitors try a 2-minute AI interview without signing up (huge conversion driver)

7. **Add case studies page** — link from the employer landing page

8. **Add an ROI calculator** — "Enter your team size and hiring volume, see how much you save"

---

## 6. Graphics Asset Checklist

| Asset | Size | Purpose | Priority |
|-------|------|---------|----------|
| PH Logo | 240x240px | Product Hunt listing | Critical |
| Gallery Image 1 (Hero) | 1270x760px | PH feed thumbnail | Critical |
| Gallery Image 2 (Workflow) | 1270x760px | PH carousel | Critical |
| Gallery Image 3 (Interview) | 1270x760px | PH carousel | Critical |
| Gallery Image 4 (Evaluation) | 1270x760px | PH carousel | High |
| Gallery Image 5 (Before/After) | 1270x760px | PH carousel | High |
| Product Video | 1920x1080, 1-2min | PH listing | High |
| OG Image (social share) | 1200x630px | Twitter/LinkedIn cards | High |
| Animated GIF | 800x450px | PH listing, tweets | Medium |
| Email banner | 600x200px | Launch announcement | Medium |
| Social media cards (5 variants) | 1200x675px | X, LinkedIn posts | Medium |
