# Contributing to mapvalid

Thanks for your interest! Issues and pull requests are welcome.

## Before you start

Please open an issue describing the bug or the idea before sending a large pull
request, so we can agree on the approach.

## Setting up

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
pre-commit install
```

## Rules

- Every change comes with tests. Methods ported from CAST are tested against
  reference outputs in `tests/reference/`.
- Code is formatted and linted with ruff (run automatically by pre-commit).
- Public functions have type hints and numpy-style docstrings.
- Keep commits small, with descriptive messages.
- Record design decisions in `docs/decisions/`.

## Running checks

```bash
ruff check .
ruff format --check .
pytest
```
