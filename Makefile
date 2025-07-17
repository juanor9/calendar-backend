dev:
	poetry run uvicorn app.main:app --reload

lint:
	poetry run ruff check .

type-check:
	poetry run mypy --explicit-package-bases app

