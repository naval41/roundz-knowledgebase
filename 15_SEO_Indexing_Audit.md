# SEO & Indexing Audit — roundz.ai

**Date:** 2026-08-08
**Analyst:** Claude (Opus 5)
**Data sources:** Live site crawl (curl) + Google Search Console (`sc-domain:roundz.ai`)
**GSC access note:** The property lives under **connect.roundz@gmail.com**, *not* `vivek.pujara199@gmail.com` (that account has zero properties). Use the Roundz account when checking.

---

## 0. Executive Summary

**Indexing is not broken. Discovery and crawl-budget allocation are.**

roundz.ai ranks #1 for its exact brand name (58% CTR on "roundz ai"). The technical SEO foundation — robots.txt, canonicals, meta robots, JSON-LD, HTTPS canonicalization, TTFB — is genuinely well built. The problem is that **432 blog posts have never been crawled**, and the site is actively wasting Googlebot's crawl allowance on login-wrapped URLs.

| Metric (last 90 days) | Value |
|---|---|
| Indexed pages | **128** |
| Not indexed | **642** |
| Impressions | 11.3K |
| Clicks | **124** |
| CTR | 1.1% |
| Avg position | 10.1 |
| Sitemap submitted | **Jul 30, 2026** (only 9 days before audit) |
| Sitemap URLs discovered | 542 |

**77 of 124 clicks are people typing the brand name.** Non-brand organic acquisition is effectively zero.

---

## 1. What Is Already Correct — Do Not Change

Verified by direct crawl. These are working; no work required.

| Check | Status | Evidence |
|---|---|---|
| robots.txt | Correct | Allows `/`, blocks only auth/dashboard paths, includes `Sitemap:` directive |
| sitemap.xml | Valid | 542 URLs, fresh `lastmod`, GSC status "Success" |
| Meta robots | Correct | `index, follow` on every page checked |
| Canonicals | Correct | Self-referencing and accurate on `/`, `/blog/*`, `/company/*`, `/companies`, `/open-jobs`, `/faq`, `/about-us` |
| HTTP → HTTPS | Correct | 301 via awselb |
| www → apex | Correct | 308 to `https://roundz.ai` |
| TTFB | Good | 0.10s–0.49s across pages |
| JSON-LD | Rich | Organization, WebSite, FAQPage, HowTo, BlogPosting, BreadcrumbList, AggregateRating, ItemList, Person |
| Blog post SSR | Good | Sample post rendered 17,420 chars of server-side text |
| AI crawler policy | Deliberate | GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot explicitly allowed |

---

## 2. Findings

### F1 — `/login?redirectTo=` internal links are burning crawl budget
**Severity: CRITICAL — fix first**
**Source: Website (our bug)** · **52 pages affected**

GSC "Blocked by robots.txt" contains almost exclusively login-wrapped versions of public content:

```
https://roundz.ai/login?redirectTo=/blog/json-vs-toon-vs-yaml-ai-era
https://roundz.ai/login?redirectTo=/blog/cdn-design-evaluation-complete-guide-building-high-performance-content-delivery-networks
https://roundz.ai/login?redirectTo=/blog/strong-vs-eventual-consistency-in-scalable-systems
https://roundz.ai/login?redirectTo=/company/intuit
https://roundz.ai/login?redirectTo=/company/carwale
https://roundz.ai/login?redirectTo=/jobs/roundz-ai/software-development-engineer-entry-1779855943851
https://roundz.ai/login?redirectTo=/candidate
```

The app renders `href="/login?redirectTo=<public-url>"` for gated CTAs. Googlebot follows these, hits `Disallow: /login`, and dead-ends. On a domain with a fresh, limited crawl allowance, this is directly competing with the 432 uncrawled blog posts for Googlebot's attention.

Also present: `https://www.roundz.ai/signup` — something still emits `www`-prefixed absolute links despite the 308 redirect being in place.

**Root cause hypothesis:** an auth-guard wrapper component or a `requireAuth` link helper that builds the login URL at render time instead of at click time.

---

### F2 — 432 blog posts discovered but never crawled
**Severity: CRITICAL**
**Source: Google systems** · **432 pages**

