# GitHub README canvas

Use these constraints whenever composing or reviewing the layout.

## Rendering model

- Target GitHub-flavored Markdown as rendered on repository pages.
- Assume GitHub sanitizes HTML and ignores custom CSS and JavaScript.
- Use Markdown for durable structure. Use small amounts of supported HTML only for composition Markdown cannot express cleanly.
- Expect desktop, narrow browser, mobile, light theme, and dark theme.
- Do not promise exact pixel placement. GitHub chrome, viewport, font metrics, translations, and user settings change the visible first screenful.

## Reliable primitives

- Headings, paragraphs, blockquotes, lists, code fences, tables, task lists, links, images, and horizontal rules.
- Relative repository links and image paths.
- `<picture>` with `prefers-color-scheme` sources for theme-aware images.
- `<details>` and `<summary>` for optional secondary content.
- Minimal centered HTML blocks for a hero; return to left alignment for body prose.
- Mermaid only when GitHub rendering is verified and the diagram is genuinely explanatory. Keep a text alternative when portability matters.

## Asset paths

Place README-owned assets in a stable repository directory. Prefer:

```text
docs/assets/readme/
  hero-light.webp
  hero-dark.webp
  product-shot.webp
  architecture.svg
```

Use relative paths so forks and branches continue to render. Avoid branch-pinned raw URLs for assets in the same repository.

Theme-aware example:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/hero-dark.webp">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/readme/hero-light.webp">
  <img alt="Owner-supplied description of the project interface" src="docs/assets/readme/hero-light.webp">
</picture>
```

## First-third budget

The opening should usually contain one identity block, one orientation line, one primary visual, and one compact action/status area. Reduce elements when the primary visual needs room. The first third should answer visually:

- What kind of thing is this?
- What is its visual identity?
- What proof can I see immediately?
- Where do I go next?

The owner supplies the semantic answers. The designer supplies hierarchy and placement.

## Accessibility

- Keep text out of raster images when the same information belongs in selectable Markdown.
- Make essential diagram labels readable at GitHub’s normal content width.
- Use descriptive alt text for informative visuals.
- Check contrast in both GitHub themes.
- Never encode status by color alone.
- Avoid flashing and unnecessary animated GIFs. Provide a static fallback when motion is essential.

## External content

Treat every hotlinked badge, analytics card, screenshot host, and generated SVG as a dependency. Use only when it communicates real, maintained information. Prefer repository-owned static assets for identity and core visuals.
