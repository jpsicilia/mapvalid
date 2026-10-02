.PHONY: install test lint format

install:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

lint:
	ruff check .
	ruff format --check .

format:
	ruff check --fix .
	ruff format .
