#!/bin/bash
set -e

# Run tests
poetry run pytest tests/test_jurisdiction_plane_registry.py > /dev/null 2>&1

# Run linting
poetry run flake8 app/jurisdiction_plane > /dev/null 2>&1

echo "Pre-commit passed"
