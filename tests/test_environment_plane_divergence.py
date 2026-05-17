import pytest
from app.environment_plane.divergence import report_divergence

def test_report_divergence():
    div = report_divergence("LOW", "None")
    assert div.severity == "LOW"
    assert div.blast_radius == "None"
