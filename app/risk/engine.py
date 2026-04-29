"""Risk engine interface for runtime evaluation."""
import logging
from typing import Optional, Dict, Any
from app.execution.paper.models import PaperOrderIntent

logger = logging.getLogger(__name__)


class RiskEngine:
    def __init__(self, config: Any):
        self.config = config

    def evaluate_intent(
        self, intent: PaperOrderIntent, current_positions: list, current_equity: float
    ) -> bool:
        """
        Fast path evaluation for runtime.
        Return True if approved, False if vetoed.
        """
        # Very basic stub: approve everything for now, except if notional is too big
        if intent.price and intent.qty:
            notional = intent.price * intent.qty
            if notional > current_equity * 0.5:  # Don't bet more than 50% on one trade
                logger.warning(
                    f"Risk vetoed intent {intent.intent_id}: Notional {notional} exceeds 50% equity."
                )
                return False

        return True
