#!/usr/bin/env python3
"""Normalize Markdown frontmatter to the repository YAML style."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.yaml_style import build_yaml, dump_frontmatter  # noqa: E402

FRONTMATTER = re.compile(r"^---[ \t]*\n(.*?)\n---[ \t]*\n", re.DOTALL)


def normalize_text(text: str) -> tuple[str, bool]:
    match = FRONTMATTER.match(text)
    if not match:
        return text, False

    yaml_text = match.group(1)
    body = text[match.end() :]
    data = build_yaml().load(yaml_text)
    if data is None:
        return text, False

    new_yaml = dump_frontmatter(data)
    new_text = f"---\n{new_yaml}---\n" + body
    return new_text, new_text != text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    docs_dir = project_root / args.docs_dir
    changed: list[Path] = []

    for md_file in sorted(docs_dir.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        new_text, did_change = normalize_text(text)
        if not did_change:
            continue
        changed.append(md_file)
        if args.apply:
            md_file.write_text(new_text, encoding="utf-8")

    print(f"Scanned {sum(1 for _ in docs_dir.rglob('*.md'))} markdown files")
    print(f"Files with style drift: {len(changed)}")

    if changed and not args.apply:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
