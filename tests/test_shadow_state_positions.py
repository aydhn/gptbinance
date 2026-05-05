from app.shadow_state.positions import detect_positions_drift
from app.shadow_state.twin import twin_assembler


def test_positions_drift():
    twin = twin_assembler.assemble_twin("test", "test")
    findings = detect_positions_drift(twin)
    assert len(findings) == 0
