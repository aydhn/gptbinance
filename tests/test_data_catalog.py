from app.data_governance import GovernanceCatalog, GovernanceCatalogEntry, DatasetRef, DatasetType, TrustLevel
from datetime import datetime, timezone

def test_governance_catalog():
    catalog = GovernanceCatalog()
    ref = DatasetRef(dataset_id="d1", dataset_type=DatasetType.RAW_MARKET_DATA, version="v1")
    entry = GovernanceCatalogEntry(
        dataset_ref=ref,
        contract_id="c1",
        latest_quality_status=TrustLevel.TRUSTED,
        latest_trust_verdict=TrustLevel.TRUSTED,
        last_updated=datetime.now(timezone.utc)
    )
    catalog.update_entry(entry)
    fetched = catalog.get_entry(ref)
    assert fetched.contract_id == "c1"
