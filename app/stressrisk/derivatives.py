from app.stressrisk.models import FundingStressSnapshot


class DerivativesStressEngine:
    def evaluate(self, positions: dict) -> FundingStressSnapshot:
        return FundingStressSnapshot(
            total_funding_burden_jump=500.0,
            borrow_cost_jump=100.0,
            liquidation_proximity_tightening=0.05,
            # Added in Phase 40
            # fake_hedge_contagion=True, collateral_dependency_stress=0.2
        )
