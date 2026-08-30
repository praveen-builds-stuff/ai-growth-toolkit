# Brand Design System — Reference (Example)

*This is a fictional, illustrative brand system used to demonstrate the ab-test-design-reviewer
skill. Swap in your own team's actual design system rules and hex values before using this
skill for real work.*

## Typography

**Primary font:** Sora — only font allowed. No exceptions.
- Weights: Regular (400), Semi Bold (600), Bold (700)
- Fallback: Sora, -apple-system, system-ui, sans-serif

| Element | Size | Weight | Notes |
|---|---|---|---|
| Hero Headline | 44–48pt | Bold (700) | Hero sections, slide titles |
| Headline | 28–34pt | Bold (700) / Semi Bold (600) | Section headings |
| Eyebrow / Label | 10–14pt | Bold (700) | UPPERCASE, letter-spacing 0.1em |
| Body | 14–16pt | Regular (400) | Paragraphs, descriptions |
| Small Body | 10–12pt | Regular (400) | Card content, supporting text |
| Caption | 8–10pt | Regular (400) | Metadata, timestamps, annotations |

**Typography rules:**
1. Sora on everything. No fallback fonts in production.
2. Left-align body text; center-align only standalone hero titles.
3. Eyebrows always UPPERCASE with letter-spacing (2pt or 0.1em).
4. Never more than 3 type sizes on a single slide or section.

---

## Color Palette

### Brand Identity Colors
| Name | Hex | Role |
|---|---|---|
| Deep Navy | #0B1E3D | Primary brand background, dark sections |
| Signal Green | #17B890 | Logo color, primary CTAs (solid buttons), active states |
| Coral | #F26D6D | Accent text, eyebrow labels, highlighted words in headlines |
| White | #FFFFFF | Primary text on dark backgrounds, cards |

### Supporting Color
| Name | Hex | Usage |
|---|---|---|
| Violet | #6E4CF5 | Gradient endpoint (coral → violet), decorative elements |

### CTA Treatments
- **Solid CTA (primary):** Background #17B890 (Signal Green), text #FFFFFF.
- **Gradient CTA (form submits):** #F26D6D → #6E4CF5 at 135°. Used on form submit buttons ONLY.

### Dark Mode Surfaces (Default Theme)
| Name | Hex | Usage |
|---|---|---|
| Background | #0B1E3D | Page background, deepest layer |
| Card BG | #16294D at 60–70% opacity | Glass morphism cards |
| Border | #3A4A6B | Card borders, dividers |

### State / Semantic Colors
| Name | Hex | Usage |
|---|---|---|
| Success | #1EDC96 | Positive outcomes |
| Warning | #F5A623 | Caution, attention needed |
| Error | #E14F4F | Failures, negative outcomes |

### Color Rules
1. Never use pure black (#000000). Use #0B1E3D on light, #FFFFFF on dark.
2. Signal Green for CTAs and logo only — not for general accent text.
3. Coral for text highlights and labels in headlines only.
4. Dark mode is the default. Light mode only when content requires it.
5. Glass morphism cards: card-background color at 60–70% opacity, border at 1–1.5px solid.

---

## Logo Usage

| Variant | Use On |
|---|---|
| White horizontal | Dark backgrounds |
| Dark horizontal | Light/white backgrounds |
| Mark only | Favicons, small placements |

**Placement:**
- Web: Top-left navbar
- Minimum clear space: Half the height of the mark on all sides
- Minimum size: 80px wide on screen

**Do Not:**
- Recolor the mark
- Place white logo on light backgrounds (or dark logo on dark backgrounds)
- Stretch or distort aspect ratio

---

## Glass Morphism

Signature visual treatment for cards/containers on dark backgrounds.

| Property | Value |
|---|---|
| Background | Card BG color at 60–70% opacity |
| Border | Border color, 1–1.5px solid |
| Border radius | 4–8px |
| Backdrop blur | 10–20px |

- **Use when:** Content cards, feature boxes, stat callouts, sidebar containers
- **Do NOT use:** On light backgrounds; for full-width sections

---

## Slide / Page Patterns

- **Eyebrow pattern:** Coral vertical bar (3–4px wide) + UPPERCASE coral text with wide letter-spacing.
- **Split layout:** 45/55 split — text left, visual right, ~0.3" gap.

---

## Voice & Tone (Visual)

| Do | Don't |
|---|---|
| Deep navy backgrounds, premium feel | Bright, playful, startup-y |
| Signal Green for CTAs and positive states | Signal Green for all accent text |
| Coral for highlighted words and labels | Off-brand reds or oranges as accents |
| Confident, technical | Buzzword-heavy, vague |
| Clean spacing, breathing room | Cramped, text-heavy |
| Coral-to-violet gradient on form submits ONLY | Gradients everywhere |
| Sora everywhere | Mixed fonts |
