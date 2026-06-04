#!/usr/bin/env python3
"""Validate local Markdown links.
External HTTP links are counted but not fetched so this check remains deterministic offline.
"""
from __future__ import annotations
from pathlib import Path
from urllib.parse import unquote, urlparse
import re
import sys
ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
BARE_URL_RE = re.compile(r"https?://[^\s)]+")

def files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)

def slugify(title: str) -> str:
    title = re.sub(r"[`*_\[\]()]", "", title.strip().lower())
    title = re.sub(r"[^a-z0-9\s-]", "", title)
    title = re.sub(r"\s+", "-", title)
    return re.sub(r"-+", "-", title).strip("-")

def has_anchor(path: Path, anchor: str) -> bool:
    if not anchor:
        return True
    headings = re.findall(r"^#{1,6}\s+(.+)$", path.read_text(encoding="utf-8"), flags=re.MULTILINE)
    return unquote(anchor).lower() in {slugify(h) for h in headings}

def check(source: Path, target: str) -> str | None:
    parsed = urlparse(target)
    if parsed.scheme in {"http", "https", "mailto"}:
        return None
    if target.startswith("#"):
        return None if has_anchor(source, target[1:]) else f"missing anchor {target} in {source.relative_to(ROOT)}"
    dest_text = unquote(parsed.path)
    if not dest_text:
        return None
    dest = (source.parent / dest_text).resolve()
    try:
        dest.relative_to(ROOT)
    except ValueError:
        return f"link escapes repository: {source.relative_to(ROOT)} -> {target}"
    if not dest.exists():
        return f"missing file: {source.relative_to(ROOT)} -> {target}"
    if parsed.fragment and dest.suffix == ".md" and not has_anchor(dest, parsed.fragment):
        return f"missing anchor: {source.relative_to(ROOT)} -> {target}"
    return None

def main() -> int:
    failures = []
    local = 0
    external = 0
    for path in files():
        text = path.read_text(encoding="utf-8")
        markdown_external_targets = set()
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if urlparse(target).scheme in {"http", "https", "mailto"}:
                markdown_external_targets.add(target)
                external += 1
                continue
            local += 1
            failure = check(path, target)
            if failure:
                failures.append(failure)
        for match in BARE_URL_RE.finditer(text):
            if match.group(0) not in markdown_external_targets:
                external += 1
    if failures:
        print("Link check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"Link check passed: {local} local links valid, {external} external links skipped.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
