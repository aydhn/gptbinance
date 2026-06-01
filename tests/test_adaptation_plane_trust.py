import pytest
from app.adaptation_plane.models import AdaptationRecord
from app.adaptation_plane.enums import AdaptationClass, TrustVerdict
from app.adaptation_plane.registry import RegistryManager
from app.adaptation_plane.trust import TrustManager

def test_patch_theater_detection():
    registry = RegistryManager()
    trust_manager = TrustManager(registry)

    # Deployed but no package and no verification -> patch theater
    record = AdaptationRecord(
        adaptation_id="ADAPT-004",
        class_type=AdaptationClass.DRIFT_CORRECTION,
        owner="test",
        scope="local",
        status="deployed"
    )
    registry.register_adaptation(record)

    verdict = trust_manager.generate_verdict("ADAPT-004")
    assert verdict.status == TrustVerdict.BLOCKED
    assert "detected" in verdict.breakdown.get("patch_theater", "")

def test_missing_evidence_degradation():
    registry = RegistryManager()
    trust_manager = TrustManager(registry)

    # Proposed but missing trigger, hypothesis, package
    record = AdaptationRecord(
        adaptation_id="ADAPT-005",
        class_type=AdaptationClass.DRIFT_CORRECTION,
        owner="test",
        scope="local",
        status="proposed"
    )
    registry.register_adaptation(record)

    verdict = trust_manager.generate_verdict("ADAPT-005")
    assert verdict.status == TrustVerdict.DEGRADED
    assert verdict.breakdown["trigger_clarity"] == "missing"