Every URL in *Discovered – currently not indexed* shows **Last crawled: N/A**. Examples:

```
/blog/ai-agents-agentic-workflows
/blog/ai-governance-the-wild-west-is-getting-sheriffs-finally
/blog/apis-idempotency-your-secret-weapon-against-chaos
/blog/back-of-the-envelope-calculations-resource-estimation-guide
/blog/back-of-the-envelope-calculations-secret-weapon-system-designer
/blog/building-apis-that-actually-scale-7-hard-learned-lessons-from-the-trenches
/blog/building-bulletproof-distributed-cache-systems-deep-dive-modern-architecture
/blog/caching-at-scale-why-your-app-needs-more-than-just-redis
/blog/client-side-error-monitoring
/blog/cloudflare-outage-broke-28-percent-internet
```

The GSC chart shows this as a single vertical step around **Jun 12, 2026**, flat ever since — a large content batch published at once with insufficient crawl signal to pull Googlebot through it.

**Contributing factors:**
- Sitemap only submitted Jul 30 (9 days before audit) — some of this may resolve on its own
- `/blog` index page exposes only **6** post links in raw server HTML (verified by grep) — there is no crawl path from the indexed pages to the other ~426
- F1 is stealing the crawl budget that would otherwise reach them

**Note:** This *contradicts* an earlier hypothesis that `/company/*` thin pages were the main problem. They are not. The uncrawled block is the blog.

---

### F3 — Only 6 blog post links in server-rendered `/blog`
**Severity: HIGH**
**Source: Website (our bug)**

```
curl -sL https://roundz.ai/blog | grep -oE 'href="/blog/[^"]+"' | sort -u
# returns 6 results
```

Pagination and the rest of the archive are client-side only. There is no server-rendered crawl path from `/blog` to the other ~426 posts. This is the direct mechanical cause of F2's "N/A last crawled."

---

### F4 — Server errors and 404s suppressing sitewide crawl rate
**Severity: HIGH**
**Source: Website (our bug)** · **2 × 5xx, 8 × 404**

Small absolute numbers, but Googlebot throttles crawl rate across an *entire host* when it encounters 5xx. With only 128 pages indexed and 432 waiting, we cannot afford any crawl-rate suppression.

---

### F5 — Brand name collision with "rounds"
**Severity: HIGH (strategic, slow to fix)**

| Query | Clicks | Impressions |
|---|---|---|
| roundz ai | **63** | 108 |
| roundz | 11 | 314 |
| roundz.ai | 3 | 5 |
| roundz app | 1 | 54 |
| round z | 1 | 34 |
| round ai | 1 | 20 |
| **rounds ai** | **0** | **603** |
| byjus | 0 | 456 |
| cdn architecture | 0 | 80 |
| epifi | 0 | 77 |

Our single highest-impression query, **"rounds ai" (603 impressions), earns zero clicks.** Google normalizes "roundz" → "rounds," putting us against:

- **rounds.so** — a direct competitor, also AI-native hiring
- **joinrounds.com** — Rounds AI, medical AI for clinicians
- **Rounds AI Ltd** — Tel Aviv, mobile assets (Preqin/Crunchbase profiles rank)
- **Senator Mike Rounds** — publishes AI-policy press releases on a `.senate.gov` domain

Third-party profiles (Crunchbase, LinkedIn) currently rank for our brand terms and are not ours.

---

### F6 — Company pages generate impressions but zero clicks
**Severity: MEDIUM**
**394 URLs in sitemap**

`byjus` = 456 impressions / 0 clicks. `epifi` = 77 / 0. So `/company/*` pages *do* surface — they just rank too deep to earn a click.

Verified `/company/amazon`: ~1,576 chars server-rendered, and the meta description is a generic corporate encyclopedia blurb about Amazon's e-commerce and AWS business — **nothing about interviewing at Amazon.** We are targeting the wrong intent entirely.

This partially rehabilitates these pages as an asset (they rank for something), but they are worthless in their current form.

---

### F7 — Open Graph tags hardcoded to homepage on subpages
**Severity: MEDIUM**
**Source: Website (our bug)**

