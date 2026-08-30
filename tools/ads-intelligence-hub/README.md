# Ads Intelligence Hub — App Logic

*Generic version — no company data. Replace every `[placeholder]` with your own product's
values before use. The rule architecture and design decisions are the reusable part; the
specific thresholds and integrations below are illustrative only.*

## Overview

Three independent modules. Each takes file or text input, runs deterministic rules and/or AI, and returns actionable output. All AI calls go through a backend route to Claude (Sonnet 4.6). All file parsing supports CSV and Excel (.xlsx/.xls).

---

## Module 1 — Performance Intelligence

### Input
Google Ads export (CSV or Excel) with these columns:
`Date · Campaign · Ad Group · Keyword · Match Type · GEO / Region · Budget · Spend · Impressions · Impression Share · Clicks · CTR · MQLs · MQL CVR · Cost/MQL`

Column names are normalised to lowercase + underscores before mapping, so `Cost/MQL`, `Cost Per MQL`, and `cost_mql` all resolve to the same field.

### Step 1 — Rule Engines

Each row is tested against four rules in order. The first matching rule wins.

**Calibrate before use:** every dollar/percentage threshold below is a placeholder. Set them
from your own target CAC per region and your own paid-search benchmarks — they should not
be copied as-is.

#### Rule 1 — Region A Poor Performance (e.g. a price-sensitive or emerging market)
**Applies when:** GEO = Region A AND Spend > `[SPEND_THRESHOLD_A]`

| Condition | Flag | Action |
|---|---|---|
| MQLs = 0 | 🔴 Red | Pause keyword — zero MQLs despite spend |
| Cost/MQL > `[CPA_THRESHOLD_A]` AND CVR < `[CVR_FLOOR]` AND CTR > `[CTR_CEILING]` | 🔴 Red | Review LP / intent mismatch (high CTR, low CVR) |
| Cost/MQL > `[CPA_THRESHOLD_A]` AND CVR < `[CVR_FLOOR]` | 🔴 Red | Review ad copy + keyword relevance |
| Cost/MQL > `[CPA_THRESHOLD_A]` | 🟡 Amber | Monitor / keep with bid cap |

#### Rule 2 — Region B Poor Performance (e.g. a mature/enterprise market)
**Applies when:** GEO = Region B AND Spend > `[SPEND_THRESHOLD_B]`

| Condition | Flag | Action |
|---|---|---|
| MQLs = 0 | 🔴 Red | Pause keyword — zero MQLs despite spend |
| Cost/MQL > `[CPA_THRESHOLD_B]` AND CVR < `[CVR_FLOOR]` AND CTR > `[CTR_CEILING]` | 🔴 Red | Review LP / intent mismatch |
| Cost/MQL > `[CPA_THRESHOLD_B]` AND CVR < `[CVR_FLOOR]` | 🔴 Red | Review ad copy + keyword relevance |
| Cost/MQL > `[CPA_THRESHOLD_B]` | 🟡 Amber | Monitor / keep with bid cap |

#### Rule 3 — SQR (Search Query) Analysis
**Applies when:** Spend > `[MIN_SPEND_TO_REVIEW]` AND CTR > `[CTR_CEILING]` AND MQLs < 1

| Condition | Flag | Action |
|---|---|---|
| MQLs = 0 | 🔴 Red | Negate search term — zero MQLs |
| MQLs > 0 but < 1 | 🟡 Amber | Review LP/ad copy — relevant but not converting |

*High CTR means the ad is being clicked, but no conversions — signals a landing page or intent problem.*

#### Rule 4 — GEO Analysis
**Applies when:** Spend > `[MIN_SPEND_TO_REVIEW]` AND CTR < `[CTR_CEILING]` AND CVR < `[CVR_FLOOR]`

| Condition | Flag | Action |
|---|---|---|
| MQLs = 0 | 🔴 Red | Exclude or reduce spend in this GEO |
| Impressions > `[IMPRESSION_THRESHOLD]` | 🟡 Amber | Review ad copy localisation — high impressions, low engagement |
| All other | 🔴 Red | Reduce GEO bid / deprioritize region |

*Low CTR + low CVR means the ad isn't resonating in this region at all.*

### Step 2 — AI Recommendations

After rule flagging, all flagged rows are sent to Claude in a single batch call. Claude returns a 1–2 sentence specific action for each row (exact action: pause, bid cap, negate, etc. + brief reason).

**Prompt structure:**
- System: "Senior paid search strategist. Give specific 1-2 sentence actionable recommendation per row."
- User: Structured summary of each flagged row with all metrics + rule + flag detail
- Max tokens: 2000

### Step 3 — Summary Dashboard

