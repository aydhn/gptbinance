import pytest
from app.reliance_plane.releases_domain import process_releases_domain

def test_process_releases_domain():
    result = process_releases_domain({"strict_enforcement": True})
    assert result["status"] == "processed"
    assert result["module"] == "releases_domain"
