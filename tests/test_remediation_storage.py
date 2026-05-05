from app.remediation.storage import RemediationStorage
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake


def test_storage():
    storage = RemediationStorage()
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="refresh_venue_shadow_snapshot")

    storage.save_pack(pack)
    retrieved = storage.get_pack(pack.pack_id)
    assert retrieved is not None
    assert retrieved.pack_id == pack.pack_id
