.PHONY: install test

install:
	uv install

run:
	uv run ./rook/main.py

test:
	uv run pytest --cov=rook tests/
