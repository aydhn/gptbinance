from app.remediation.simulation import DryRunEngine
from app.remediation.compiler import RemediationCompiler
from app.remediation.findings import FindingIntake


def test_simulation_read_only():
    compiler = RemediationCompiler()
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {})
    pack = compiler.compile_pack(f1, explicit_recipe_id="refresh_venue_shadow_snapshot")

    engine = DryRunEngine()
    res = engine.simulate(pack)

    assert res.is_safe is True
    assert "sync with venue" in res.expected_deltas[0]
