import logging
from app.products.enums import ProductType, MarginMode
from app.products.registry import ProductRegistry
from app.execution.derivatives.models import LiquidationSnapshot
from app.execution.derivatives.enums import LiquidationProximity

logger = logging.getLogger(__name__)

class DerivativeRiskController:
    def __init__(self, registry: ProductRegistry):
        self.registry = registry

    def check_leverage_cap(self, product_type: ProductType, current_leverage: int) -> bool:
        desc = self.registry.get_descriptor(product_type)
        if current_leverage > desc.capabilities.max_leverage:
            logger.warning(f"Risk Breach: Leverage {current_leverage}x exceeds product cap {desc.capabilities.max_leverage}x")
            return False
        return True

    def check_liquidation_buffer(self, snapshot: LiquidationSnapshot) -> bool:
        if snapshot.proximity in (LiquidationProximity.WARNING, LiquidationProximity.DANGER):
            logger.warning(f"Risk Breach: Liquidation proximity is {snapshot.proximity.value} for {snapshot.symbol}")
            return False
        return True

    def requires_strict_reduce_only(self, margin_mode: MarginMode, snapshot: LiquidationSnapshot) -> bool:
        # Require reduce only if close to liquidation or in cross mode with tight margin
        if snapshot.proximity == LiquidationProximity.WARNING:
            return True
        return False
