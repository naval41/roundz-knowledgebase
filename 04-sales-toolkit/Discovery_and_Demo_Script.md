# Discovery-First Demo Script: Roundz (roundz.ai)

**Audience:** Employer buyer, CTO / VP Eng / Head of Talent at an engineering org.
**Wedge:** Lead with the **agentic-coding round**: the reason screening signal died and the reason Roundz exists.
**Method:** Kazanjy demo discipline. The equation for the whole call:

> **Sale = Potential Value × Value Comprehension × Belief**

If any of the three is zero, the deal is zero. So the call is engineered to (1) quantify *their* potential value in *their* numbers, (2) show only what they can comprehend and confirm, and (3) build belief with explainable proof, not claims.

**Desired next step (state it to yourself before the call):** a **priced pilot on ONE open req**, with a **start date booked before you hang up**.

---

## 0. Honesty Guardrails: read before every call

These are non-negotiable. Breaking them kills belief the moment a technical buyer catches it.

1. **Never claim code execution or test-case pass rates.** Roundz **evaluates approach, complexity, and the correctness of reasoning**: not "we ran your tests and it passed." Say "evaluates approach, complexity, and correctness of reasoning."
2. **All cost/fraud stats are industry research, not Roundz outcomes.** Cite the source out loud: US DoL / SHRM (cost of a bad hire), Officevibe / LinkedIn (interview time burden), Stripe Developer Coefficient (engineering time waste), Glider AI (interview fraud). Never present them as "our customers saw..."
3. **Correct stack, if asked:** live voice interviewer = **Google Gemini 2.5 Flash**; evaluation/scoring = **AWS Bedrock (Claude)**; resume↔JD matching = **Gemini**; speech-to-text = **Deepgram**; text-to-speech = **Kokoro**.
4. **No fabricated logos, customer names, or testimonials.** If you have none yet, sell the pilot, not fake social proof.
5. **The agentic-coding round is live-demoable** (confirmed 2026-07-25), make it the centerpiece of the demo. Show a real copilot session live, then the telemetry view and the competency score it produces.

---

## 1. Pre-Call Planning Checklist

Do this the day before. Ten minutes of research buys you the right to run discovery.

**Account**
- [ ] What do they build? (product, stack, scale), skim their engineering blog / careers page.
- [ ] Company stage & headcount, are they scaling eng right now?
- [ ] Any public signal on hiring volume (open reqs on their site, LinkedIn job posts).

**Attendees**
- [ ] Who is on the call and what do they own? (CTO = quality of hire + eng time; Head of Talent = throughput + time-to-fill; VP Eng = both).
- [ ] Their background, did they come up as an IC? (If yes, the "job changed to directing AI" teach lands harder.)

**Current stack & process (hypothesize, then confirm in discovery)**
- [ ] What do they likely screen with today? (HackerRank / CoderPad / take-home / recruiter phone screen / nothing structured).
- [ ] Guess their weak point: volume they can't handle, or signal they don't trust.

**Open reqs (this is your pilot target)**
- [ ] Identify 1–2 live engineering reqs. Pick the one with **high applicant volume** or **most senior-eng interview drain**: that's where the pilot ROI is obvious.

**Agenda & desired next step**
- [ ] Written agenda ready (see up-front contract below).
- [ ] Desired outcome fixed in your head: **priced pilot on the [specific req], start date booked.**

---

## 2. Call Structure (scripted)

Rough time budget for a 45-minute call:
Rapport 2 · Up-front contract 2 · **Discovery 12–15** · Mirror-back 2 · **Demo 15** (most of it on the agentic round) · ROI math 5 · Ask 3.

> Discovery is longer than the demo on purpose. You cannot compute their Potential Value or earn Belief without it.

---

### 2a. Rapport (brief: ~2 min)

Keep it short and specific to *them*, not the weather.

> "Thanks for the time, [Name]. I saw [specific thing, you just posted three backend roles / your eng blog post on X]. Before I show you anything, I'd rather understand how you actually hire engineers today so this isn't a generic pitch. That work for you?"

---

### 2b. Up-Front Contract (~2 min): agree agenda, time, and that a decision results

Say it close to verbatim:

> "Here's what I'd propose for the next [45] minutes. First I'll ask you a bunch of questions about how you screen engineers today and where it hurts, that's most of the value for me. Then I'll show you the parts of Roundz that map to what you tell me, not a full tour. Then we'll do quick math on your actual numbers.
>
> At the end, one of three things is true: it's clearly not a fit and you tell me that and we don't waste each other's time; you need something before you can decide and we agree what that is; or it *is* interesting and we pick one open role to run a small paid pilot on and book a start date. All of those are fine outcomes, I just want us to leave with a real decision instead of a 'let me think about it.' Fair?"

Get the explicit "yeah, fair." That "yes" is what lets you ask for the sale at the end without it feeling abrupt.

---

### 2c. Discovery FIRST (~12–15 min): surface felt pain

Ask, then **shut up and listen**. Take notes out loud ("got it, so ~40 hours a month of senior time..."). You'll reuse their exact numbers in the ROI math and their exact words in the mirror-back.

Grouped by intent. You won't ask all 14, pick the live threads.

**PAIN (where it hurts today)**
1. "Walk me through what happens today from 'a candidate applies' to 'an engineer talks to them.' Who touches it and where does it get stuck?"
2. "When you use [HackerRank / take-homes / whatever they named], how much do you *trust* the score? Do you still re-verify in the onsite?"
3. "How often does someone pass your coding screen and then clearly can't reason through problems live? Roughly what's your pass-the-screen / fail-the-onsite rate?"
4. "Since AI coding tools became normal, has your screen gotten easier to game? Are candidates shipping code that runs but that they can't explain?"

**PROCESS (how the machine runs)**
5. "How many applicants do you get per engineering req right now? How many can you realistically give a real screen to?"
6. "Who runs first-round technical screens, recruiters, or your engineers? How many hours a week are your senior engineers in interviews?"
7. "How consistent is the bar across interviewers? If two engineers screen the same candidate, do they land in the same place?"
8. "How do you interview for AI-assisted work today, do you let candidates use Copilot / an AI in the interview, or ban it?"

**IMPACT (what it costs)**
9. "What's your current time-to-hire for an engineer? What does a slow req cost you, delayed roadmap, load on the current team?"
10. "When a hire doesn't work out, what's the real cost to you, ramp, backfill, the manager's time, team morale?"
11. "If you got back [X] senior-engineer hours a month, where would that time go?"

**BUYING PROCESS (can this actually close)**
12. "If a pilot proved this out, who besides you is in the decision? Anyone in security/procurement I should get ahead of?"
13. "Do you have a budget line for hiring/assessment tools, or would this come out of an eng or talent budget?"
14. "What would you personally need to see to say 'yes, let's run this on a real req'?"

> **The signal you're mining for:** the gap between "code that runs" and "an engineer who can reason and direct." Get them to say some version of it in their own words. That admission is what makes the agentic round land later.

---

### 2d. Mirror the Problem Back (~2 min): before any demo

Reflect their pain in their language, then get the teach-up "yes."

> "Let me play back what I heard. You get ~[N] applicants a req, your engineers are burning ~[hours] a month screening, and the screen you have doesn't fully de-risk it, people pass the coding test and then can't reason through the onsite, and it's gotten worse now that anyone can prompt an AI into working code. A bad hire runs you [their number]. Did I get that right?"

Wait for confirmation. Then the reframe (this is the Challenger teaching moment, see §3):

> "Here's the thing I think is actually going on, and it's bigger than tooling. The old screen measured *can you produce correct code.* But AI produces correct code now for free. So that screen is measuring a skill the job no longer rewards. **The job changed: it's now about directing AI well: decomposing the problem, judging the output, catching where the model is wrong.** Nobody's screen tests for that yet. Can I show you what testing for *that* looks like?"

That question is your permission to demo. Only now do you share your screen.

---

### 2e. Demo by Sections

Rules for every section below:
- **Show the ONE pain it maps to** (theirs, in their words), not a feature list.
- **Get a micro-yes** before moving on ("Does that match how you'd want to see it?").
- Spend the **most time on Section 3 (the agentic round)**: it's the wedge.

---

