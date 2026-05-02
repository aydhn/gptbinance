import logging
from app.execution.derivatives.models import DerivativeExecutionIntent
from app.execution.derivatives.pretrade_validation import DerivativePretradeValidator
from app.execution.derivatives.leverage import LeverageManager
from app.execution.derivatives.liquidation import LiquidationApproxModel

logger = logging.getLogger(__name__)


class PaperDerivativesRuntime:
    def __init__(
        self, validator: DerivativePretradeValidator, lev_mgr: LeverageManager
    ):
        self.validator = validator
        self.lev_mgr = lev_mgr
        self.liq_model = LiquidationApproxModel()

    def process_intent(
        self,
        intent: DerivativeExecutionIntent,
        current_qty: float,
        current_price: float,
        margin_balance: float,
    ):
        logger.info(
            f"[PAPER] Processing {intent.product_type} {intent.side} for {intent.symbol}"
        )

        if not self.validator.validate_intent(intent, current_qty):
            logger.error("[PAPER] Pretrade validation failed. Order dropped.")
            return False

        # Simulate Liquidation Check
        curr_lev = self.lev_mgr.get_leverage(intent.product_type, intent.symbol)
        liq_snap = self.liq_model.calculate_liquidation_snapshot(
            intent.symbol,
            current_price,
            current_price,
            current_qty
            + (intent.quantity if intent.side.value == "LONG" else -intent.quantity),
            margin_balance,
            intent.side.value == "LONG",
        )

        logger.info(
            f"[PAPER] Proximity: {liq_snap.proximity.value}. Distance: {liq_snap.distance_pct:.2%}"
        )
        logger.info(
            f"[PAPER] Accepted {intent.quantity} @ {current_price} (Leverage: {curr_lev}x)"
        )

        return True
