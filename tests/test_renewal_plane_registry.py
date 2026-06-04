import pytest
from app.renewal_plane.registry import CanonicalRenewalRegistry
from app.renewal_plane.models import RenewalObject
from app.renewal_plane.enums import RenewalClass, ContinuationClass
from datetime import datetime

def test_registry_registration():
    registry = CanonicalRenewalRegistry()
    obj = RenewalObject(
        renewal_id="R-001",
        renewal_class=RenewalClass.MANDATE_RENEWAL,
        owner="admin",
        scope="global",
        continuation_posture=ContinuationClass.FULL_RENEWAL,
        reauthorization_posture="verified",
        created_at=datetime.utcnow()
    )
    registry.register(obj)

    assert registry.get("R-001") == obj
    assert len(registry.list_all()) == 1
    assert registry.has_stale_continuations() == False

def test_registry_stale_detection():
    registry = CanonicalRenewalRegistry()
    obj = RenewalObject(
        renewal_id="R-002",
        renewal_class=RenewalClass.MANDATE_RENEWAL,
        owner="admin",
        scope="global",
        continuation_posture=ContinuationClass.PROVISIONAL,
        reauthorization_posture="unverified",
        created_at=datetime.utcnow()
    )
    registry.register(obj)

    assert registry.has_stale_continuations() == True
