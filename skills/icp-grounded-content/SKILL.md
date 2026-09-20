---
name: icp-grounded-content
description: Write net-new B2B content (LinkedIn posts, emails, landing page copy, blog intros, launch announcements, ads) that a specific ICP actually finds relatable, by hard-gating every draft on a populated company-context file of verbatim customer language, defensible opinions, and honest product truth. Use whenever the user asks to write, draft, or create content aimed at a named business audience - "write a post for QA leads", "draft the launch email", "write the LP hero", "make this land with engineering managers", "this needs to stand out from competitors" - and especially when they ask for content that is more human, more opinionated, less corporate, or less generic. Also use when the user has just joined a company and needs to build the audience-context foundation from customer calls, tickets, and reviews. Do NOT use for editing text that already exists (use humanizer, copy-defluffer, or copy-polish for that) or for personal posts written in one named individual's voice (use that person's voice skill instead).
---

# ICP-Grounded Content

## Why this skill exists

Most advice about making B2B content less boring is posture, not process: "be human, be opinionated, be fun." Handed to a language model, that advice fails in a specific way. Asked to be opinionated, the model manufactures an opinion. Asked to be relatable, it reaches for an analogy from general culture (an orchestra, a recipe, a road trip) because it has no access to the audience's actual working day. The output sounds confident and lands as fraudulent, because the reader is a practitioner and can tell within seconds that the writer has never done their job.

Relatability is not a writing technique. It is an evidence problem. The fix is to make evidence a precondition for drafting rather than a nice-to-have. That is what this skill does.

## The gate

Before writing a single line of content, locate the company-context file. It is usually at one of:

- `company-context.md` in the current working directory or project knowledge
- a file the user names when asked
- project knowledge / uploaded files in the current session

If no context file exists, or the required sections are empty, **do not draft.** Do not write a "rough version to get started." Do not offer a placeholder draft with brackets for the user to fill in. A draft produced without evidence sets an anchor that is very hard to pull back from, and the user will ship it.

Instead, say plainly which required fields are missing and offer to run the bootstrap (see `references/bootstrap-interview.md`). Keep the refusal short and useful: name the blocking gaps, estimate the time to fill them, and offer to start with the highest-leverage source.

If the user is trying the skill out rather than doing real work, offer the fictional example in `references/example-context-file.md` as a sandbox. Anything drafted against it is a demonstration and must be labelled as such, because every quote and number in that file is invented.

### Minimum bar to draft

All five of these must be present:

| Section | Minimum |
|---|---|
| ICP definition | Job title, who they report to, what they are measured on, what gets them promoted or fired |
| Verbatim bank | 10+ direct quotes from real customers or prospects, each with a source label |
| Opinion inventory | 3+ defensible positions, each with the evidence behind it |
| Product truth | 3 things the product genuinely does better, 1 thing it genuinely does worse |
| Forbidden phrases | 5+ category-standard phrases every competitor already uses |

If four of five are filled, the gate still holds. Partial evidence produces partial-quality content that looks finished, which is the worst outcome.

**One exception:** if the user explicitly acknowledges the gate and overrides it for a low-stakes internal draft, proceed, but label the output clearly as ungrounded and list every claim that has no evidence behind it.

## Workflow

### 1. Read the context file

Read it fully before drafting. Pay particular attention to the verbatim bank and the forbidden phrases: these are the two sections that most directly shape word choice.

### 2. Confirm the brief

Get three things straight before writing. Ask only if they are genuinely unclear from the request:

- **Who exactly** is reading this. "B2B buyers" is not an ICP. "QA lead at a 200-person product company who just inherited a flaky Selenium suite" is.
- **What single reaction** you want. Not "engagement." Something like: "I have that exact problem and nobody has described it this precisely before."
- **What the reader does next**, if anything.

### 3. Draft under constraint

Follow `references/drafting-rules.md`. The rules that do the most work:

- Every factual claim maps to a line in the context file. Unmapped claims get cut, not softened.
- Opinions come only from the opinion inventory. Never generate a new take to satisfy a request to "be opinionated."
- Analogies come from the ICP's working day or an adjacent domain they know cold. Never from general culture.
- Keep the domain vocabulary the ICP uses daily. Simplify structure, not terminology.
- Numbers, product names, error messages, and tool names are the texture that makes writing feel lived-in. Generic nouns are where relatability goes to die.

### 4. Run the swap test

Put a competitor's name and logo on the finished draft. If it still reads as true and publishable, the draft is dead. Rewrite it around whatever only this company can say.

This single test catches more generic output than any style rule.

### 5. Deliver with an evidence trace

Output the content first, clean and ready to use. Then a compact trace beneath it:

```
Evidence trace
- [claim or line] <- [context file section / source]
- [claim or line] <- [context file section / source]

Unsupported and cut: [anything removed during the self-check, and why]
```

Keep the trace tight. Its purpose is to let the user spot a claim that drifted, not to re-argue the draft. If the trace has any row where the source is vague ("general knowledge", "industry standard"), that line should have been cut already. Go back and cut it.

## What this skill does not do

This is an upstream drafting skill. It hands off cleanly:

- **Editing existing copy** goes to `humanizer`, `copy-defluffer`, or `copy-polish`.
- **A named individual's personal voice** goes to that person's voice skill. This skill produces brand or product content, which is a different register.
- **After drafting**, running the output through a humanizing or defluffing pass is fine and usually improves it. Grounding and polish are separate jobs.

## Reference files

- `references/context-file-template.md` - the schema of `company-context.md`. Read when creating or auditing a context file.
- `references/bootstrap-interview.md` - how to populate the context file from scratch at a new company, with sources ranked by fidelity. Read when the gate blocks and the user wants to fix it.
- `references/drafting-rules.md` - the drafting mechanics, format-specific notes, and the anti-pattern list. Read before every draft.
- `references/example-context-file.md` - a fully populated fictional context file. Read to see what a sufficient file looks like, or to demo the skill when no real file exists yet. Never treat its contents as real evidence.

## Maintenance

A context file decays. Verbatims older than about six months describe a market that has moved, and the opinion inventory goes stale fastest of all because competitors copy positions.

When the file is more than six months old, say so before drafting and offer a refresh pass. Do not block on it. Stale evidence still beats no evidence.
