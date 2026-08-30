---
name: voc-messaging-starter
description: >
  Configurable starter for a monthly Voice-of-Customer messaging automation. Pulls a month of
  PROSPECT discovery/intro calls from a call-recording tool, drops current customers via CRM,
  extracts pains, buying triggers, must-have outcomes and verbatim prospect quotes
  (verbatim-validated, never paraphrased), then synthesises POV pillars, problem-to-value ladders,
  and hook headlines in the customer's own words, plus a one-page messaging sheet. THIS IS A
  TEMPLATE: fill in the CONFIG block and complete the VERIFY checklist before first use.

  Use when someone says: "run the VOC messaging report", "monthly voice of customer", "turn our
  prospect calls into messaging / pillars / hooks", "customer voice messaging", or a monthly
  scheduled task fires it. Read the companion playbook first if you haven't configured it yet.
---

# VOC Messaging — Starter (configure before use)

Turns a month of prospect calls into customer-grounded messaging. Read this whole file once and
fill in CONFIG before running. The core rule is non-negotiable:

**Quotes are LIFTED, never AUTHORED.** The model selects candidate quotes; a script validates each
is an exact substring of a raw transcript; failures are dropped, never reworded. This is enforced
in `scripts/validate_quotes.py`. Do not skip it.

---

## CONFIG — fill this in (everything company-specific lives here)

```
# --- Call-recording tool (Gong / Chorus / Fathom / etc.) ---
CALL_TOOL                = <name of your connected call tool>
CALL_LIST_SUPPORTS       = <which filters its list/search actually supports: date? title? participant?>
                           # TEST THIS with real calls before relying on it — see VERIFY step 1.
TRANSCRIPT_HAS_TIMESTAMPS = <true|false>   # if false, locator = title + speaker, NOT a timecode

# --- How prospect discovery/intro calls are identified (by call TYPE, not by rep) ---
INCLUDE_TITLE_KEYWORDS   = [<e.g. Intro, Demo, Discovery, Walkthrough, Evaluation, POC>]
EXCLUDE_TITLE_KEYWORDS   = [<e.g. Sync, Check-in, QBR, Renewal, Onboarding, CSM, Support>]
MIN_DURATION_SECONDS     = 300            # drop no-shows / reschedules

# --- CRM (Salesforce / HubSpot / etc.) customer filter ---
CRM                      = <name of your connected CRM>
CUSTOMER_TEST            = <the field+value that marks a current customer — VERIFY, don't assume>
                           # e.g. Account.Lifecycle_Stage__c = 'Customer' OR Account.Owner is a CS profile.
                           # On some orgs the "obvious" field (e.g. Account.Type) is null — check.

# --- Run controls ---
MAX_CALLS                = 30             # context-window ceiling; raise cautiously
WINDOW                   = last full calendar month, in <YOUR_TIMEZONE>
TARGET_QUOTES            = 15             # aspirational; output fewer rather than paraphrase

# --- Delivery ---
DELIVER_TO               = <your own DM / a private channel — NOT a shared channel>
NEVER_POST_TO            = any shared/public channel without explicit human action
```

---

## VERIFY — do these ONCE before the first real run (do not skip)

1. **Call-tool filters.** Make 2-3 real calls to your call tool's list/search. Confirm what it
   actually filters on (date, title keyword, participant). Note whether transcripts include
   timestamps and whether participant data is populated. Set CALL_LIST_SUPPORTS and
   TRANSCRIPT_HAS_TIMESTAMPS from what you observe, not what the docs claim.
2. **Title convention.** Pull a month of call titles. Confirm INCLUDE/EXCLUDE keywords match how
   your team actually names discovery vs. CS calls. Adjust the sets.
3. **Customer field.** Query a few known-customer and known-prospect accounts. Find what actually
   distinguishes them. Set CUSTOMER_TEST to the confirmed field+value. Test that it drops a known
   customer and keeps a known prospect.
4. **Supervised dry run.** Run once on last month with a human watching. Read the entire output.
   Check the coverage line and the unclassified-title tail. Tune, then update this file's CONFIG.

Until all four are done, treat outputs as drafts, not truth.

---

## Workflow

### Step 1 — Retrieve prospect calls
Query CALL_TOOL for WINDOW. Run once per INCLUDE_TITLE_KEYWORD (list actions usually match one
keyword at a time), union and dedupe by call id. Drop any title containing an EXCLUDE keyword.
Drop calls under MIN_DURATION_SECONDS. Separately, list the whole window unfiltered and record any
call matching neither include nor exclude as "unclassified (review)" — this is your blind-spot guard.

### Step 2 — Drop current customers (CRM)
Extract each call's company from the title. Batch-look-up in CRM. Drop any matching CUSTOMER_TEST;
list them in the appendix with the reason. On a fuzzy name miss (title company != CRM name), KEEP
and flag — never hard-drop on a miss.

### Step 3 — Substance-rank and cap
Sort survivors by duration desc; take top MAX_CALLS. Report coverage in every output:
`Analysed N of M substantive prospect calls (window). Cap = MAX_CALLS.` List the rest.

### Step 4 — Per-call extraction
For each capped call, get its transcript, then extract a COMPACT record and keep only that:
`{ call_id, title, company, pains[], triggers[], outcomes[],
   quote_candidates:[{speaker, text (EXACT transcript substring), theme}] }`
Attribute pains/triggers/outcomes to the PROSPECT, not your rep. Copy quote text exactly — no
cleanup, no merging turns, no grammar fixes. Write records to /tmp/voc_records.json.

### Step 5 — Verbatim validation (hard gate)
Run `scripts/validate_quotes.py --records /tmp/voc_records.json --transcripts <dir of raw
transcripts named <call_id>.txt>`. Only exact-substring passes are eligible. Drop failures; never
reword. If fewer than TARGET_QUOTES survive, output what survived and say so.

### Step 6 — Synthesise (from records + validated quotes only)
Top pains (ranked, with call counts) · buying triggers · must-have outcomes ·
TARGET_QUOTES verbatim quotes with company+speaker locators · 3 POV pillars ·
problem-to-value ladder per pillar (NO proof rung — proof isn't in prospect calls; don't
fabricate metrics) · 5 hook headlines per pillar in the customer's language · a one-page sheet.
Every claim traces to a record.

### Step 7 — Output & deliver
Produce: (1) a one-page messaging sheet (markdown), (2) an evidence appendix (spreadsheet: quotes
with locators, per-call signal, ranked lists, coverage + unclassified tail), (3) a short
Slack/email-ready summary. Deliver to DELIVER_TO. NEVER post to NEVER_POST_TO without explicit
human action. In an interactive run, confirm before sending; in a scheduled run, the private
destination is the approved one.

---

## Scheduling

If your scheduler has monthly/custom-cron: run on the 1st or 2nd of the month.
If it only offers daily/weekly: set WEEKLY on a fixed weekday and open the instructions with a
date guard — "If today's day-of-month > 7, STOP and do nothing; only proceed on the first
occurrence of this weekday each month." Exactly one such weekday exists per month.
Permissions: auto-approve is safe only while the sole write action is a DM to yourself. If you
widen delivery, switch to manual approval.

---

## Known traps (see the playbook for detail)
- Fabricated quotes → the verbatim gate exists for this. Never trust an unvalidated quote.
- Rep-vs-prospect attribution → the gate proves a quote is real, not who said it. Eyeball it.
- Missing timestamps / empty participant data → design around what your tool actually returns.
- Fuzzy company-name matches → keep-and-flag, never hard-drop.
- Context limits → cap calls, rank by substance, report coverage.
