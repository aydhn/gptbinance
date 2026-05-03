from typing import Dict, Any, List
from app.stressrisk.models import ShockVector
from app.stressrisk.enums import ShockType


class ShockEngine:
    def apply_shocks(
        self, current_state: Dict[str, Any], shocks: List[ShockVector]
    ) -> Dict[str, Any]:
        shocked = current_state.copy()
        for shock in shocks:
            if shock.shock_type == ShockType.PRICE and "price" in shocked:
                shocked["price"] = (
                    shocked["price"] * shock.value_multiplier + shock.absolute_addition
                )
            elif shock.shock_type == ShockType.LIQUIDITY and "liquidity" in shocked:
                shocked["liquidity"] = shocked["liquidity"] * shock.value_multiplier
            elif shock.shock_type == ShockType.SPREAD and "spread" in shocked:
                shocked["spread"] = shocked["spread"] * shock.value_multiplier
            elif shock.shock_type == ShockType.CORRELATION and "correlation" in shocked:
                shocked["correlation"] = min(
                    1.0, shocked["correlation"] + shock.absolute_addition
                )
            elif shock.shock_type == ShockType.FUNDING and "funding_rate" in shocked:
                shocked["funding_rate"] = (
                    shocked["funding_rate"] * shock.value_multiplier
                )
        return shocked
