from app.shadow_state.drift import DriftDetector
from app.shadow_state.twin import twin_assembler
from app.shadow_state.enums import ShadowDomain


def test_drift_detector():
    detector = DriftDetector()
    twin = twin_assembler.assemble_twin("test", "test")
    findings = detector.detect_drift(twin, ShadowDomain.ORDERS)
    assert len(findings) == 0
