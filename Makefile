.PHONY: run test

run:
	uv run ./rook/main.py

test:
	uv run pytest --cov=rook tests/
