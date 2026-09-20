# company-context.md template

This is the file the gate checks. Copy this structure, fill it with real evidence, save it as `company-context.md` in project knowledge or the working directory.

Everything in it is evidence, not aspiration. If a line describes what the company wishes were true, it does not belong here.

---

## 1. ICP

Write one block per ICP. Two is plenty. If there are more than three, the positioning is the problem, not the content.

```
### ICP 1: [job title]

Reports to: [who]
Team size: [range]
Company profile: [size, stage, industry, tech stack if relevant]

Measured on: [the 2-3 metrics on their performance review]
Gets promoted for: [the specific outcome]
Gets fired for: [the specific failure]

Their week: [what they actually spend time on, hour by hour if known]
Tools open on their desktop right now: [named tools]
Who they have to convince internally: [the blocker, and what that person cares about]
What they read and who they trust: [publications, communities, individuals]
```

The "gets fired for" line matters more than any other in this file. It is the fear the content has to speak to, and almost no company writes it down.

## 2. Verbatim bank

Minimum 10. Aim for 25. **Never paraphrase.** The value is in the exact words, including the grammar mistakes, the profanity, and the hedging. The moment you clean a quote up it becomes marketing language and stops being useful.

```
| # | Quote (exact) | Speaker role | Source | Date |
|---|---|---|---|---|
| 1 | "we've basically given up on the nightly run, nobody looks at it anymore" | QA lead, 400-person fintech | Discovery call | 2026-03-14 |
```

Tag each quote with what it reveals: `pain`, `trigger`, `objection`, `outcome`, `internal politics`, or `competitor-language`.

Watch for words the audience uses that the company does not. Those gaps are where most B2B content loses the reader. If customers say "the suite is red again" and the company writes "test reliability challenges," the company is invisible.

## 3. Opinion inventory

This is the section that prevents manufactured hot takes. Every opinion needs all four fields, or it is not usable.

```
### Opinion: [the claim, stated flatly]

Who this annoys: [the specific group that disagrees, named]
Evidence: [data, customer pattern, or direct experience that supports it]
What we do differently because of it: [the product or process consequence]
What a smart person would say against it: [the strongest counter]
```

If the "who this annoys" field is empty, it is not an opinion, it is a platitude. If the "what we do differently" field is empty, the opinion is decorative and the audience will notice the mismatch between the stance and the product.

The counter-argument field is not decoration either. Content that acknowledges the strongest objection reads as written by someone who has had the argument. Content that pretends there is no counter reads as marketing.

## 4. Product truth

```
Genuinely better than alternatives:
1. [specific capability] - evidence: [benchmark, customer outcome, or named comparison]
2. ...
3. ...

Genuinely worse:
1. [the real one] - who should not buy us because of it: [segment]

Where we are simply at parity: [the features the category treats as differentiators that are not]
```

The "genuinely worse" line is the highest-trust asset in the file and the one most companies refuse to write. Content that names a real limitation earns the right to make the strong claims. Do not fake it: an invented weakness ("we're maybe too thorough") is more damaging than no weakness at all, because the audience has seen that trick.

## 5. Forbidden phrases

Pull these from competitor homepages, category analyst reports, and the company's own old copy. Minimum 5, but 20 is more useful.

```
Banned, with the reason:
- "seamless integration" - on 6 of 8 competitor homepages
- "end-to-end" - category wallpaper, carries no information
- "empower your team" - no customer has ever said this
```

Add any phrase that appears on more than two competitor sites. Add any phrase that no customer in the verbatim bank has ever used.

## 6. Proof assets

```
Numbers we can cite: [metric, magnitude, source, whether it is public]
Named customers we can reference publicly: [names, and what each one is willing to say]
Before/after stories: [the specific transformation, with detail]
Things we cannot say publicly: [so drafts do not reach for them]
```

The last line saves a review cycle every time.

## 7. Analogy sources

Where relatable comparisons are allowed to come from, drawn from the ICP's world rather than general culture.

```
Their domain: [processes, failure modes, and rituals the ICP knows cold]
Adjacent domains they would recognize: [the neighbouring discipline they work with daily]
Off-limits: general culture analogies (cooking, sports, orchestras, road trips, gardening)
```

---

## Freshness

Add a header at the top of the finished file:

```
Last updated: [date]
Verbatims collected: [date range]
Next refresh due: [date + 6 months]
```
