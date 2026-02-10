.PHONY: short-notes outline

short-notes:
	./scripts/generate_short_notes.py

PY := python3

outline:
	$(PY) scripts/foam_to_github_links.py --in outline_foam.md --out outline.md