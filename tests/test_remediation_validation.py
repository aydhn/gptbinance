import pytest
from app.remediation.validation import PackValidator
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake
from app.remediation.exceptions import StaleFindingError


def test_validator_rejects_stale():
    compiler = RemediationCompiler()
    intake = FindingIntake()

    # Pack created when not stale
    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="refresh_venue_shadow_snapshot")

    # Mutate to stale for test
    pack.finding_ref.is_stale = True

    validator = PackValidator()
    with pytest.raises(StaleFindingError):
        validator.validate(pack)
