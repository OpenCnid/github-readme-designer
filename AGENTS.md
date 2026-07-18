# AGENTS.md

## Repository purpose

This repository contains `github-readme-designer`, a portable Agent Skill for designing the visual presentation of GitHub repository READMEs. Treat the README as a GitHub-rendered landing experience, with special attention to the opening viewport and first third.

## Apply the skill

When asked to create, beautify, restructure, or visually redesign a GitHub `README.md`:

1. Read `SKILL.md` completely before editing the target README.
2. Read `references/github-canvas.md` before using HTML, SVG, screenshots, theme variants, alignment, or diagrams.
3. Read `references/layout-patterns.md` before choosing the opening composition.
4. Inspect the target repository’s current README, metadata, logo, screenshots, demos, and existing visual identity.
5. Write a short design intent covering audience, first impression, dominant visual, composition, identity cues, preserved copy, and missing owner inputs.
6. Implement the visual hierarchy and repository-owned assets.
7. Read `references/visual-qa.md`, render the result, run the audit, and iterate.

If the harness supports explicit skill invocation, use `github-readme-designer`. In Codex, invoke `$github-readme-designer`; in Claude Code, invoke `/github-readme-designer`.

## Content boundary

- Own presentation, hierarchy, composition, and visual assets.
- Preserve owner-authored meaning unless copy editing is explicitly requested.
- Do not invent taglines, benefits, metrics, testimonials, features, compatibility claims, install commands, links, or calls to action.
- Do not fabricate CI, package, coverage, sponsor, download, or version badges.
- Use an invisible `<!-- OWNER: ... -->` prompt when a composition requires missing owner copy.
- Never publish secrets, local paths, temporary URLs, or placeholder content.

## Design expectations

- Make the design specific to the repository type and existing identity.
- Give the opening one dominant visual idea.
- Prefer real product screenshots, authentic output, and exact diagrams over decorative art.
- Keep core identity assets inside the target repository and use relative paths.
- Design for GitHub light and dark themes and narrow viewports.
- Use static neon and glow effects when appropriate; avoid flashing, autoplay, or inaccessible motion.
- Do not rely on custom CSS, JavaScript, web fonts, or HTML GitHub sanitizes.
- Keep long prose left-aligned even when the opening identity block is centered.

## Editing this skill

- Keep `SKILL.md` portable: its YAML frontmatter contains only `name` and `description`.
- Put Codex-specific interface metadata in `agents/openai.yaml`.
- Keep the core workflow concise; place detailed guidance in the existing `references/` files.
- Keep reference files one level from `SKILL.md` and link them directly from it.
- Add deterministic checks to `scripts/` only when they improve repeatability without unnecessary dependencies.
- Keep repository showcase visuals under `.github/assets/`; do not confuse them with reusable skill output assets.
- Do not add generated marketing claims to the skill or its examples.
- Preserve compatibility with Codex, Claude Code, and other Agent Skills–compatible harnesses.

## Validation

Run these checks after changing the README, SVGs, audit logic, or skill instructions:

```bash
python scripts/audit_readme.py README.md
python -c "import xml.etree.ElementTree as ET; ET.parse('.github/assets/readme-designer-hero.svg'); ET.parse('.github/assets/neon-workflow.svg'); print('SVG assets are valid XML')"
git diff --check
```

Also:

- run the available Agent Skill validator after modifying `SKILL.md` or `agents/openai.yaml`;
- render every changed SVG at its native dimensions and inspect it visually;
- inspect the rendered GitHub README in light and dark themes;
- inspect a narrow viewport around 375–430 CSS pixels;
- verify every local image, badge target, and navigation link;
- confirm the audit reports zero errors and resolve warnings intentionally.

## Review blockers

Do not approve changes that introduce:

- invented repository copy or unsupported claims;
- fake or broken badges and links;
- missing local assets or inaccessible informative images;
- unreadable SVG labels at GitHub content width;
- theme-dependent contrast failures;
- excessive centered prose, badge walls, or competing focal points;
- a generic visual formula unrelated to the target repository;
- new runtime dependencies without a clear need.

## Publishing safety

Do not push branches, merge pull requests, change repository visibility, publish releases, or alter repository topics unless the user explicitly requests the external change.
