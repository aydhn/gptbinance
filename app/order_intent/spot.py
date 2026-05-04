from app.order_intent.models import HighLevelIntent, CompiledOrderLeg, IntentContext
from app.order_intent.enums import OrderLegType


class SpotCompiler:
    def compile(
        self, intent: HighLevelIntent, context: IntentContext
    ) -> CompiledOrderLeg:
        # Basic spot execution mapping
        return CompiledOrderLeg(
            leg_id=f"leg_{intent.intent_id}_spot",
            leg_type=OrderLegType.SPOT_TRADE,
            symbol=intent.symbol,
            product=intent.product,
            side=intent.side,
            size=intent.size,
        )
