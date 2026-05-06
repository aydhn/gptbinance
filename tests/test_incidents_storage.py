import pytest
import os
from app.incidents.storage import IncidentStorage
from app.incidents.models import IncidentRecord
from app.incidents.enums import IncidentSeverity, IncidentScopeType
from app.incidents.scopes import IncidentScope

def test_storage():
    storage = IncidentStorage(".test_incidents_storage")
    inc = IncidentRecord(
        incident_id="INC-123",
        severity=IncidentSeverity.INFO,
        scope=IncidentScope(type=IncidentScopeType.SYMBOL, ref="ETHUSDT", blast_radius_summary="Test")
    )
    storage.save(inc)

    loaded = storage.load("INC-123")
    assert loaded is not None
    assert loaded.incident_id == "INC-123"

    # cleanup
    import shutil
    shutil.rmtree(".test_incidents_storage", ignore_errors=True)
