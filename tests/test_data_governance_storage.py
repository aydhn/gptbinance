from app.data_governance import GovernanceStorage
import os

def test_governance_storage(tmp_path):
    storage = GovernanceStorage(base_path=str(tmp_path))
    data = {"key": "value"}
    storage.save_contract("c1", data)
    fetched = storage.get_contract("c1")
    assert fetched == data
