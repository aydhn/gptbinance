from app.shadow_state.classification import DriftClassifier
from app.shadow_state.models import DriftFinding
from app.shadow_state.enums import ShadowDomain, DriftType, DriftSeverity


def test_drift_classifier():
    classifier = DriftClassifier()
    assert classifier.evaluate_verdict([]).value == "clean"

    finding = DriftFinding(
        finding_id="1",
        domain=ShadowDomain.ORDERS,
        drift_type=DriftType.MISSING_LOCAL,
        severity=DriftSeverity.BLOCKER,
        description="test",
    )
    assert classifier.evaluate_verdict([finding]).value == "critical_divergence"
