from decimal import Decimal
from app.performance_plane.opportunity import OpportunitySurfaceBuilder
from app.performance_plane.enums import OpportunityClass


def test_opportunity_confidence_classes():
    o = OpportunitySurfaceBuilder.build(
        opportunity_class=OpportunityClass.FOREGONE_SAME_ASSUMPTIONS,
        estimated_value=Decimal("50.0"),
        currency="USD",
        confidence_score=0.9,
    )
    assert len(o.caveats) == 0
    assert o.confidence_score == 0.9


def test_risk_blocked_opportunity_caveats():
    o = OpportunitySurfaceBuilder.build(
        opportunity_class=OpportunityClass.RISK_BLOCKED,
        estimated_value=Decimal("150.0"),
        currency="USD",
        confidence_score=0.6,
        caveats=["Blocked by freeze"],
    )
    assert "Low confidence opportunity, highly counterfactual." in o.caveats
    assert "Blocked by freeze" in o.caveats
