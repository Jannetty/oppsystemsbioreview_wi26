#!/usr/bin/env python3
"""
Convert Obsidian/Foam wikilinks [[...]] into GitHub-clickable Markdown links.

- [[path/to/file]]        -> [file](path/to/file.md)
- [[path/to/file|Label]]  -> [Label](path/to/file.md)
- [[file]] (no path)      -> [file](file.md)  (relative to the current doc)

Writes output to a separate file by default so Foam/Obsidian links stay intact.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


WIKILINK_RE = re.compile(r"\[\[([^\]\n]+?)\]\]")  # contents can't include ']' or newline


def ensure_md_suffix(target: str) -> str:
    target = target.strip()
    if not target:
        return target
    # Strip any anchor fragments from suffix handling: foo#bar
    if "#" in target:
        base, frag = target.split("#", 1)
        base = base.strip()
        if base and not base.lower().endswith(".md"):
            base += ".md"
        return f"{base}#{frag}"
    if not target.lower().endswith(".md"):
        target += ".md"
    return target


def wikilink_to_markdown(match: re.Match, current_doc_dir: Path) -> str:
    raw = match.group(1).strip()

    # Support [[target|label]]
    if "|" in raw:
        target, label = raw.split("|", 1)
        target = target.strip()
        label = label.strip()
        if not label:
            label = target
    else:
        target = raw
        label = raw

    # Ignore empty
    if not target:
        return match.group(0)

    # If target is a URL, leave alone
    if target.startswith("http://") or target.startswith("https://"):
        return match.group(0)

    # If target has no slash, interpret as relative to this doc
    # If it has slashes, keep as-is (already relative path in your outline)
    if "/" not in target and "\\" not in target:
        link_path = ensure_md_suffix(target)
    else:
        link_path = ensure_md_suffix(target)

    # Display text: for common pattern [[paper_notes_short/foo]]
    # label should be "foo" not "paper_notes_short/foo" unless user gave a label.
    if label == raw and ("/" in label or "\\" in label):
        label = Path(label).name

    return f"[{label}]({link_path})"


def convert_text(text: str, current_doc_path: Path) -> str:
    doc_dir = current_doc_path.parent

    def _repl(m: re.Match) -> str:
        return wikilink_to_markdown(m, doc_dir)

    return WIKILINK_RE.sub(_repl, text)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--in", dest="infile", required=True, help="Input markdown file")
    parser.add_argument("--out", dest="outfile", required=True, help="Output markdown file")
    args = parser.parse_args()

    in_path = Path(args.infile)
    out_path = Path(args.outfile)

    text = in_path.read_text(encoding="utf-8")
    converted = convert_text(text, in_path)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(converted, encoding="utf-8")


if __name__ == "__main__":
    main()