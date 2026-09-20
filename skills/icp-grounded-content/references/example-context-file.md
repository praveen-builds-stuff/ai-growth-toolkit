# Example: a populated company-context.md

**This is fictional.** Wombat Labs does not exist. Every quote, number, and customer here is invented to demonstrate the structure. Replace this file entirely before doing real work; do not copy any of its content into live copy.

It is included so the skill can run and be evaluated without a real context file, and so the shape of a *sufficient* file is concrete rather than abstract. Note how specific every line is. That specificity is the whole point. A version of this file full of reasonable-sounding generalities would pass a glance and fail the gate.

---

Last updated: 2026-02-10
Verbatims collected: 2025-11 to 2026-02
Next refresh due: 2026-08-10

Company: Wombat Labs. Data pipeline observability for analytics teams.

## 1. ICP

### ICP 1: Analytics Engineering Lead

Reports to: Head of Data, or sometimes VP Engineering at companies under 300 people
Team size: 3 to 8 analytics engineers
Company profile: Series B to Series D, 200 to 1500 people, dbt plus Snowflake or BigQuery, Airflow or Dagster

Measured on: dashboard uptime for the exec team, time-to-delivery on new data models, and the number of "is this number right?" escalations per month
Gets promoted for: making the data team stop being a bottleneck for other teams
Gets fired for: the board deck pulling a wrong revenue number, twice

Their week: roughly 40% firefighting broken pipelines, 30% reviewing dbt PRs, 20% meetings with stakeholders who want a dashboard, 10% actual modelling work they wanted the job for
Tools open on their desktop right now: dbt Cloud, Snowflake console, Slack, Linear, Looker, a terminal with a failed Airflow DAG in it
Who they have to convince internally: the VP Eng, who sees data tooling as a cost line and already pays for Snowflake, Fivetran, dbt Cloud, and Looker. The objection is never "does this work," it is "that is a fifth data tool."
What they read and who they trust: the dbt Slack community, Locally Optimistic, a handful of practitioners on LinkedIn. They distrust vendor blogs by default.

## 2. Verbatim bank

| # | Quote (exact) | Speaker role | Source | Date | Tag |
|---|---|---|---|---|---|
| 1 | "I find out the pipeline broke because someone posts a screenshot of a dashboard in #general" | Analytics eng lead, 400-person fintech | Discovery call | 2025-11-08 | pain |
| 2 | "we have alerts, they just all fire at once so nobody reads them" | Analytics eng lead, 250-person marketplace | Discovery call | 2025-11-22 | pain |
| 3 | "honestly the tests pass and the data is still wrong, that's the part that kills me" | Senior analytics eng, 900-person SaaS | Discovery call | 2025-12-03 | pain |
| 4 | "my VP asked why we need a fifth data tool and I didn't have a good answer" | Analytics eng lead, 300-person healthtech | Lost deal notes | 2025-12-11 | objection |
| 5 | "I spent a whole Thursday finding out a source system changed a column type" | Analytics engineer, 600-person logistics | Community thread | 2026-01-09 | pain |
| 6 | "we bought it after the board deck had a wrong number in it, that was the trigger" | Head of Data, 1100-person SaaS | Win interview | 2026-01-15 | trigger |
| 7 | "I don't want more alerts. I want fewer, better ones." | Analytics eng lead, 250-person marketplace | Discovery call | 2026-01-20 | outcome |
| 8 | "the freshness checks are table stakes now, everyone has those" | Head of Data, 800-person retail | Discovery call | 2026-01-28 | competitor-language |
| 9 | "setup took two days and I'd budgeted an afternoon" | Analytics engineer, 400-person fintech | Support ticket | 2026-02-01 | objection |
| 10 | "the thing I actually use is the column-level lineage, I use it every single day" | Senior analytics eng, 900-person SaaS | Renewal call | 2026-02-04 | outcome |
| 11 | "nobody upstream tells us when they ship a schema change, ever" | Analytics eng lead, 300-person healthtech | Discovery call | 2026-02-06 | pain |
| 12 | "we're the last to know and the first to get blamed" | Analytics engineer, 600-person logistics | Community thread | 2026-02-07 | pain |

