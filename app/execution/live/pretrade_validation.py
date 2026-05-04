from app.crossbook.enums import CrossBookVerdict
from app.events.models import EventRiskOverlay
from app.events.execution import validate_execution_against_events
from app.products.enums import ProductType
from app.execution.derivatives.pretrade_validation import DerivativePretradeValidator
from typing import Dict, Any
from decimal import Decimal
from app.execution.live.models import ExecutionIntent
from app.execution.live.exceptions import PretradeValidationError
from app.core.models import OrderType
import logging

logger = logging.getLogger(__name__)


class PretradeValidator:
    def __init__(self, exchange_rules: Dict[str, Any]):
        """
        exchange_rules expects a dictionary mapping symbols to their rules.
        Example: {
            "BTCUSDT": {
                "minQty": Decimal("0.00001"),
                "minNotional": Decimal("10.0"),
                "tickSize": Decimal("0.01"),
                "stepSize": Decimal("0.00001")
            }
        }
        """
        self.exchange_rules = exchange_rules

    def validate(self, intent: ExecutionIntent) -> None:
        if intent.symbol not in self.exchange_rules:
            raise PretradeValidationError(
                f"No exchange rules found for symbol {intent.symbol}"
            )

        rules = self.exchange_rules[intent.symbol]

        # Quantity check
        min_qty = rules.get("minQty")
        if min_qty and intent.quantity < min_qty:
            raise PretradeValidationError(
                f"Quantity {intent.quantity} below minQty {min_qty} for {intent.symbol}"
            )

        step_size = rules.get("stepSize")
        if step_size and (intent.quantity % step_size) != Decimal("0"):
            logger.warning(
                f"Quantity {intent.quantity} does not align perfectly with stepSize {step_size}. May fail on exchange."
            )
            # In a stricter implementation, we might round or reject. For now, warning.

        # Price check
        if intent.order_type == OrderType.LIMIT:
            if not intent.price:
                raise PretradeValidationError(f"Limit order requires a price.")

            tick_size = rules.get("tickSize")
            if tick_size and (intent.price % tick_size) != Decimal("0"):
                logger.warning(
                    f"Price {intent.price} does not align with tickSize {tick_size}."
                )

            min_notional = rules.get("minNotional")
            if min_notional and (intent.price * intent.quantity) < min_notional:
                raise PretradeValidationError(
                    f"Notional value below minNotional {min_notional} for {intent.symbol}"
                )

        logger.info(f"Pretrade validation passed for intent {intent.intent_id}")

    # Added in Phase 38
    def check_stress_overlay_verdict(self, verdict):
        pass

    # Added in Phase 40
    def check_crossbook_overlay_verdict(self, verdict):
        if verdict == CrossBookVerdict.BLOCK:
            raise PretradeValidationError("Blocked by cross-book exposure overlay.")
        elif verdict == CrossBookVerdict.REDUCE:
            logger.warning("Cross-book overlay suggests reducing exposure.")
