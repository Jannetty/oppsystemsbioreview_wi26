#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys


TITLE_RE = re.compile(r"(?m)^\#\s+(.+?)\s*$")
SHORT_NOTE_RE = re.compile(r"(?ms)^## Short note\s*\n(.*?)(?=^##\s|\Z)")


def extract_title(text: str, src: Path) -> str:
    m = TITLE_RE.search(text)
    if not m:
        raise ValueError(f"{src}: could not find a top-level '# Title' header.")
    return m.group(1).strip()


def extract_short_note_body(text: str, src: Path) -> str:
    m = SHORT_NOTE_RE.search(text)
    if not m:
        raise ValueError(f"{src}: could not find a '## Short note' section.")
    return m.group(1).strip()


def main() -> int:
    repo_root = Path.cwd()

    long_dir = repo_root / "paper_notes_long"
    short_dir = repo_root / "paper_notes_short"

    if not long_dir.exists():
        print(f"ERROR: missing directory: {long_dir}", file=sys.stderr)
        return 2

    short_dir.mkdir(parents=True, exist_ok=True)

    long_files = sorted(long_dir.glob("*.md"))
    if not long_files:
        print(f"No .md files found in {long_dir}")
        return 0

    ok = 0
    failed = 0

    for src in long_files:
        try:
            text = src.read_text(encoding="utf-8")

            title = extract_title(text, src)
            short_body = extract_short_note_body(text, src)

            out_text = (
                f"# {title}\n\n"
                f"## Short note\n\n"
                f"{short_body}\n"
            )

            dst = short_dir / src.name
            dst.write_text(out_text, encoding="utf-8")
            ok += 1

        except Exception as e:
            failed += 1
            print(f"[FAIL] {src.name}: {e}", file=sys.stderr)

    print(f"Done. Wrote {ok} short notes to {short_dir}. Failed: {failed}.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())