from app.risk.explain import RiskExplainer
from app.risk.models import RiskDecision, RiskRejectionReason, PositionSizingResult
from app.risk.enums import RiskVerdict, VetoSeverity, SizingMode


def test_explainer():
    decision = RiskDecision(
        verdict=RiskVerdict.REJECT,
        rationale="Too big",
        sizing=PositionSizingResult(
            requested_size=2.0,
            approved_size=0.0,
            notional_value=0.0,
            sizing_mode=SizingMode.FIXED_FRACTION,
        ),
        rejection_reasons=[
            RiskRejectionReason(
                source="P1", severity=VetoSeverity.HIGH, rationale="Exceeded"
            )
        ],
    )
    explainer = RiskExplainer()
    res = explainer.explain(decision)
    assert "Verdict: REJECT" in res
    assert "Too big" in res
    assert "Requested Size: 2.0" in res
    assert "Exceeded" in res
