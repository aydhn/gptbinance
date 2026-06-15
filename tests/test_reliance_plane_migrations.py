import pytest
from app.reliance_plane.migrations import process_migrations

def test_process_migrations():
    result = process_migrations({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "migrations"
