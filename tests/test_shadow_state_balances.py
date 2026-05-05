from app.shadow_state.balances import detect_balances_drift
from app.shadow_state.twin import twin_assembler


def test_balances_drift():
    twin = twin_assembler.assemble_twin("test", "test")
    findings = detect_balances_drift(twin)
    assert len(findings) == 0
