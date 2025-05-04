.PHONY: install test

install:
	uv install

test:
	uv run pytest --cov=rook tests/
