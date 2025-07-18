PYTHON = poetry run

.PHONY: dev lint format type-check test all

dev:
	$(PYTHON) uvicorn app.main:app --reload

lint:
	$(PYTHON) ruff check .

format:
	$(PYTHON) ruff check . --fix

type-check:
	$(PYTHON) mypy --explicit-package-bases app

test:
	$(PYTHON) pytest

all: lint type-check test
