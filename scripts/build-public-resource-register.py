#!/usr/bin/env python3
"""Create a copyright-safe public register from a private resource audit."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("audit", type=Path, help="private resource_audit.json")
    parser.add_argument("output", type=Path, help="public Markdown file to create")
    args = parser.parse_args()
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    groups: dict[str, list[dict]] = defaultdict(list)
    for item in audit["pdf_resources"]:
        groups["PDF resources"].append(item)
    for item in audit["zip_resources"]:
        groups["ZIP resources"].append(item)

    lines = [
        "# Game AI Pro Resource Register",
        "",
        "This copyright-safe register records the local corpus that informed this skill. It contains titles, routing, and evidence states only; it does not reproduce source text, code, figures, or extracted ZIP contents.",
        "",
        f"- PDFs: {audit['pdf_count']} | pages: {audit['pdf_pages']} | full-text extraction: {audit['pdf_full_text_extraction']}",
        f"- ZIP resources: {audit['zip_count']}",
        "- Default evidence state: source-indexed. A register entry is not, by itself, a validated design rule; see [evidence-governance.md](evidence-governance.md).",
        "",
    ]
    for name, items in groups.items():
        lines.extend([f"## {name}", ""])
        if name == "PDF resources":
            lines.extend(["| ID | Resource | Route | Initial disposition |", "|---|---|---|---|"])
            for item in items:
                lines.append(f"| {item['id']} | {esc(item['title'])} | `{item['skill_route']}` | `{item['integration_status']}` |")
        else:
            lines.extend(["| ID | Resource | Readable entries extracted |", "|---|---|---|"])
            for item in items:
                lines.append(f"| {item['id']} | {esc(item['relative_path'])} | {item['readable_text_extracted']} / {item['entry_count']} |")
        lines.append("")
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
