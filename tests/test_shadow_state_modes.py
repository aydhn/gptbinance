from app.shadow_state.modes import detect_modes_drift
from app.shadow_state.twin import twin_assembler


def test_modes_drift():
    twin = twin_assembler.assemble_twin("test", "test")
    findings = detect_modes_drift(twin)
    assert len(findings) == 0
