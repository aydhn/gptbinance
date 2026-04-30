from app.products.registry import ProductRegistry
from app.products.enums import ProductType
from .models import DerivativeExecutionIntent
from .leverage import LeverageManager
from .reduce_only import ReduceOnlyValidator, ReduceOnlyExecutionRequest
from .enums import ReduceOnlyVerdict
import logging

logger = logging.getLogger(__name__)

class DerivativePretradeValidator:
    def __init__(self, registry: ProductRegistry, lev_mgr: LeverageManager):
        self.registry = registry
        self.lev_mgr = lev_mgr

    def validate_intent(self, intent: DerivativeExecutionIntent, current_position_qty: float) -> bool:
        desc = self.registry.get_descriptor(intent.product_type)

        if intent.is_reduce_only:
            req = ReduceOnlyExecutionRequest(intent=intent, current_position_qty=current_position_qty)
            verdict, adj_qty, reason = ReduceOnlyValidator.validate(req)
            if verdict == ReduceOnlyVerdict.REJECTED:
                logger.error(f"Pretrade validation failed: {reason}")
                return False
            elif verdict == ReduceOnlyVerdict.ADJUSTED:
                logger.warning(f"Pretrade validation warning: {reason}")
                intent.quantity = adj_qty # Side effect adjusting intent

        # Leverage checks
        curr_lev = self.lev_mgr.get_leverage(intent.product_type, intent.symbol)
        if curr_lev > desc.capabilities.max_leverage:
            logger.error(f"Pretrade validation failed: Current leverage {curr_lev} exceeds cap {desc.capabilities.max_leverage}")
            return False

        return True