#### Section 1: Post a role + semantic resume→JD match & shortlist
- **Show:** paste/point at a JD (ideally their pilot req), show semantic matching rank applicants against it, and the auto-shortlist.
- **Maps to pain:** #5 volume / "we can't give everyone a real screen." (Stack note if asked: matching runs on **Gemini**.)
- **Micro-yes:** "If the top of this list were the only people your engineers had to think about, would that help?"

#### Section 2: Live voice interview, code + whiteboard aware
- **Show:** a live voice AI interviewer (built on **Gemini 2.5 Flash**, STT **Deepgram**, TTS **Kokoro**) conducting a round; the candidate's **live code in Monaco** and **system-design on Excalidraw** are watched in real time, so the interviewer asks follow-ups on *what the candidate is actually doing*.
- **Say (guardrail):** "It's not running your test suite: it's evaluating their **approach, complexity, and the correctness of their reasoning**, the way a good engineer sitting next to them would."
- **Maps to pain:** #6 senior-eng hours + #7 inconsistent bar, same rigorous interview, every candidate, no engineer in the room.
- **Micro-yes:** "Is that the kind of conversation your engineers wish they had time to run every time?"

#### Section 3: THE AGENTIC-CODING ROUND *(spend the most time here: the wedge)*
> **Pre-flight:** this round is live-demoable: run it live. Have a real problem loaded and drive a short copilot session, then open the **telemetry view + competency score**. This is the moment of the call; give it the most time.

- **Frame first (tie to the teach):** "Remember the reframe, the job is now directing AI. So this round hands the candidate an AI copilot *on purpose* and scores **how they direct it**, not whether they can avoid it."
- **Show (live or via telemetry):**
  - The candidate solving **with an AI copilot**.
  - **Prompt quality**: are they specifying the problem well?
  - **Decomposition**: do they break the task into the right sub-problems?
  - **Accept / reject telemetry**: do they blindly accept AI output or catch and correct bad suggestions?
  - **Judgment & token efficiency**: do they get to a good answer economically, or thrash?
  - The resulting **agentic-competency score**.
- **Maps to pain:** #4 + #8, "code runs but they can't explain it" and "we don't know how to interview for AI-assisted work." This is the only thing on the call that directly tests the skill they admitted they can't measure.
- **Micro-yes (the big one):** "If you could see *this*, how a candidate actually directs AI, before your engineers spend a minute on them, does that change the quality of who reaches your onsite?"

#### Section 4: Explainable report + hire verdict
- **Show:** the **level-aware (ENTRY / MID / SENIOR)** rubric-scored report, per-competency breakdown with evidence, and the **hire verdict (STRONG_HIRE → STRONG_NO_HIRE)**. Emphasize it's **explainable**: every score points to what the candidate said/did (evaluation runs on **AWS Bedrock / Claude**).
- **Maps to pain:** #2 "do you trust the score" + #7 consistency, a defensible, evidence-backed verdict your engineers will actually believe.
- **Micro-yes:** "Would your engineers trust a verdict that shows its work like this?"

#### Section 5: Proctoring / anti-cheat
- **Show:** the proctoring signals and integrity flags on the report.
- **Maps to pain:** #3 + the gaming problem; anchor with the **industry stat**: "Glider AI's research on interview fraud is one reason integrity matters here, [cite figure if you have it]."
- **Micro-yes:** "Does that cover the 'how do we know it was really them' question your team will ask?"

#### Section 6: The 80/20 human-in-the-loop framing *(land the model here)*
- **Say:** "Important: Roundz never makes the hire. **We filter; your engineers make the call.** We do the heavy top-of-funnel screening so your team only meets the **pre-vetted top ~20%**: the people worth their time. Humans stay in the loop on every decision that matters."
- **Maps to pain:** #6 (eng time) + defuses the "you want AI to hire for us?" objection before it's raised.
- **Micro-yes:** "Is meeting only the top ~20%, pre-vetted, the workflow you'd want?"

---

### 2f. Live ROI Math (~5 min): walk THEM through THEIR numbers

Use the numbers they gave you in discovery. Compute it live, out loud. Label it **illustrative**.

