#!/usr/bin/env python3
"""Audit structural signals that commonly affect a GitHub README design."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse


IMAGE_MD = re.compile(r"!\[([^\]]*)\]\(([^\s)]+)(?:\s+[^)]*)?\)")
IMAGE_HTML = re.compile(r"<img\b[^>]*?src=[\"']([^\"']+)[\"'][^>]*>", re.I)
ALT_HTML = re.compile(r"\balt=[\"']([^\"']*)[\"']", re.I)
BADGE = re.compile(r"(?:shields\.io|badge\.svg|badge\.fury\.io|codecov\.io|coveralls\.io)", re.I)
HEADING = re.compile(r"^(#{1,6})\s+\S", re.M)


def add(results: list[tuple[str, str]], level: str, message: str) -> None:
    results.append((level, message))


def local_target(target: str) -> str | None:
    target = target.strip("<>")
    parsed = urlparse(target)
    if parsed.scheme or target.startswith("//") or target.startswith("#"):
        return None
    return unquote(parsed.path)


def audit(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    results: list[tuple[str, str]] = []

    markdown_h1 = len(re.findall(r"^#\s+\S", text, re.M))
    html_h1 = len(re.findall(r"<h1\b[^>]*>.*?</h1>", text, re.I | re.S))
    h1_count = markdown_h1 + html_h1
    if h1_count != 1:
        add(results, "WARN", f"Expected one Markdown H1; found {h1_count}.")

    headings = [(len(m.group(1)), text.count("\n", 0, m.start()) + 1) for m in HEADING.finditer(text)]
    for (previous, _), (current, line) in zip(headings, headings[1:]):
        if current > previous + 1:
            add(results, "WARN", f"Heading hierarchy skips from H{previous} to H{current} near line {line}.")

    opening = "\n".join(lines[:50])
    badge_count = len(BADGE.findall(opening))
    if badge_count > 6:
        add(results, "WARN", f"Opening contains about {badge_count} badge URLs; aim for 3–6 high-signal badges or fewer.")

    first_h2 = next((i + 1 for i, line in enumerate(lines) if re.match(r"^##\s+\S", line)), None)
    if first_h2 and first_h2 > 90:
        add(results, "WARN", f"First H2 begins at line {first_h2}; the opening may delay substantive content.")

    if re.search(r"<(?:style|script)\b", text, re.I) or re.search(r"\sstyle=[\"']", text, re.I):
        add(results, "ERROR", "README contains CSS or script-dependent markup that GitHub may sanitize.")

    centered_words = 0
    for block in re.findall(r"<(?:div|p)\b[^>]*align=[\"']center[\"'][^>]*>(.*?)</(?:div|p)>", text, re.I | re.S):
        centered_words += len(re.sub(r"<[^>]+>", " ", block).split())
    if centered_words > 100:
        add(results, "WARN", f"Centered blocks contain roughly {centered_words} words; center the hero, not long prose.")

    for alt, target in IMAGE_MD.findall(text):
        if not alt.strip():
            add(results, "INFO", f"Image `{target}` has empty alt text; confirm it is decorative.")
        local = local_target(target)
        if local and not (path.parent / local).resolve().exists():
            add(results, "ERROR", f"Local image does not exist relative to README: {target}")

    for match in IMAGE_HTML.finditer(text):
        tag, target = match.group(0), match.group(1)
        if not ALT_HTML.search(tag):
            add(results, "WARN", f"HTML image lacks an alt attribute: {target}")
        local = local_target(target)
        if local and not (path.parent / local).resolve().exists():
            add(results, "ERROR", f"Local HTML image does not exist relative to README: {target}")

    visible_placeholders = re.findall(r"(?:YOUR[_ -]|TODO:?|TBD|Lorem ipsum|example\.com)", text, re.I)
    if visible_placeholders:
        add(results, "WARN", f"Found {len(visible_placeholders)} possible visible placeholder(s). Use invisible OWNER comments instead.")

    remote_images = [target for _, target in IMAGE_MD.findall(text) if urlparse(target.strip("<>")).scheme]
    remote_images += [m.group(1) for m in IMAGE_HTML.finditer(text) if urlparse(m.group(1)).scheme]
    if len(remote_images) > 10:
        add(results, "INFO", f"README depends on {len(remote_images)} remote images; consider repository-owned core visuals.")

    if not results:
        add(results, "PASS", "No structural issues detected. Complete the rendered visual review manually.")
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", type=Path, help="Path to README.md")
    args = parser.parse_args()
    if not args.readme.is_file():
        parser.error(f"File not found: {args.readme}")

    results = audit(args.readme)
    for level, message in results:
        print(f"[{level}] {message}")
    errors = sum(level == "ERROR" for level, _ in results)
    warnings = sum(level == "WARN" for level, _ in results)
    print(f"\nSummary: {errors} error(s), {warnings} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
