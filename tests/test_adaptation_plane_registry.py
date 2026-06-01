import pytest
from app.adaptation_plane.models import AdaptationRecord
from app.adaptation_plane.enums import AdaptationClass
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.exceptions import InvalidAdaptationObject

def test_adaptation_registry_integrity():
    registry = RegistryManager()
    record = AdaptationRecord(
        adaptation_id="ADAPT-001",
        class_type=AdaptationClass.DRIFT_CORRECTION,
        owner="security_team",
        scope="global",
        status="proposed"
    )

    registry.register_adaptation(record)
    assert registry.get_adaptation("ADAPT-001").class_type == AdaptationClass.DRIFT_CORRECTION

def test_adaptation_registry_overwrite_protection():
    registry = RegistryManager()
    record = AdaptationRecord(
        adaptation_id="ADAPT-002",
        class_type=AdaptationClass.SECURITY_HARDENING,
        owner="sec",
        scope="global",
        status="proposed"
    )
    registry.register_adaptation(record)

    with pytest.raises(InvalidAdaptationObject):
        registry.register_adaptation(record)

    record_invalid_update = AdaptationRecord(
        adaptation_id="ADAPT-002",
        class_type=AdaptationClass.COMPLIANCE_REPAIR, # Cannot change class
        owner="sec",
        scope="global",
        status="deployed"
    )
    with pytest.raises(InvalidAdaptationObject):
        registry.update_adaptation("ADAPT-002", record_invalid_update)