`/blog`, `/companies`, `/about-us`, `/faq` all emit the **homepage's** `og:title`, `og:description`, and `og:url`:

```html
<!-- served on https://roundz.ai/blog -->
<meta property="og:title" content="AI Voice Interviews &amp; Hiring Platform | Roundz"/>
<meta property="og:url" content="https://roundz.ai"/>
```

Note `<title>` and `<meta name="description">` *are* correct per-page — only the OG block is stale. Every social share of a blog post presents as a homepage share. This also degrades LLM attribution, which matters given we explicitly allowlist GPTBot/ClaudeBot/PerplexityBot.

`/open-jobs` is the one page with correct OG — use it as the reference implementation.

---

### F8 — Empty `<h1>` in server HTML
**Severity: MEDIUM**
**Source: Website (our bug)**
**Affected: `/blog`, `/about-us`, `/faq`**

```html
<h1 class="mb-6 text-4xl font-bold leading-tight md:text-4xl lg:text-5xl">
```

The tag renders with no text content server-side; the heading is injected client-side. Google does render JS, but it's a deferred queue, not a guarantee.

---

### F9 — Thin server-rendered listing pages
**Severity: MEDIUM**

| Page | Server-rendered text |
|---|---|
| `/open-jobs` | 524 chars |
| `/faq` | 827 chars |
| `/companies` | 902 chars |
| `/about-us` | 1,852 chars |
| `/company/amazon` | 1,576 chars |
| `/blog/progressive-disclosure-...` | **17,420 chars** |

Blog posts are properly SSR'd. Product and listing pages are client-rendered shells.

---

### F10 — CTR crisis at position 10.1
**Severity: MEDIUM**

11.3K impressions → 124 clicks (1.1%) at average position 10.1. We are reaching page-one visibility for 408 queries and converting almost none of it. Expected CTR at position ~10 is roughly 2–3%; we're at a third of that.

---

### F11 — Duplicate / canonical noise
**Severity: LOW**

- Duplicate without user-selected canonical: 9
- Alternate page with proper canonical tag: 9
- Page with redirect: 15
- Excluded by 'noindex': 8
- Indexed though blocked by robots.txt: 3

Small counts, likely mostly intentional, but worth a pass once the big items ship.

---

## 3. Fix Plan

### Phase 1 — Stop the bleeding (target: this week)

#### Fix 1.1 — Remove `/login?redirectTo=` from rendered `href` attributes → *addresses F1*
**Where:** auth-guard link component / `requireAuth` link helper

- Find every place a link is rendered as `/login?redirectTo=<target>`. Search the frontend repo for: `redirectTo`, `?redirectTo=`, `/login?`.
- Change the pattern so the anchor's `href` is **always the canonical public URL**. Handle the auth gate in the click handler / route guard, not in the markup.
  ```jsx
  // before
  <a href={isAuthed ? url : `/login?redirectTo=${url}`}>

  // after
  <a href={url} onClick={e => { if (!isAuthed) { e.preventDefault(); router.push(`/login?redirectTo=${url}`); } }}>
  ```
- If any gated link genuinely must stay, add `rel="nofollow"` as a stopgap — but the `href` fix is the correct solution.
- Audit for `www.roundz.ai` absolute URLs anywhere in the codebase; all internal links should be root-relative or use the apex host.

**Verify:** `curl -sL https://roundz.ai/blog | grep -c 'redirectTo'` should return 0. Repeat for `/companies`, `/company/<slug>`, `/open-jobs`.

#### Fix 1.2 — Resolve the 2 × 5xx and 8 × 404 → *addresses F4*
- Export the URL lists from GSC → Pages → each reason → EXPORT.
- 5xx: fix the underlying error. Non-negotiable — this throttles crawl rate hostwide.
- 404: either restore, 301 to the correct target, or remove from sitemap and internal links.

**Verify:** GSC → Pages → "Validate Fix" on both reasons.

#### Fix 1.3 — Manually request indexing for top blog posts → *addresses F2*
Not a code change. In GSC → URL Inspection, submit the 10–15 highest-value posts individually. Do this **after** Fix 1.1 ships so the recrawl sees a clean link graph.

---

