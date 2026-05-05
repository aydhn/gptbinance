from app.shadow_state.orders import detect_orders_drift
from app.shadow_state.twin import twin_assembler


def test_orders_drift():
    twin = twin_assembler.assemble_twin("test", "test")
    # Both are empty by default
    findings = detect_orders_drift(twin)
    assert len(findings) == 0
