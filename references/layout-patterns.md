# Layout patterns

Choose one opening system, then make it specific to the repository. These are compositions, not copy templates.

## 1. Product showcase

Best for web apps, desktop apps, mobile apps, and visual developer tools.

```text
┌──────────────────────────────────────────┐
│                identity                  │
│          owner orientation line          │
│       [primary actions / real links]     │
│                                          │
│         dominant product visual          │
│                                          │
│       restrained proof/status row        │
└──────────────────────────────────────────┘
```

Let the screenshot or demo carry the hook. Crop it around the differentiating interaction, not the entire application window.

## 2. Output-first tool

Best for CLIs, linters, formatters, build tools, automation, and terminal software.

```text
identity + owner orientation
small status row
┌──────────────────────────────────────────┐
│ representative command and real output  │
└──────────────────────────────────────────┘
compact navigation → install / usage / docs
```

Prefer authentic terminal output over a glossy illustration. Use a screenshot only when terminal styling is itself part of the product; otherwise use a code fence.

## 3. Developer library

Best for packages, SDKs, frameworks, and APIs.

```text
identity + owner orientation
version / CI / license (only real signals)
minimal owner-provided usage example
result or conceptual diagram
navigation into installation and reference
```

The usage example is the visual hook. Avoid a large decorative hero that pushes the API’s core shape below the opening.

## 4. System map

Best for infrastructure, platforms, protocols, distributed systems, and complex integrations.

```text
identity + owner orientation
one architecture / relationship diagram
legend or three concise owner-supplied anchors
links into concepts / deploy / operate
```

Keep the opening diagram conceptual. Move exhaustive component inventories to a later section.

## 5. Artifact gallery

Best for UI kits, themes, icon sets, templates, creative tools, and example collections.

```text
identity + owner orientation
curated 2-up or single-column montage
category navigation
usage / contribution path
```

Use consistent crops and aspect ratios. On narrow screens, prefer a vertical sequence over a wide HTML table.

## 6. Research or benchmark

Best for papers, datasets, experiments, and model repositories.

```text
identity / paper title
owner-supplied context and links
one result figure or method diagram
artifact/status links
abstract or repository map
```

Do not turn preliminary findings into marketing claims. Preserve captions, provenance, and accessible descriptions.

## Variation controls

Create distinction through:

- scale: dominant visual versus compact proof;
- alignment: centered opening versus editorial left alignment;
- density: sparse showcase versus information-forward tool;
- image treatment: full-bleed crop, framed screenshot, montage, diagram, or no image;
- rhythm: short opening followed by immediate technical depth, or visual proof followed by a guided path.

Do not create distinction through arbitrary emoji, excessive badges, rainbow dividers, or an unrelated generated banner.
