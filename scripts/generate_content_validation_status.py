#!/usr/bin/env python3
"""Generate content validation dashboard from frontmatter metadata."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.content_scope import (  # noqa: E402
    NAVIGATION_INDEXES,
    SCANNED_SECTIONS,
    TAUTOLOGICAL_CLAIM_MARKER,
    is_in_scope,
    is_tautological_text,
)

ICON_VERIFIED = "✅ Verified"
ICON_PENDING = "⚠️ Pending Review"
ICON_UNVERIFIED = "➖ Unverified"
ICON_NO_META = "❓ No Metadata"


def parse_frontmatter(filepath: Path) -> dict[str, Any] | None:
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def scan_documents(docs_dir: Path) -> list[dict[str, Any]]:
    documents: list[dict[str, Any]] = []
    for section in sorted(SCANNED_SECTIONS):
        section_dir = docs_dir / section
        if not section_dir.exists():
            continue
        for md_file in section_dir.rglob("*.md"):
            rel_path = md_file.relative_to(docs_dir)
            if not is_in_scope(rel_path):
                continue

            frontmatter = parse_frontmatter(md_file) or {}
            cv = frontmatter.get("content_validation", {}) or {}
            claims = cv.get("core_claims", []) if isinstance(cv, dict) else []
            documents.append(
                {
                    "rel_path": str(rel_path),
                    "section": rel_path.parts[0],
                    "title": md_file.stem.replace("-", " ").title(),
                    "status": cv.get("status", "no_metadata")
                    if isinstance(cv, dict)
                    else "no_metadata",
                    "last_reviewed": cv.get("last_reviewed")
                    if isinstance(cv, dict)
                    else None,
                    "claims": len(claims) if isinstance(claims, list) else 0,
                    "verified_claims": sum(
                        1
                        for claim in claims
                        if isinstance(claim, dict) and claim.get("verified", False)
                    )
                    if isinstance(claims, list)
                    else 0,
                    "tautological_claims": sum(
                        1
                        for claim in claims
                        if isinstance(claim, dict)
                        and is_tautological_text(claim.get("claim"))
                    )
                    if isinstance(claims, list)
                    else 0,
                }
            )
    return documents


def count_mermaid_diagrams(docs_dir: Path) -> int:
    count = 0
    for md_file in docs_dir.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        count += len(re.findall(r"^```mermaid\s*$", text, re.MULTILINE))
    return count


def status_icon(status: str) -> str:
    return {
        "verified": ICON_VERIFIED,
        "pending_review": ICON_PENDING,
        "unverified": ICON_UNVERIFIED,
        "no_metadata": ICON_NO_META,
    }.get(status, ICON_NO_META)


def generate_dashboard(
    documents: list[dict[str, Any]], docs_dir: Path, today: date
) -> str:
    total = len(documents)
    verified = sum(1 for d in documents if d["status"] == "verified")
    pending = sum(1 for d in documents if d["status"] == "pending_review")
    unverified = sum(1 for d in documents if d["status"] == "unverified")
    no_meta = sum(1 for d in documents if d["status"] == "no_metadata")
    diagrams = count_mermaid_diagrams(docs_dir)

    nav_examples = ", ".join(f"`docs/{p}`" for p in sorted(NAVIGATION_INDEXES))
    lines = [
        "---",
        "description: Content-validation dashboard for in-scope Azure Storage factual-claim pages and the metadata status recorded on each page.",
        "content_sources:",
        "  diagrams:",
        "    - id: reference-content-validation-status",
        "      type: pie",
        "      source: self-generated",
        '      justification: "Auto-generated dashboard summarizing content_validation metadata across in-scope documents."',
        "      based_on:",
        "        - https://learn.microsoft.com/en-us/azure/storage/",
        "---",
        "",
        "# Content Validation Status",
        "",
        "This page tracks `content_validation` metadata for in-scope factual-claim documents under `docs/platform/`, `docs/best-practices/`, `docs/operations/`, and `docs/troubleshooting/`. Start-here pages, tutorials, reference pages, contributing docs, and navigation-only indexes are intentionally out of scope.",
        "",
        f"Navigation-only indexes excluded from this dashboard: {nav_examples}.",
        "",
        "## Summary",
        "",
        f"*Generated: {today.isoformat()}*",
        "",
        "| Content Type | Total | Verified | Pending | Unverified | No Metadata |",
        "|---|---:|---:|---:|---:|---:|",
        f"| Mermaid Diagrams | {diagrams} | {diagrams} | 0 | 0 | 0 |",
        f"| In-Scope Factual-Claim Documents | {total} | {verified} | {pending} | {unverified} | {no_meta} |",
        "",
        "<!-- diagram-id: reference-content-validation-status -->",
        "```mermaid",
        "pie title In-Scope Document Validation Status",
    ]
    if verified:
        lines.append(f'    "Verified" : {verified}')
    if pending:
        lines.append(f'    "Pending Review" : {pending}')
    if unverified:
        lines.append(f'    "Unverified" : {unverified}')
    if no_meta:
        lines.append(f'    "No Metadata" : {no_meta}')
    lines.extend(
        [
            "```",
            "",
            "## By Section",
            "",
        ]
    )

    by_section: dict[str, list[dict[str, Any]]] = {}
    for document in documents:
        by_section.setdefault(document["section"], []).append(document)

    for section in ["platform", "best-practices", "operations", "troubleshooting"]:
        if section not in by_section:
            continue
        lines.extend(
            [
                f"### {section.replace('-', ' ').title()}",
                "",
                "| Document | Status | Claims | Last Reviewed |",
                "|---|---|---|---|",
            ]
        )
        for document in sorted(by_section[section], key=lambda item: item["rel_path"]):
            claims = (
                f"{document['verified_claims']}/{document['claims']}"
                if document["claims"]
                else "—"
            )
            last_reviewed = document["last_reviewed"] or "—"
            lines.append(
                f"| [{document['title']}](../{document['rel_path']}) | {status_icon(document['status'])} | {claims} | {last_reviewed} |"
            )
        lines.append("")

    lines.extend(
        [
            "## Validation Status Values",
            "",
            "| Status | Description |",
            "|---|---|",
            "| `verified` | All core claims on the page were confirmed against Microsoft Learn sources. |",
            "| `pending_review` | The page has concrete core claims and source URLs, but one or more claims still need claim-level confirmation. |",
            "| `unverified` | The page carries metadata but no claim-level review has been completed yet. |",
            "",
            "## How to Update",
            "",
            "Add a `content_validation` block only to in-scope factual-claim pages:",
            "",
            "```yaml",
            "---",
            "content_validation:",
            "  status: pending_review",
            f"  last_reviewed: {today.isoformat()}",
            "  reviewer: agent",
            "  core_claims:",
            '    - claim: "Azure Storage supports locally redundant, zone-redundant, geo-redundant, and geo-zone-redundant replication options."',
            "      source: https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy",
            "      verified: false",
            "---",
            "```",
            "",
            f"The generator fails if a claim contains the placeholder marker `{TAUTOLOGICAL_CLAIM_MARKER}`.",
            "",
            "## See Also",
            "",
            "- [Validation Status](validation-status.md)",
            "- [Reference Index](index.md)",
            "",
            "## Sources",
            "",
            "- <https://learn.microsoft.com/en-us/azure/storage/>",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate content validation status dashboard"
    )
    parser.add_argument("--docs-dir", type=Path, default=Path("docs"))
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/reference/content-validation-status.md"),
    )
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    docs_dir = project_root / args.docs_dir
    output_path = project_root / args.output

    documents = scan_documents(docs_dir)
    tautological = [doc for doc in documents if doc["tautological_claims"]]
    if tautological:
        names = ", ".join(doc["rel_path"] for doc in tautological)
        raise SystemExit(f"Tautological core claims found: {names}")

    dashboard = generate_dashboard(documents, docs_dir, date.today())
    output_path.write_text(dashboard, encoding="utf-8")
    print(f"Scanned {len(documents)} in-scope documents, generated {output_path}")


if __name__ == "__main__":
    main()
