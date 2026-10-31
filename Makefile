.PHONY: readme check

readme:
	uv run scripts/build.py

check:
	uv run scripts/build.py --check