Four aggregate metrics displayed above the results table:
- **Total Spend Flagged** — sum of `spend` across all flagged rows
- **Keywords to Pause** — count of rows where AI recommendation contains "pause"
- **Budget at Risk** — sum of `budget` across all flagged rows
- **GEOs Under-performing** — count of unique GEO values in flagged rows

---

## Module 2 — Ad Copy Generator

### Input
Ad copy export (CSV or Excel) with these columns:
`Campaign · Ad Group · GEO · Keyword Theme · Headline 1/2/3 · Description 1/2 · Final URL · Notes`

Multiple column name formats are supported (e.g. `Headline 1`, `Headline1`, `H1`, `Head_1` all map to `headline1`).

### Step 1 — Background Buyer-Intelligence Fetch

When a GEO is selected (or on page load with a default region), the app immediately fires a background request to a buyer-intelligence endpoint for that GEO.

This request:
1. Checks a cache (e.g. Vercel Blob) for a result less than 24 hours old — returns instantly if found
2. If cache miss, calls your call-intelligence vendor's API (e.g. `https://[your-call-intel-vendor].example/api/chat`) with a GEO-specific prompt asking for the top 5 buyer pain points from your own discovery calls and CS conversations
3. Stores the result in cache for 24 hours

**This runs silently in the background.** Generate never waits for it — it uses whatever landed, or proceeds without it if the vendor didn't respond in time.

### Step 2 — Claude Rewrite

When the user clicks Generate, Claude rewrites each ad group's copy for the selected GEO.

**System prompt includes:**
- GEO context (e.g. "Region B enterprise buyers — emphasize ROI, [your key integrations], enterprise scale")
- Buyer intelligence, if available: real pain-point language from prospect calls, injected verbatim
- Hard character limits: headlines ≤ 30 chars, descriptions ≤ 90 chars

**User prompt:** Structured summary of all ad groups with existing copy, requesting a raw JSON array back with rewritten headlines and descriptions.

**Max tokens:** 2000

### Step 3 — Character Limit Enforcement

After Claude responds, every field is passed through a post-processing trim:
- If a headline exceeds 30 characters, it is trimmed at the nearest word boundary below 30
- If a description exceeds 90 characters, it is trimmed at the nearest word boundary below 90

This ensures output is always upload-ready, even if Claude miscounts.

### GEO Contexts

Fill in with your own product's real positioning per region. Example shape:

| GEO | Buyer Profile |
|---|---|
| Region A | Enterprise buyers — value, local compliance, reliability, cost efficiency |
| Region B | Enterprise buyers — ROI, speed, [your key integrations], enterprise scale |
| Region C | Enterprise buyers — global compliance, multi-region support, enterprise-grade reliability |

---

## Module 3 — LP Title Generator

### Input
- **Keyword** — the Google Ads keyword to optimise for
- **GEO** — one of your configured regions

### Logic

Single Claude call. No file upload required.

**System prompt:** Google Ads landing page specialist focused on Quality Score optimisation. Instructed to apply these five principles:
1. Include the exact keyword in the title
2. Match searcher intent precisely — informational vs. transactional
3. Use power words that signal value or urgency without clickbait
4. Keep it under 70 characters so it doesn't truncate in SERPs
5. Front-load the keyword — Google weights the first 3 words most heavily

**Output:** Five candidate hero titles, each with:
- The title text
- Character count
- A brief note on which Quality Score principle it applies

**Max tokens:** 800

---

## Data Flow Summary

```
Module 1: CSV/Excel → Column normalisation → Rule 1→2→3→4 → Flagged rows → Claude batch → Recommendations + Dashboard

Module 2: CSV/Excel → Column normalisation → [Background: buyer-intel fetch → cache]
          → Generate clicked → Claude rewrite (with or without buyer-intel context) → Post-process char trim → Results

Module 3: Keyword + GEO → Claude → 5 Quality Score-optimised titles
```

---

## Key Thresholds Reference

All values are placeholders — replace with your own calibrated numbers.

| Rule | GEO | Spend Threshold | Cost/MQL Threshold |
|---|---|---|---|
| Rule 1 | Region A | > `[SPEND_THRESHOLD_A]` | > `[CPA_THRESHOLD_A]` |
| Rule 2 | Region B | > `[SPEND_THRESHOLD_B]` | > `[CPA_THRESHOLD_B]` |
| Rule 3 | Any | > `[MIN_SPEND_TO_REVIEW]` | — |
| Rule 4 | Any | > `[MIN_SPEND_TO_REVIEW]` | — |

Rule 3 triggers on: CTR > `[CTR_CEILING]` + MQLs < 1 (high click engagement, no conversion)
Rule 4 triggers on: CTR < `[CTR_CEILING]` + CVR < `[CVR_FLOOR]` (low engagement across the board)
