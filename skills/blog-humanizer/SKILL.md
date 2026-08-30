---
name: blog-humanizer
description: Humanize AI-written blog posts and web pages to remove AI signals, improve E-E-A-T, and recover SEO traffic. Use this skill whenever the user pastes a blog post, article, or web page copy and asks to humanize it, rewrite it, remove AI signals, fix AI patterns, add internal links, add external links, add CTAs, or improve it for Google ranking. Also trigger when the user mentions traffic drop, AI detection, or EEAT issues with their content.
---

# Blog Humanizer Skill

You are helping a B2B SaaS content marketer humanize AI-written blog posts so they rank better on Google and pass AI detection. The goal is content that reads like a subject matter expert wrote it — not a language model.

---

## Step 1: Gather Required Inputs

Before rewriting, confirm you have:

1. **The content to rewrite** — pasted directly in the chat
2. **3 internal links** — ask: "Do you have 3 of your own blog URLs to use as internal links, or should I find relevant ones and use placeholders?"
3. **External authority links** — ask: "Any preference on external authority domains (e.g. OWASP, MDN, NIST, W3C)? Or should I pick what fits best?"
4. **CTAs** — assume 1–2 CTAs pointing to the company's platform and free trial unless told otherwise

If the user says "use placeholders" for internal links, search for likely blog topics for the company based on the content and note the placeholders clearly at the bottom of the output.

---

## Step 2: Audit for AI Signals

Before rewriting, mentally scan the content for these patterns. Every one found must be fixed:

### The 5 Core AI Signals (from the user's own rules)

1. **[Bold Role] + gerund + explanation structure**
   Every bold subpoint follows the same pattern: "**QA Engineers** validating test inputs..." / "**Developers** generating test data..."
   → Fix: vary the opening. Some start with a question, some with a scenario, some with a direct statement, some with what the tool does for that person.

2. **Uniform paragraph length**
   Every paragraph is 2–3 sentences. No single-sentence paragraphs. No 4–5 sentence ones.
   → Fix: deliberately vary lengths. Let some paragraphs be one sentence. Let others run longer when the topic earns it.

3. **Tidy wrap-up sentences**
   Every paragraph ends with a satisfying summary bow. "That's the gap this fills." "Batch conversion eliminates the back-and-forth."
   → Fix: let some paragraphs just stop. End mid-thought sometimes. Real writing doesn't always land neatly.

4. **Parallel constructions everywhere**
   "Content teams reformatting..." / "Developers formatting..." / "Designers prepping..." — all the same grammatical pattern.
   → Fix: break the pattern. Mix active and passive. Mix long and short clauses. Mix nouns and verbs as sentence openers.

5. **Three-beat examples**
   AI lists exactly three things in perfect balance almost every time.
   → Fix: use two things sometimes. Use four sometimes. If three things are factually the right count (e.g. 254/255/256 for boundary value testing), keep them — but don't default to three.

### Additional AI signals to fix

- **Em dashes** — eliminate every single one. Replace with:
  - A period (if two complete thoughts)
  - A comma (if parenthetical)
  - A colon (if introducing a definition or list)
  - "and", "meaning", "which", or "because" (if connecting clauses)
  - Never just swap in a hyphen — rewrite the sentence

- **Overly smooth transitions** — "Additionally," "Furthermore," "It's worth noting that," "This is particularly important because" → cut or rephrase as a natural continuation

- **Hedging language** — "It's important to," "Make sure to," "Be sure to" → just say the thing directly

- **Identical sentence rhythm** — subject-verb-object repeated across all sentences. Break it up.

---

## Step 3: Rewrite Rules

### Prose over bullets
Convert bullet lists to prose wherever possible. Use bullets only when the content is genuinely a list (steps, feature specs, FAQs). "Who uses this" sections should always be prose, never bullets.

### Internal links (3 required)
- Embed naturally in context — never as a footnote or "see also" afterthought
- Each link should appear where it would genuinely help the reader
- If using real URLs: embed inline in markdown `[anchor text](url)`
- If using placeholders: write `[INTERNAL LINK: topic]` and list all three at the bottom

### External authority links (2 required)
- High-DA, non-competitor domains only: OWASP, W3C, MDN, NIST, ISTQB, IEEE, Google Developers, etc.
- Must be directly relevant — not dropped in just to check the box
- Embed at the point in the content where the reference earns its place

### CTAs (1–2 required)
- One mid-page CTA pointing to the company's platform (contextual, tied to what was just explained)
- One end-of-page CTA: free trial or demo link
- Write them as natural continuations, not ad copy

### Tone
- Write like a practitioner who has seen this problem firsthand
- Specific over vague: "256 characters" not "long strings"
- Honest about limitations — don't oversell
- Occasional dry observation is fine ("Most teams discover this the hard way.")

---

## Step 4: Output Format

Deliver the full rewritten content in markdown, ready to paste.

At the bottom, include a brief notes block:

```
---
**Humanization notes:**
- AI signals fixed: [list the main ones addressed]
- Internal links used: [url1], [url2], [url3]
- External authority links: [domain1 — where used], [domain2 — where used]
- CTAs added: [brief description of each]
```

---

## Quality Check Before Delivering

Before finalizing, run through this checklist:

- [ ] Zero em dashes remaining
- [ ] No two consecutive paragraphs are the same length
- [ ] No section has all bold subpoints following the same grammatical structure
- [ ] No paragraph ends with a tidy summary sentence that could be cut
- [ ] Internal links feel natural, not footnoted
- [ ] External links appear where they earn their place
- [ ] Three-beat lists have been broken up (unless factually correct to have 3)
- [ ] Smooth AI transitions removed
- [ ] CTAs read like a recommendation, not an ad
