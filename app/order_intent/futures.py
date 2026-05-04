from app.order_intent.enums import OrderLegType
from app.order_intent.models import HighLevelIntent, CompiledOrderLeg, IntentContext
from app.order_intent.semantics import SemanticsResolver


class FuturesCompiler:
    def compile(
        self, intent: HighLevelIntent, context: IntentContext
    ) -> CompiledOrderLeg:
        pos_mode = context.account_snapshot.futures_position_mode
        resolved_pos_side = SemanticsResolver.resolve_position_side(
            intent.product, pos_mode, intent.side, intent.position_side
        )

        return CompiledOrderLeg(
            leg_id=f"leg_{intent.intent_id}_fut",
            leg_type=OrderLegType.FUTURES_TRADE,
            symbol=intent.symbol,
            product=intent.product,
            side=intent.side,
            size=intent.size,
            position_side=resolved_pos_side,
        )