**Formula A: Senior-engineer time recovered**
```
Applicants per req                         = A
Share you'd screen with a human today      = s   (e.g. 30%)
Human screens avoided                      = A × s  (Roundz pre-vets these)
Senior-eng hours per screen (incl. review) = h   (e.g. 1.0)
Loaded senior-eng cost / hour              = C   (e.g. $90)

Time recovered per req  = A × s × h        (hours)
Dollar value per req    = A × s × h × C
Annualized              = (A × s × h × C) × reqs_per_year
```

**Worked example (illustrative: swap in their numbers):**
```
A = 200 applicants/req,  s = 30%,  h = 1.0 hr,  C = $90/hr,  reqs = 10/yr

Human screens avoided / req = 200 × 0.30      = 60 screens
Hours recovered / req       = 60 × 1.0        = 60 senior-eng hours
Dollar value / req          = 60 × $90        = $5,400
Annualized (10 reqs)        = $5,400 × 10     = $54,000/yr in recovered eng time
```

**Formula B: Bad-hire avoidance**
```
Bad-hire rate today            = b   (e.g. 1 in 8 = 12.5%)
Fully-loaded cost of a bad eng hire = B  (US DoL / SHRM cite: often 1.5–2× salary+)
Eng hires per year             = H

Expected bad-hire cost today   = b × B × H
If Roundz cuts bad-hire rate by even a modest fraction f,
Avoided cost / yr              = b × B × H × f
```

**Worked example (illustrative):**
```
b = 12.5%,  B = $150,000 (per SHRM-style estimates),  H = 10,  f = 40% reduction

Expected bad-hire cost today = 0.125 × $150,000 × 10 = $187,500/yr
Avoided (40% fewer)          = $187,500 × 0.40        = $75,000/yr
```

