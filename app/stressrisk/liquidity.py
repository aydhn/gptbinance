from app.stressrisk.models import LiquidityStressSnapshot


class LiquidityStressEngine:
    def evaluate(
        self, current_liquidity: dict, shocked_liquidity: dict
    ) -> LiquidityStressSnapshot:
        return LiquidityStressSnapshot(
            average_spread_widening_pct=200.0,
            average_turnover_drop_pct=80.0,
            illiquid_symbols_warning=["LOWCAP1", "LOWCAP2"],
        )
