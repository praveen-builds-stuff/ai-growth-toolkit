# Building a VOC-Grounded Messaging Automation on Your Own Stack

A practitioner playbook for growth marketers who want to turn a month of sales calls into
customer-language messaging — automatically, and without an AI quietly inventing quotes.

This is the method, not a plug-and-play file. The companion `SKILL.md` gives you the scaffold,
but this document is what makes it work on your stack instead of someone else's.

## What you get, and what it's for

Once a month, pull your prospect calls, extract the pains / buying triggers / must-have outcomes
prospects actually described, lift a set of verbatim quotes, and synthesise them into messaging
pillars, benefit ladders, and hook headlines written in your customers' own words. Output lands
in your DMs for a one-tap forward.

Who it's for: a growth/PMM/demand-gen person with access to a call-recording tool (Gong,
Chorus, Fathom, etc.) and a CRM (Salesforce, HubSpot). No engineering required, but you do
have to do some field-checking on your own stack — see "The discipline that makes it real."

## The one rule everything hangs on: quotes are lifted, never authored

The failure mode that kills these projects is an AI tool emitting a quote that sounds like a
customer but was never said — a paraphrase in quotation marks, a merged sentence, a
plausible invention. Once that lands in a messaging doc, it spreads into ads and decks as if it
were real VOC. I've seen a commercial call-analysis tool do exactly this.

So the non-negotiable design rule: the model may only SELECT quotes, never WRITE them.
Every quote must be validated as an exact substring of a raw transcript before it's allowed into
any output. If a candidate quote can't be found verbatim in the transcript, it is dropped — never
reworded to "make it fit." This is enforced in code (a validation script), not left to the model's
good intentions. Everything else in this playbook is negotiable; this isn't.

## The pipeline (five stages)

1. Retrieve the month's prospect calls.
2. Classify prospect vs. customer (drop the customers).
3. Extract per call: pains, triggers, outcomes, and candidate verbatim quotes.
4. Validate every quote as an exact transcript substring (drop failures).
5. Synthesise into pains/triggers/outcomes, pillars, ladders, hooks, and a one-page sheet.
6. Deliver to yourself; forward manually.

The rest of this doc is the why and the how to adapt for each stage.

## Design decision 1 — Identify prospect calls by call TYPE, not by rep

The intuitive approach is "get the calls run by our SDRs." It's usually the wrong spine, for two
reasons: (a) your roster changes, so any hardcoded list rots; (b) your call tool may not let you
filter by internal participant at all.

Better: filter on what makes a call a prospect discovery call regardless of who ran it. On
most stacks that signal is the call title/type. Discovery and intro calls tend to follow a house
naming convention (e.g. a consistent "Intro | [Us] | [Prospect]" pattern), while customer-success
calls carry different words (sync, check-in, QBR, renewal, onboarding). Filtering on the call-type
keyword captures every prospect call automatically — including ones run by a rep who started
yesterday — and it's cheap, because you only pull the transcripts that match.

**How to adapt:**
- Look at a month of your call titles. Is there a reliable convention for discovery/intro calls?
  Build an INCLUDE keyword set from it and an EXCLUDE set from your CS/internal naming.
- Test what your call tool can actually filter on before you design around it. Specifically:
  can it filter by participant/rep? Many integrations can't (or return empty participant data).
  Can it filter by title keyword? By date? Confirm with a couple of real API calls, don't assume.
- Always log the "unclassified" tail — calls in your window that matched neither include
  nor exclude keywords. Eyeball it each run. This is your guard against a naming
  convention you missed silently dropping real calls.

## Design decision 2 — Classify prospect vs. customer via the CRM, and VERIFY the field

Intro calls are usually new prospects, but "intro to a new module/division" calls can land on
existing customers, and customer language is not prospect language. So cross-check each
call's company against your CRM and drop current customers.

Do not guess the field that marks a customer. On the stack I built this for, the obvious
candidate field was null across the entire org — using it would have filtered nothing. What
actually worked was a combination: a lifecycle-stage field equal to "Customer," OR the account
being owned by a Customer Success profile. Yours may differ. Common real-world markers:

- A lifecycle/stage field ("Customer", "Closed Won", "Active Subscription")
- Account ownership by a CS/CSM profile or role
- Presence of a closed-won opportunity or an active subscription record

**How to adapt:** run one query against a handful of known-customer and known-prospect
accounts and look at what actually distinguishes them. Confirm the field name and the exact
value. Then hard-drop on it. Treat "this field marks a customer" as a hypothesis to test, not a
given.

One more: company names in call titles won't exactly match CRM account names (e.g. "Acme
Retail Group" vs "Acme", "Northwind Traders" vs "Northwind"). On a fuzzy miss, keep and flag
the call — never hard-drop it just because the name didn't resolve.

## Design decision 3 — The verbatim gate (the anti-fabrication mechanism)