### Phase 2 — Open the crawl path (target: next 1–2 weeks)

#### Fix 2.1 — Server-render the full blog archive → *addresses F2, F3*
**This is the highest-value structural change.**

- `/blog` must expose real `<a href="/blog/...">` links in the **server HTML**, not client-side only.
- Add server-rendered pagination (`/blog/page/2`, `/blog/page/3`, …) with crawlable prev/next links, or a `/blog/archive` page listing every post.
- Add server-rendered tag/category hubs (e.g. `/blog/tag/system-design`, `/blog/tag/caching`) — these create multiple crawl paths per post and are strong topical-authority signals.
- Add "related posts" links, server-rendered, at the bottom of every post.

**Verify:** `curl -sL https://roundz.ai/blog | grep -oE 'href="/blog/[^"]+"' | sort -u | wc -l` should be ≫ 6.

#### Fix 2.2 — Route internal link equity into the blog → *addresses F2*
The 128 indexed pages are crawled recently (`/`, `/groups`, `/community`, `/book-interview`, `/about-us`, `/company/goldman-sachs`, `/jobs/*` all crawled Aug 3–5). That is live crawl equity currently going nowhere.

- Add a server-rendered "Latest from the blog" block on the homepage.
- Cross-link `/company/<slug>` → relevant blog posts, and `/community` / `/groups` → blog.

#### Fix 2.3 — Verify sitemap completeness → *addresses F2*
Sitemap lists **98** blog URLs but GSC discovered **432** blog URLs. The sitemap is incomplete.

- Ensure sitemap generation enumerates *all* published posts.
- Consider splitting into a sitemap index: `sitemap-pages.xml`, `sitemap-blog.xml`, `sitemap-companies.xml`, `sitemap-jobs.xml`. Easier to diagnose per-section coverage in GSC.
- Drop `priority` and `changefreq` — Google ignores both. Keep accurate `lastmod`.

---

### Phase 3 — Make the traffic convert (target: weeks 3–4)

#### Fix 3.1 — Per-page Open Graph tags → *addresses F7*
Use `/open-jobs` as the reference — it's already correct. Propagate per-route `og:title` / `og:description` / `og:url` / `og:image` to `/blog`, `/blog/*`, `/companies`, `/company/*`, `/about-us`, `/faq`. `og:url` must equal the canonical.

**Verify:** `curl -sL https://roundz.ai/blog | grep 'og:url'` → must show `/blog`, not the apex.

#### Fix 3.2 — Server-render `<h1>` text → *addresses F8*
`/blog`, `/about-us`, `/faq` — move heading text into the server payload.

#### Fix 3.3 — Rewrite `/company/*` for interview intent → *addresses F6, F9*
The single biggest content-quality change.

- **Retarget:** "Amazon interview questions", "Amazon system design interview", "Amazon interview process" — **not** Amazon's corporate profile.
- **Rewrite meta descriptions.** Current ones are generic company encyclopedia text. They must describe the *interview content on our page*.
- **Server-render** the interview experiences, question lists, and round breakdowns.
- **Triage the 394.** Keep and invest in the ~20–40 with real user-contributed content. `noindex` the rest until they have substance, and remove them from the sitemap — a thin page that ranks at position 40 with 0 clicks is a liability, not an asset.

#### Fix 3.4 — Title & description rewrite pass → *addresses F10*
At position 10.1 with 1.1% CTR, the snippet is the bottleneck. Pull the top 50 queries by impression from GSC Performance, map each to its landing page, and rewrite that page's `<title>` and `<meta name="description">` to match the query intent.

#### Fix 3.5 — SSR the listing pages → *addresses F9*
`/open-jobs` (524 chars), `/faq` (827), `/companies` (902) need real server-rendered content.

---

### Phase 4 — Brand & entity (ongoing, months)

#### Fix 4.1 — Own the brand SERP → *addresses F5*
Not a frontend task, but it caps everything else.

- Claim/complete: Google Business Profile, Crunchbase, LinkedIn, G2, Product Hunt.
- Ensure `Organization` JSON-LD on the homepage carries `sameAs` pointing at every owned profile — this is the entity-disambiguation signal that tells Google "Roundz" ≠ "Rounds". *(The Organization schema already exists; verify `sameAs` is populated.)*
- Consider targeting "roundz vs rounds" style disambiguation content.
- Accept that "rounds ai" (603 impressions) is a long fight against a competitor and a sitting US Senator.

