import pytest
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake
from app.remediation.exceptions import StaleFindingError, InvalidRemediationRecipe


def test_compile_pack_success():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    finding = intake.normalize_finding("FND-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(
        finding, explicit_recipe_id="refresh_venue_shadow_snapshot"
    )
    assert pack.pack_id.startswith("PACK-")
    assert pack.recipe.recipe_id == "refresh_venue_shadow_snapshot"


def test_compile_stale_finding_blocks():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    finding = intake.normalize_finding(
        "FND-1", "shadow_state", "low", {}, is_stale=True
    )
    with pytest.raises(StaleFindingError):
        compiler.compile_pack(finding)


def test_compile_invalid_recipe():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    finding = intake.normalize_finding("FND-1", "shadow_state", "low", {})
    with pytest.raises(InvalidRemediationRecipe):
        compiler.compile_pack(finding, explicit_recipe_id="non_existent_recipe")
