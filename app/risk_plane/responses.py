from app.risk_plane.models import RiskState, DrawdownState, MarginState
from app.risk_plane.enums import BreachClass, DrawdownClass, ResponseAction
from app.performance_plane.opportunity import OpportunitySurfaceBuilder
from app.performance_plane.enums import OpportunityClass
from decimal import Decimal


class ResponseIntentEngine:
    @staticmethod
    def generate_responses(
        state: RiskState, drawdown: DrawdownState, margin: MarginState
    ):
        responses = []
        if drawdown.drawdown_class in [DrawdownClass.CRITICAL, DrawdownClass.SEVERE]:
            responses.append(ResponseAction.FREEZE)
        elif drawdown.drawdown_class == DrawdownClass.ELEVATED:
            responses.append(ResponseAction.NO_NEW_EXPOSURE)
        return responses

    @staticmethod
    def export_risk_blocked_opportunity(
        symbol: str, intended_qty: Decimal, expected_price: Decimal, currency: str
    ):
        value = intended_qty * expected_price
        return OpportunitySurfaceBuilder.build(
            opportunity_class=OpportunityClass.RISK_BLOCKED,
            estimated_value=value,
            currency=currency,
            confidence_score=0.6,
            caveats=[
                "Opportunity foregone due to active risk blocks (e.g., freeze or no_new_exposure)."
            ],
        )
