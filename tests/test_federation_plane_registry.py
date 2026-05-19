import pytest
from app.federation_plane.models import FederationRecord
from app.federation_plane.enums import FederationClass
from app.federation_plane.registry import CanonicalFederationRegistry
from app.federation_plane.exceptions import FederationStorageError


def test_canonical_federation_registry_register():
    registry = CanonicalFederationRegistry()
    record = FederationRecord(
        federation_id="fed-001",
        federation_class=FederationClass.MULTI_TENANT,
        purpose="Testing tenant federation",
        participating_domains=["dom-1"],
        participating_tenants=["ten-1"],
        trust_translation_notes="none",
    )
    registry.register_federation(record)
    assert registry.get_federation("fed-001") == record


def test_canonical_federation_registry_undocumented_id():
    registry = CanonicalFederationRegistry()
    record = FederationRecord(
        federation_id="",
        federation_class=FederationClass.MULTI_TENANT,
        purpose="Testing",
        participating_domains=[],
        participating_tenants=[],
        trust_translation_notes="none",
    )
    with pytest.raises(FederationStorageError):
        registry.register_federation(record)
