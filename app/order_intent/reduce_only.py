from app.order_intent.enums import VenueProduct, OrderSide
from app.order_intent.models import CompiledOrderLeg, IntentContext
from app.order_intent.exceptions import ReduceOnlyViolation


class ReduceOnlyCompiler:
    def apply(self, leg: CompiledOrderLeg, context: IntentContext) -> CompiledOrderLeg:
        if leg.product not in [VenueProduct.FUTURES_USDM, VenueProduct.FUTURES_COINM]:
            return leg  # Spot/Margin don't use this flag directly in the same way

        # If it's explicitly marked as reduce_only or the intent is to reduce
        if leg.reduce_only:
            # Basic sanity check: to reduce, you must trade opposite to your position
            if context.existing_exposure > 0 and leg.side != OrderSide.SELL:
                raise ReduceOnlyViolation(
                    "Cannot apply reduce-only BUY to a long position"
                )
            if context.existing_exposure < 0 and leg.side != OrderSide.BUY:
                raise ReduceOnlyViolation(
                    "Cannot apply reduce-only SELL to a short position"
                )

            leg.reduce_only = True

        return leg
