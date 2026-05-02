from app.products.enums import ProductType
from .models import DerivativeExecutionIntent
import logging

logger = logging.getLogger(__name__)


class DerivativeRouter:
    def route(self, intent: DerivativeExecutionIntent, paper_mode: bool = False):
        if intent.product_type == ProductType.SPOT:
            # Should not be routed here, but safety check
            logger.warning("Spot order routed to derivatives router.")
            return

        if paper_mode:
            logger.info(
                f"Routing {intent.product_type} {intent.symbol} to PAPER execution."
            )
            # Dispatch to paper derivatives runtime
        else:
            logger.info(
                f"Routing {intent.product_type} {intent.symbol} to TESTNET/LIVE execution."
            )
            # Dispatch to live binance derivatives executor
