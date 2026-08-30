# AI Growth Toolkit

Skills and tools I've built for growth and product marketing work — some are Claude skills
(structured playbooks that turn a fuzzy, repeatable task into a reliable process), others are
real automation projects (scripts, scheduled jobs, monitoring). Grouped by which they are.

## What's a skill?

A skill is a written playbook that tells Claude exactly how to handle a specific, recurring task:
what inputs to ask for, what steps to follow, what to check before delivering an answer, and
what output format to use. Instead of re-explaining a task every time, I load the skill and Claude
follows the same process every time.

## Skills

**cro-page-auditor** — Audits a landing page screenshot or URL for conversion issues using visual analysis alone, no analytics access needed. Structured across seven CRO dimensions, ending in one sharp, actionable insight.

**cro-audit** — A deeper version that reads a screenshot alongside a heatmap and scrollmap, tags every finding with a confidence level, and gates recommendations so nothing gets implemented on a guess.

**ab-test-design-reviewer** — Pre-flight QA for an A/B test design before it ships. Checks brand compliance, UX friction, and whether the design actually gives the test hypothesis a fair shot.

**blog-humanizer** — Rewrites AI-drafted blog content to remove the patterns that make it read like AI: uniform paragraph length, tidy wrap-up sentences, three-beat lists, over-smooth transitions.

**anti-ai-writing-style** — The writing system behind everything above. A full set of rules for direct, specific, human-sounding writing, with a hard list of banned words and phrases.

**praveen-linkedin-voice** — Writes LinkedIn posts that sound like me, not a brand account or an AI. Built from studying my own real posts and coding what works and what doesn't.

**growth-experiment-brainstormer** — A brainstorming partner that won't stop at "here's an idea." Forces every idea into a testable hypothesis, scores it on Impact/Confidence/Ease, and defines a kill criterion before any time gets spent on it.

**voc-messaging-starter** — Turns a month of prospect sales calls into customer-language messaging: pains, buying triggers, pillars, hook headlines. The one rule everything hangs on: quotes are lifted from real transcripts, never authored by the model — enforced by a validation script, not left to good intentions. Read the companion `PLAYBOOK.md` for the full reasoning; it's the most engineering-heavy piece in here.

## Tools

**ads-relevance-audit** — Cross-checks keyword intent, ad copy, and landing page content in a Google Ads account to flag Quality Score problems, and recommends reroute-before-pause fixes ranked by severity.

**canary-landing-page-monitor** — Daily synthetic monitoring for paid landing pages: broken links, dead CTAs, embedded forms that are configured but not actually rendering. Built with Playwright and GitHub Actions, emails a report via Resend.

**ads-intelligence-hub** — A three-module app: a rule engine that flags underperforming keywords by region and hands them to Claude for a specific action per row, a GEO-aware ad copy rewriter with a hard character-limit safety net, and a Quality-Score-focused landing page title generator. The most "real app" of everything here — background data fetching with caching, graceful degradation, post-processing that catches the model's mistakes.

## Using the skills

Each skill folder has a `SKILL.md` (the instructions) and, where needed, a `references/` folder
with supporting material. Drop a folder into Claude, Claude Code, or any tool that supports the
Claude Skills format, and it activates automatically when you ask for the kind of task it covers.

Some reference files use fictional example data — the brand design system in
`ab-test-design-reviewer`, the writer examples in `praveen-linkedin-voice`, the config
placeholders in `voc-messaging-starter`. Swap in your own team's real details before using
those for production work.

## Using the tools

Each tool folder is close to a real, standalone project. Read its README for setup —
generally: install dependencies, fill in the placeholder config/URLs/credentials, and run.