Vocabulary gap to watch: customers say "the pipeline broke" and "the dashboard is wrong." They never say "data quality incident" or "observability posture," both of which appear on our own homepage.

## 3. Opinion inventory

### Opinion: Data quality alerting is mostly noise, and adding more tests makes it worse

Who this annoys: every vendor selling test coverage as the metric, and the part of the dbt community that treats more assertions as unambiguously good
Evidence: verbatims 2 and 7. Across 18 discovery calls, 14 teams had alerting already and 11 described ignoring it. Median alert volume in accounts we onboarded last quarter was 240 per week; median acted upon was 6.
What we do differently because of it: we ship with alerting off for everything except column-level changes with a downstream consumer, and we cap alert volume rather than maximizing coverage
What a smart person would say against it: suppression hides real failures, and the teams drowning in alerts usually have a pipeline design problem that no tool should paper over. Partly fair, and we say so.

### Opinion: Tests passing while the data is wrong is the normal case, not the edge case

Who this annoys: anyone whose product is a test framework
Evidence: verbatim 3. In our own audit of 40 accounts, 62% of the incidents customers cared about produced zero failing tests, because the failure was a semantic change upstream, not a constraint violation.
What we do differently because of it: we diff column semantics and distributions against history rather than checking assertions
What a smart person would say against it: distribution diffing generates false positives on any genuinely seasonal business, and we have to tune it per account, which is real work.

### Opinion: "Fifth data tool" is a legitimate objection and most vendors dodge it

Who this annoys: our own sales team, occasionally
Evidence: verbatim 4, which came from a deal we lost and deserved to lose
What we do differently because of it: we publish a page listing the cases where dbt tests plus a Slack webhook are genuinely enough, and we tell those teams not to buy yet
What a smart person would say against it: this loses deals we could have won by being more persuasive. True. We think the trust is worth more.

## 4. Product truth

Genuinely better than alternatives:
1. Column-level lineage across dbt and the warehouse, resolved in under 10 seconds on a 4000-model project. Evidence: verbatim 10; benchmarked against two named competitors at 40s and 2m on the same project.
2. Upstream schema-change detection that fires before the pipeline runs, not after it fails. Evidence: verbatims 5 and 11; the single most-cited reason in win interviews.
3. Setup that does not require a warehouse role with write permissions. Evidence: named blocker in 7 of 22 evaluations last year.

Genuinely worse:
1. Our alerting is deliberately conservative and will miss slow-drift quality degradation that a threshold-based tool would catch. Who should not buy us because of it: regulated finance teams who need documented coverage of every column for audit.

Where we are simply at parity: freshness checks, row-count anomaly detection, Slack and PagerDuty integrations. Verbatim 8 confirms the market treats these as table stakes. Do not lead with them.

## 5. Forbidden phrases

- "data observability platform" - on 5 of 6 competitor homepages
- "single source of truth" - category wallpaper, carries no information
- "empower your data team" - no customer in the bank has ever said "empower"
- "end-to-end visibility" - on 4 competitor sites
- "proactive, not reactive" - appears on 3, and reads as a slogan rather than a claim
- "data quality incident" - our word, not theirs. They say "the pipeline broke"
- "observability posture" - nobody has ever said this out loud
- "mission-critical data" - all their data is mission-critical, so the modifier does nothing

## 6. Proof assets

Numbers we can cite: 62% of customer-visible incidents produced no failing test (internal audit, 40 accounts, public); 10-second lineage resolution on a 4000-model project (benchmarked, public); median 240 weekly alerts before onboarding versus 6 acted upon (internal, public)
Named customers we can reference publicly: none yet. Two are in legal review.
Before/after stories: the healthtech team in verbatim 11 went from finding out about schema changes via broken dashboards to catching 9 of 11 in the following quarter before any downstream run. Usable without the name.
Things we cannot say publicly: revenue, headcount, the churned logo in retail, and anything sourced from the Series C deck

## 7. Analogy sources

Their domain: failed DAG runs, PR review queues, on-call rotations, backfills, the Monday morning board-deck scramble, schema migrations landing unannounced
Adjacent domains they would recognize: application observability and on-call practice (Datadog, PagerDuty, alert fatigue), and software testing culture generally
Off-limits: cooking, orchestras, sports teams, road trips, gardening, air traffic control