#### Fix 4.2 — Canonical/duplicate cleanup → *addresses F11*
Once Phases 1–3 ship, export and review the 9 duplicates, 9 alternates, 15 redirects, 8 noindex, and 3 indexed-though-blocked.

---

## 4. Priority Order for Implementation

| # | Fix | Finding | Effort | Impact |
|---|---|---|---|---|
| 1 | Remove `/login?redirectTo=` from `href` | F1 | S | **Critical** |
| 2 | Fix 5xx + 404s | F4 | S | **Critical** |
| 3 | SSR full blog archive + pagination | F2, F3 | M | **Critical** |
| 4 | Sitemap completeness (98 → all posts) | F2 | S | High |
| 5 | Internal links into blog | F2 | S | High |
| 6 | Request indexing for top posts | F2 | S | High |
| 7 | Per-page OG tags | F7 | S | Medium |
| 8 | Server-render `<h1>` | F8 | S | Medium |
| 9 | Rewrite `/company/*` for interview intent | F6, F9 | L | High |
| 10 | Title/description CTR pass | F10 | M | High |
| 11 | SSR listing pages | F9 | M | Medium |
| 12 | Brand entity / `sameAs` | F5 | L | High (slow) |
| 13 | Canonical cleanup | F11 | S | Low |

---

## 5. Verification Commands

Run after each deploy:

```bash
# F1 — no login-wrapped links in server HTML
for p in "" blog companies open-jobs company/amazon; do
  echo -n "/$p redirectTo count: "
  curl -sL "https://roundz.ai/$p" | grep -c 'redirectTo'
done

# F3 — blog archive crawl path
curl -sL https://roundz.ai/blog | grep -oE 'href="/blog/[^"]+"' | sort -u | wc -l

# F7 — per-page OG
for p in blog companies about-us faq; do
  echo "--- /$p"; curl -sL "https://roundz.ai/$p" | grep -oE '<meta property="og:(title|url)"[^>]*>'
done

# F8 — h1 has text
curl -sL https://roundz.ai/blog | grep -oE '<h1[^>]*>[^<]{1,80}'

# F9 — server-rendered text volume
curl -sL https://roundz.ai/open-jobs -o /tmp/p.html && python3 -c "
import re;h=open('/tmp/p.html',encoding='utf8',errors='ignore').read()
h=re.sub(r'(?is)<(script|style).*?</\1>',' ',h)
print(len(re.sub(r'\s+',' ',re.sub(r'(?s)<[^>]+>',' ',h)).strip()))"

# sitemap blog coverage
curl -sL https://roundz.ai/sitemap.xml | grep -c '<loc>https://roundz.ai/blog/'
```

**GSC checkpoints (weekly):**
- Pages → Indexed count should climb from 128
- Pages → "Discovered – currently not indexed" should fall from 432
- Pages → "Blocked by robots.txt" should fall from 52 toward ~0 non-auth URLs
- Performance → filter *excluding* "roundz" → non-brand clicks should become non-zero

---

## 6. Baseline Snapshot (2026-08-08)

Freeze these to measure against:

```
Indexed:                              128
Not indexed:                          642
  Discovered - currently not indexed: 432
  Crawled - currently not indexed:    107
  Blocked by robots.txt:               52
  Page with redirect:                  15
  Duplicate without user canonical:     9
  Alternate w/ proper canonical:        9
  Excluded by 'noindex':                8
  Not found (404):                      8
  Server error (5xx):                   2
Indexed though blocked by robots:       3

Clicks (90d):        124
Impressions (90d):  11.3K
CTR:                 1.1%
Avg position:        10.1
Total queries:       408
Brand clicks:         77 / 124  (62%)

Sitemap URLs:        542  (394 company, 98 blog, 21 community, 11 groups, 5 jobs-at, 13 static)
Sitemap submitted:   Jul 30, 2026
Sitemap last read:   Aug 7, 2026
```
