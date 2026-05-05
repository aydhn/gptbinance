from app.data_governance import (
    ProvenanceStore,
    ProvenanceRecord,
    DatasetRef,
    DatasetType,
)
from datetime import datetime, timezone


def test_provenance_store():
    store = ProvenanceStore()
    ref = DatasetRef(
        dataset_id="d1", dataset_type=DatasetType.RAW_MARKET_DATA, version="v1"
    )
    record = ProvenanceRecord(
        dataset_ref=ref,
        build_time=datetime.now(timezone.utc),
        source_refs=[],
        transform_step_ids=["t1"],
        responsible_module="mod1",
    )
    store.record_provenance(record)
    fetched = store.get_provenance(ref)
    assert fetched.responsible_module == "mod1"