This is stage 4, and it's the whole point. After the model proposes candidate quotes, a script
checks each one is an exact substring of the raw transcript (whitespace normalised, case
preserved). Passes go through; failures are dropped, not rewritten.

The logic is simple enough to state in full (the starter skill ships a ready-to-run version):

- Normalise whitespace in both the transcript and the candidate quote.
- If the normalised quote is an exact substring of the normalised transcript → keep.
- If it only matches when you ignore case → flag for human review, don't auto-accept.
- Otherwise → drop.
- No fuzzy/edit-distance matching. "Close" is not verbatim.

If fewer quotes survive than you wanted, output fewer and say so. Never backfill to a target
count with paraphrase — the target is a nice-to-have; verbatim is the requirement.

Caveat the gate does NOT cover: it proves a quote is real, not that the prospect said it (vs.
your rep). On multi-party calls, attributing a rep's framing of a pain to the customer is the main
residual quality risk. That's a judgment step in extraction and a thing to eyeball on your first few
runs — the gate won't catch it for you.

## Design decision 4 — Cap the volume; it's a context limit, not a preference

"Analyse everything for a bigger sample" sounds right and will break the run. Every transcript
flows through the model's context, and context is finite; a month of long calls overflows it and the
unattended job dies partway. And this task saturates fast anyway — you're clustering pains into
a handful of buckets and picking a set of quotes; by ~25-30 substantive calls the top pains and
best quotes are almost always already present. The marginal call rarely adds a new pillar.

**How to adapt:** drop no-shows with a minimum-duration filter, rank the rest by substance
(duration is a decent proxy), take the top N (start around 30), and report coverage every run
("analysed 30 of 47; the rest are listed and were the shortest"). If you genuinely need 100%
coverage, that's a heavier multi-pass build — most people don't need it for messaging.

## Design decision 5 — Deliver to yourself first; never auto-broadcast

This is synthesised, model-generated language about real prospects. It gets a human glance
before it's public. Send the output to your own DM (or a private channel), and forward manually.
Even with auto-approve on the automation, keep the destination private — the 30-second read
is your last line of defence against the attribution issue above. Only widen the destination once
you've watched a few runs and trust the output.

## The traps (things that cost me time so they don't cost you)

- **Fabricated quotes** — the reason the verbatim gate exists. Assume any AI-surfaced
  quote is invented until validated against the raw transcript.
- **Rep-vs-prospect attribution** — the gate proves a quote is real, not who said it. Watch it
  on multi-party calls.
- **Timestamps may not exist** — some call-tool integrations return speaker-tagged text
  with no timecodes. Don't design a "quote with timestamp" output if your data can't back
  it. A title + speaker + verbatim-text locator is often better anyway (it's searchable).
- **Participant filters may not work** — test before relying on them; some return empty
  data.
- **Fuzzy company-name matching** — CRM names ≠ call-title names. Keep-and-flag on a
  miss.
- **Context limits** — cap the calls, rank by substance, report coverage.
- **No native "monthly" schedule** — many schedulers only offer daily/weekly. Workaround
  below.

## Scheduling it

If your scheduler has a monthly or custom-cron option, use it (e.g. run on the 1st or 2nd so the
prior month is fully closed).

If it only offers daily/weekly (common), fake monthly with a weekly schedule + a date guard in
the prompt: set it weekly on a fixed weekday, and open the instructions with —

> First, check today's date. If today's day-of-month is greater than 7, STOP: do
> nothing, run nothing, send nothing. Only proceed on the first occurrence of this
> weekday each month.

Exactly one weekday per month has a day-of-month of 1-7, so only that run does the work; the
others exit in seconds. By the first week of any month, last month is closed, so "last full calendar
month" is always correct. (This leans on the run reading the date correctly — verify the first live
run fired on the right week.)

Permissions: if the only write action is a DM to yourself, auto-approve is safe. If you ever extend
it to post to a shared channel or send email, switch back to manual approval and re-supervise
— the setting blesses future runs, not just today's.

## The discipline that makes it real

The difference between this working and this quietly lying to you is about 20 minutes of
field-checking on YOUR stack before you trust it:

1. Confirm your call tool's filters (title? date? participant?) with real calls.
2. Find your real prospect-call naming convention; build include/exclude sets from actual
   titles.
3. Identify the CRM field(s) that actually mark a customer — test against known accounts.
4. Run it once on last month, supervised. Read the whole output, not the summary.
5. Check the coverage line and the unclassified tail. Tune.
6. Only then let it run unattended — and still read the first few monthly DMs properly.

Automated is not unsupervised. The verbatim gate protects you from invented quotes; only you
protect you from the rest.

Companion artifact: the `SKILL.md` in this folder is a parameterised scaffold with a config
block for your CRM, call-tool, and delivery settings, plus the ready-to-run verbatim-validation
script. Fill in the config, work through the verify checklist, run once supervised.
