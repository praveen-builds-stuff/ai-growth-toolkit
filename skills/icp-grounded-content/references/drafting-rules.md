# Drafting rules

Read before every draft. These replace vibes-level advice ("be human, be opinionated") with mechanics that can actually be followed and checked.

## Rule 1: Claims map or they get cut

Every factual claim, statistic, customer behaviour, and competitive assertion traces to a specific line in the context file. Anything that does not trace gets cut, not hedged.

Hedging is the failure mode to watch for. "Many teams struggle with flaky tests" is an unsupported claim wearing a disguise. If the verbatim bank does not contain teams saying this, the sentence goes.

Never invent a statistic. Not as a placeholder, not with a bracket around it, not "roughly." A fabricated number in a draft survives review more often than it should, and a made-up stat in published B2B content is the fastest way to lose a technical audience permanently.

## Rule 2: Opinions come from the inventory only

When the brief asks for something opinionated, take a position from the opinion inventory. Do not generate a new one.

A manufactured opinion is detectable because it has no consequence behind it. Real positions have a product decision, a hiring choice, or a lost deal attached. Invented ones float free, which is exactly how they read.

If the inventory is empty and the brief demands a stance, say so and offer to run the opinion questions from the bootstrap. That conversation takes fifteen minutes and produces something defensible.

## Rule 3: Readability is structural, not lexical

The common advice is to write at a grade 5 reading level and check it in a readability tool. For technical and specialist B2B audiences this is actively wrong, because readability scores penalize polysyllabic nouns, and in specialist writing the polysyllabic nouns are the precise ones. Strip "idempotent", "parallel execution", "attribution window", or "reconciliation" and the writing does not get clearer. It gets vaguer, and it reads as condescending to a reader who uses those words every day.

Apply simplification to structure instead:

- One idea per sentence. Split anything carrying two.
- Cap sentences at roughly 25 words, with occasional short ones for rhythm.
- Active voice by default.
- Cut connective padding: "in order to", "it is important to note", "when it comes to", "at the end of the day".
- Keep every domain noun the ICP uses daily. Simplify the verbs and the joins around them.

The test that works better than any score: read it aloud. If you would not say it to this person standing at their desk, rewrite it.

## Rule 4: Analogies come from their world

Analogies from general culture (an orchestra, a recipe, a road trip, a sports team) signal that the writer knows the audience's domain only from the outside. Draw instead from the ICP's own working day or an adjacent discipline they deal with constantly, as listed in section 7 of the context file.

A comparison that lands makes the reader think "this person has done my job." A generic one makes them think "this person googled my job."

## Rule 5: Specificity is the whole game

Generic nouns are where relatability dies. Replace categories with instances wherever the context file supports it:

- "a testing tool" becomes the actual tool name
- "significant time savings" becomes the actual number with its source
- "customers tell us" becomes the verbatim, attributed to a role
- "at scale" becomes the actual scale
- "our integration" becomes what it does on a Tuesday when it breaks

Error messages, log lines, tool names, meeting names, and numbers with odd digits in them are all texture that reads as lived experience. Round numbers read as estimates.

## Rule 6: The swap test

Before delivering, mentally place a competitor's logo on the draft. If it still reads as true and publishable, the draft has said nothing only this company could say. Rewrite around whatever survives the swap.

Run this on the headline and the opening paragraph specifically. Those are where generic copy concentrates.

## Rule 7: One reaction, not many

Content that tries to produce several reactions produces none. Pick the single response the piece is for and cut anything not serving it. The target is not "this is amazing," which nobody thinks about B2B content. It is closer to:

- "that is exactly my problem and nobody has described it this precisely"
- "I had not thought about it that way and I think they are right"
- "I am sending this to my manager"

## Format notes

**LinkedIn or social.** The first two lines carry the whole post because that is the truncation point. Open with the most specific thing in the piece, not with context-setting. Never open with a rhetorical question the reader would answer "no" to.

**Email.** The subject line is a promise and the first line has to pay it immediately. One ask per email. If the body needs a "quick note on another thing," that is a second email.

**Landing page.** The hero has to name the problem in the ICP's vocabulary before naming the product. Every claim in the hero needs proof visible without scrolling. Match the vocabulary to the traffic source: paid search visitors arrive with the query still in their head.

**Blog intro.** No throat-clearing about how important the topic is. Open where the reader already is. If the first paragraph could be deleted without loss, it should be.

**Launch or announcement.** Lead with what the reader can now do that they could not do last week. The feature name is the least interesting fact available and belongs in paragraph two.

## Anti-patterns

Never produce any of these, even when the brief seems to ask for them:

| Anti-pattern | Why it fails |
|---|---|
| Invented statistics ("73% of teams report...") | Destroys credibility permanently with a technical audience |
| Fabricated or composite customer quotes | Fraudulent, and detectable by anyone who knows the market |
| "Most people think X. Actually, Y." with evidence for neither half | The signature move of manufactured contrarianism |
| A weakness the company does not actually have | Fake humility is more damaging than none |
| Analogies from general culture | Signals outsider status |
| Forbidden phrases from the context file | The category wallpaper the content exists to escape |
| Calling the audience by a flattering label they do not use | Nobody calls themselves a "modern QA leader" |
| Manufactured urgency with no real deadline | Trains the audience to discount everything |
| Opening with a rhetorical question | Reads as template, and invites a "no" that ends the read |
| Three-item lists everywhere | A rhythm tell that reads as machine-generated |

## Self-check before delivering

Work through this list, then produce the evidence trace:

1. Does every claim trace to a context file line?
2. Is every opinion from the inventory, with its consequence visible?
3. Would the ICP recognize this vocabulary as their own?
4. Does it survive the swap test?
5. Is there at least one detail only an insider would know?
6. Are the domain nouns intact and the connective tissue simple?
7. Zero forbidden phrases?
8. Does it name a real limitation anywhere, or does it read as a sales pitch throughout?
9. One reaction, clearly targeted?

Anything failing 1, 2, or 4 needs a rewrite rather than an edit.
