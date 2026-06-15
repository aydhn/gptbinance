from app.warranty_plane.registry import CanonicalWarrantyRegistry
from app.warranty_plane.models import WarrantyObject
from app.warranty_plane.enums import WarrantyClass
from app.warranty_plane.trust import TrustedWarrantyVerdictEngine
from app.warranty_plane.enums import WarrantyTrustVerdictEnum

def test_warranty_registry():
    registry = CanonicalWarrantyRegistry()
    obj = registry.register_warranty(
        warranty_id="wrnt_001",
        owner="owner_1",
        class_type=WarrantyClass.ATTESTED_STATE,
        scope="global"
    )
    assert obj.warranty_id == "wrnt_001"
    assert registry.get_warranty("wrnt_001") == obj
    assert len(registry.list_warranties()) == 1

def test_trusted_warranty_verdict_engine():
    engine = TrustedWarrantyVerdictEngine()

    # Clean case
    verdict_clean = engine.evaluate("wrnt_001", {"has_illusory_backing": False})
    assert verdict_clean.verdict == WarrantyTrustVerdictEnum.TRUSTED

    # Degraded case
    verdict_degraded = engine.evaluate("wrnt_002", {"has_illusory_backing": True})
    assert verdict_degraded.verdict == WarrantyTrustVerdictEnum.DEGRADED
