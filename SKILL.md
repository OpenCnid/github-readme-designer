---
name: github-readme-designer
description: Design or redesign the visual layout, opening viewport, hierarchy, imagery, badges, diagrams, and GitHub-rendered presentation of repository README.md files. Use for README beautification, first-impression improvements, hero sections, visual refreshes, gallery layouts, screenshot placement, or making a GitHub project page feel intentionally designed. Preserve owner-authored meaning and avoid inventing project copy; this skill owns presentation, not substantive documentation.
---

# GitHub README Designer

Treat a repository README as a constrained landing page rendered by GitHub. Create a distinctive first impression and a coherent visual journey without turning the README into a generic badge wall or writing product claims for the owner.

## Non-negotiable boundary

- Preserve owner-authored wording unless explicitly asked to edit it.
- Do not invent taglines, benefits, metrics, compatibility claims, testimonials, features, install commands, or calls to action.
- Reposition, group, shorten only with permission, or replace missing text with invisible owner prompts such as `<!-- OWNER: add a one-line project promise -->`.
- Never fabricate badges, package versions, CI states, sponsors, downloads, or links.
- Keep useful technical content intact below the redesigned opening unless the user scopes a larger restructuring.

## Workflow

### 1. Inspect the GitHub canvas

Read the current `README.md`, repository metadata, image assets, logo files, screenshots, demos, and relevant owner-authored copy. Identify:

- project type and audience;
- visual assets that already establish identity;
- the current opening sequence and first major sections;
- light/dark-mode behavior;
- existing badges and whether their targets are real;
- constraints imposed by nested README location or relative paths.

Read [references/github-canvas.md](references/github-canvas.md) before using HTML, images, responsive variants, alignment, or diagrams.

### 2. Choose a visual direction

Infer a direction from the repository rather than applying a house template. Select one primary composition from [references/layout-patterns.md](references/layout-patterns.md), then adapt it to the project’s assets and tone.

Write a short design intent before editing:

```text
Audience: ...
First impression: ...
Primary visual: ...
Opening composition: ...
Identity cues: ...
Preserved owner copy: ...
Missing owner inputs: ...
```

Avoid fashionable decoration that conflicts with the project. A terminal tool, design system, research library, and consumer app should not share the same opening treatment.

### 3. Design the opening viewport

Prioritize the first screenful and the first third of the README. Establish, in this order unless the repository suggests otherwise:

1. recognizable identity: logo, wordmark, or strong typographic title;
2. owner-supplied one-line orientation;
3. one dominant proof visual: screenshot, demo, diagram, output, or product montage;
4. a restrained action/navigation row using real links;
5. a small trust/status row only when backed by real repository data;
6. a visual transition into the body.

Use one dominant visual idea. Do not make the title, badge row, screenshot, feature grid, and architecture diagram compete at equal weight.

### 4. Build a visual rhythm for the body

- Alternate dense technical sections with visual relief.
- Turn repeated parallel facts into compact tables or cards only when narrow screens remain readable.
- Use screenshots to prove interface behavior, output blocks to prove tools, and diagrams to explain systems.
- Prefer a single excellent visual over several ornamental images.
- Use `<details>` for secondary material, not essential onboarding.
- Let GitHub’s generated outline handle navigation unless a custom contents block materially helps.
- Keep heading depth shallow and predictable.

Do not rewrite body copy merely to fit the layout. Surface conflicts and leave owner prompts where new text is necessary.

### 5. Create or refine assets

Prefer repository-owned assets under a clear directory such as `docs/assets/` or `.github/assets/` and reference them with relative paths.

- Reuse or crop existing screenshots before generating decorative art.
- Create an SVG diagram when the information is structural and exact.
- Use the harness’s image-generation capability only when the user wants a new raster hero, illustration, or backdrop.
- Provide light and dark variants when contrast cannot be made robust in one asset.
- Optimize dimensions and file size; avoid loading a full-resolution screenshot only to display it narrowly.
- Include meaningful alt text for informative images and empty alt text for purely decorative images.

Never modify a logo’s proportions, colors, or clear space without owner authorization.

### 6. Preview and audit

Inspect the rendered README, not only its source. Check desktop and a narrow viewport when the harness can render GitHub-flavored Markdown. Confirm that external badges and images load and that local paths work from the README’s actual location.

Run the bundled structural audit:

```bash
python scripts/audit_readme.py path/to/README.md
```

Then follow [references/visual-qa.md](references/visual-qa.md). Iterate until the opening has a clear focal point, the body scans cleanly, and GitHub light/dark themes remain usable.

## Design rules

- Design for GitHub-flavored Markdown and GitHub’s sanitized HTML, not a general web browser.
- Do not add CSS, JavaScript, web fonts, autoplay media, or layout that depends on unsupported HTML.
- Keep the first badge row to roughly 3–6 high-signal items; zero is valid.
- Avoid oversized logos that delay all evidence of the project.
- Avoid centered alignment for long prose or code-heavy sections.
- Avoid wide multi-column HTML tables as the main mobile layout.
- Avoid emoji as a substitute for identity.
- Avoid decorative separators between every section.
- Avoid false interactivity: buttons are links, not controls.
- Avoid external image generators whose URLs leak repository/user data or may disappear.

## Delivery

Return:

- the edited `README.md` and any new repository-owned assets;
- a one-paragraph explanation of the visual direction;
- a list of preserved owner copy and any invisible owner-input prompts;
- preview/audit results and any GitHub-rendering limitations;
- a concise summary of files changed.

If the user requested concepts rather than implementation, provide 2–3 materially different opening compositions using wireframes or small Markdown mockups, without filling them with invented marketing text.
