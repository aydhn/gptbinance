from app.order_intent.enums import VenueProduct
from app.order_intent.models import CompiledOrderLeg, IntentContext


class ClosePositionCompiler:
    def apply(self, leg: CompiledOrderLeg, context: IntentContext) -> CompiledOrderLeg:
        if leg.product not in [VenueProduct.FUTURES_USDM, VenueProduct.FUTURES_COINM]:
            return leg

        if leg.close_position:
            # closePosition usually means size is ignored or sent as 0 depending on the API,
            # but conceptually we mark it.
            leg.close_position = True
            leg.size = 0.0  # Standard Binance behavior often relies on 0 or omission for closeAll
            # Must also ensure reduce_only is false if close_position is true, or handled by API correctly.
            # In Binance, closePosition is a separate param.

        return leg