**Formula C: Time-to-hire compression (frame, don't over-claim)**
> "You said time-to-hire is [X] days. If pre-vetting removes the human-screen bottleneck on [A×s] candidates per req, the constraint moves off your engineers' calendars. I won't put a dollar on that today, but you know what a roadmap slipping [X] days costs better than I do."

**How to say it:**
> "These are *your* numbers, and they're illustrative, not a Roundz guarantee, and the cost figures come from industry research like SHRM and the US Department of Labor. But even on conservative inputs you're looking at roughly **$[54K] in recovered engineering time plus $[75K] in avoided bad hires**. That's the size of the prize. The only honest way to find out your *real* number is to run it on one req. Which brings me to what I'd propose."

---

### 2g. Ask for the Sale (~3 min): propose the one-req priced pilot, book the date

Don't soften it into a "next steps" mush. Make a specific proposal and go quiet.

> "Here's what I'd suggest. Let's run a **paid pilot on [the specific req: e.g. your Senior Backend role]**. Roundz screens every applicant to that req end-to-end, including the agentic-coding round, and hands your engineers only the pre-vetted top ~20% with the explainable reports you just saw. Pricing for a single-req pilot is **[$___]**.
>
> You keep full control, your engineers make every final call. We measure it against exactly what you'd expect today: engineer hours spent, quality of who reaches the onsite, time-to-fill.
>
> If it works, we talk about the rest of your reqs. If it doesn't, you've spent [$___] and a couple weeks to find out, and I've earned an honest 'no.'
>
> Can we start it on **[propose a date: e.g. Monday the 4th]**?"

Then **stop talking.** Let them answer.

- If **yes** → book it in the calendar *on the call*: "Great, I'll send a calendar invite for a 20-minute kickoff [date/time] and the pilot agreement today. Who owns the req on your side so I loop them in?"
- If **"need to check budget/team"** → pin it: "Totally fair. What specifically do you need to confirm, and can we hold **[date]** tentatively so we don't lose two weeks to scheduling? I'll send everything you need to get the internal yes."
- If **no** → "Appreciate the honesty. What would have to be different for this to be a yes?" (Learn, and keep the door open.)

---

## 3. Challenger Moves: where to teach & reframe

The whole call has ONE teaching moment; everything else supports it.

- **The teach (deliver at the mirror-back, §2d):** *"The job changed. Coding screens measure 'can you produce correct code', but AI produces correct code for free now. The skill that's now scarce and valuable is **directing AI well**: decomposing, judging, catching where the model is wrong. Your current screen tests a commodity skill; nobody's screen tests the scarce one."*
- **Reinforce it at Section 3**: the agentic round is the physical proof of the teach.
- **Reframe "AI interviewing feels impersonal"** → "The impersonal part today is a take-home nobody reads and a rushed 45-minute screen. This gives every candidate the *same* rigorous conversation and gives your engineers their time back for the people who earned it."
- **Reframe "we already have HackerRank/CoderPad"** → "Right, and you told me you still re-verify in the onsite because you don't fully trust the score. That's the tell that it's measuring the wrong thing. This measures the thing you're actually re-verifying for."
- **Take-away close (use sparingly):** "Honestly, if you're not seeing candidates game your screen with AI yet, you may not need this for another quarter. When you do start seeing it, and you will, this is what fixes it."

---

## 4. Objection Redirects Inside the Demo (short: full library lives elsewhere)

Keep these to one or two sentences and get back to the demo. Point to the full objection-handling doc for depth.

- **"Does the AI make the hiring decision?"** → "No. We filter; your engineers decide. You only ever meet the pre-vetted top ~20%." *(Section 6.)*
- **"How do I know it's not just running my tests?"** → "It isn't, it evaluates approach, complexity, and correctness of reasoning, and the report shows its evidence." *(Section 4.)*
- **"Candidates will cheat with AI."** → "In the coding round we proctor for it; in the agentic round we *hand* them the AI on purpose and score how they direct it, cheating isn't a concept there." *(Sections 5 + 3.)*
- **"Is this biased / defensible?"** → "It's rubric-based, level-aware, and every score is explainable and evidence-backed, more consistent than five different engineers with five different bars." *(Section 4.)*
- **"Where's my candidate data / security?"** → "Fair question, let me get you our data handling one-pager and loop in whoever you need; I won't wing security on this call." *(Redirect to security doc; don't improvise.)*
- **"What if a great candidate interviews badly with a bot?"** → "That's exactly why humans stay in the loop, borderline verdicts still go to your engineers; we're removing the obvious no's, not auto-rejecting maybes."

> For pricing pushback, ROI skepticism, and competitor teardowns, use the full objection-handling playbook (separate doc).

---

## 5. Post-Call Follow-Up Template

Send within an hour, while it's warm. Recap in *their* language, restate the number, confirm the booked next step.

**Subject:** Roundz pilot on [Req name], recap + kickoff [date]

> Hi [Name],
>
> Thanks for the time today. Quick recap so we're aligned:
>
> **What you're solving:** [their pain in their words, e.g. ~200 applicants a req, engineers losing ~60 hours a month to screens you don't fully trust, and AI making "code that runs" a weak signal].
>
> **What we agreed to try:** a paid pilot on **[the specific req]**: Roundz screens every applicant end-to-end, including the agentic-coding round, and hands your engineers only the pre-vetted top ~20% with explainable, level-aware reports. Your team makes every final call.
>
> **The prize (your numbers, illustrative):** ~$[54K]/yr in recovered engineering time and ~$[75K]/yr in avoided bad hires. Cost figures are from industry research (SHRM / US DoL); the pilot will produce your real numbers.
>
> **Next step:** kickoff on **[date/time]**: invite attached. Pilot agreement attached as well. [Owner name] is looped in on the req.
>
> Anything you need from me before [date] to get the internal green light? Happy to jump on a 10-minute call with [budget owner / security] if useful.
>
> [Your name] · roundz.ai

**If they didn't commit to the pilot, swap the last block:**
> **Open item:** you're confirming [budget / team buy-in] by [date]. I've held [pilot start date] tentatively. Here's the one-pager for your internal conversation: [link]. I'll check back [day].

---

### Facilitator reminders (for you, not the buyer)
- Discovery earns the demo. Never demo before the mirror-back "yes."
- Every section = one pain + one micro-yes. No feature tours.
- The agentic round is the wedge, protect its time and run it live (it's demoable); it's the one thing on the call no competitor can show.
- Compute ROI in *their* numbers, live, labeled illustrative; label every industry stat as industry research.
- Never claim code execution, test pass rates, or invent customers.
- Leave with a booked pilot date or a crisp reason why not.
