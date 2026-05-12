import pytest
from app.observability_plane.ingestion import IngestionRegistry
from app.observability_plane.models import TelemetryIngestionRecord

def test_ingestion_registry():
    reg = IngestionRegistry()
    reg.register_ingestion(TelemetryIngestionRecord(ingestion_id="i1", source_ref="sys1", lag_ms=100))
    assert reg.get_ingestion("i1").lag_ms == 100
