import pytest
from app.federation_plane.models import DelegatedAuthorityRecord
from app.federation_plane.delegation import DelegationManager
from app.federation_plane.exceptions import InvalidDelegatedAuthority


def test_delegation_manager_register():
    manager = DelegationManager()
    record = DelegatedAuthorityRecord(
        delegation_id="del-001",
        bounds="Strict bounds",
        expiry="2025-12-31",
        proof_notes="Tested bounds",
    )
    manager.register(record)
    assert manager.get_delegation("del-001") == record


def test_delegation_manager_without_bounds():
    manager = DelegationManager()
    record = DelegatedAuthorityRecord(
        delegation_id="del-002", bounds="", expiry="2025-12-31", proof_notes=""
    )
    with pytest.raises(InvalidDelegatedAuthority):
        manager.register(record)
