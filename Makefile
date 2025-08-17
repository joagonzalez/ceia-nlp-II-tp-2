install:
	uv sync

run:
	uv run run.py

typehint:
	uv run mypy src/ tests/

test-local:
	uv run pytest tests/ -v --cov

test:
	uv run pytest tests/ -v --cov --cov-report=xml:coverage.xml

lint:
	uv run ruff check src/ tests/ 

format:
	uv run ruff check src/ tests/ --fix

clean:
	rm -rf .*_cache coverage.xml .*coverage site report

checklist: typehint lint test clean

code-quality: typehint lint clean

coverage-publish:
	uv run coveralls

.PHONY: checklist