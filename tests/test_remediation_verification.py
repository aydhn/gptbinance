from app.remediation.verification import VerificationEngine
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake
from app.remediation.enums import VerificationVerdict


def test_verification_engine():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="refresh_venue_shadow_snapshot")

    engine = VerificationEngine()
    verdict = engine.verify(pack)
    assert verdict.verdict == VerificationVerdict.FIXED
