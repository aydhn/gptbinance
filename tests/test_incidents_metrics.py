import pytest
from app.incidents.metrics import IncidentMetrics
from app.incidents.storage import IncidentStorage
from app.incidents.repository import IncidentRepository


def test_metrics():
    repo = IncidentRepository(IncidentStorage(".test_incidents_metrics"))
    metrics = IncidentMetrics(repo)
    summary = metrics.compute_summary()
    assert "mttd" in summary
    assert "mttr" in summary

    # cleanup
    import shutil

    shutil.rmtree(".test_incidents_metrics", ignore_errors=True)
