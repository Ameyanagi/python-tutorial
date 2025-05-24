# Python Tutorial Makefile
# Local testing and development commands

.PHONY: help install lint format typecheck test build clean all

# Default target
help:
	@echo "Available commands:"
	@echo "  install    - Install dependencies with uv"
	@echo "  lint       - Run linting checks"
	@echo "  format     - Format code"
	@echo "  typecheck  - Run type checking"
	@echo "  test       - Test that Python code compiles"
	@echo "  build      - Build all content locally"
	@echo "  clean      - Clean build artifacts"
	@echo "  all        - Run all checks and build"

# Install dependencies
install:
	@echo "Installing dependencies..."
	uv venv
	uv sync

# Lint code
lint:
	@echo "Running linting checks..."
	uv run ruff check .

# Format code
format:
	@echo "Formatting code..."
	uv run ruff format .

# Type checking
typecheck:
	@echo "Running type checks..."
	uv run pyright

# Test Python code compilation
test:
	@echo "Testing Python code compilation..."
	@echo "Checking shared code examples..."
	@for file in shared/code/*.py; do \
		echo "  Checking $$file..."; \
		uv run python -m py_compile "$$file" || exit 1; \
	done
	@echo "Checking multiprocessing chapter syntax..."
	@uv run python -c "exec(open('test_syntax.py').read())"

# Build content locally
build:
	@echo "Building main landing page..."
	uv run quarto render index.qmd
	@echo "Building English content..."
	uv run quarto render en/ --to html
	@echo "Building Japanese content..."
	uv run quarto render ja/ --to html

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -rf docs/
	rm -rf _freeze/
	rm -rf .quarto/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Run all checks
all: install lint format typecheck test
	@echo "All checks passed! Ready to build and deploy."

# Quick check (without install)
check: lint test
	@echo "Quick checks passed!"