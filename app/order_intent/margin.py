from typing import List
from app.order_intent.models import HighLevelIntent, CompiledOrderLeg, IntentContext
from app.order_intent.enums import OrderLegType, BorrowMode, OrderSide


class MarginCompiler:
    def compile(
        self, intent: HighLevelIntent, context: IntentContext
    ) -> List[CompiledOrderLeg]:
        legs = []

        # 1. Evaluate Borrow logic
        if intent.intent_type.value == "margin_borrow_backed_buy":
            # Inject a explicit borrow leg if needed
            if context.available_balance < intent.size:
                borrow_amount = intent.size - context.available_balance
                legs.append(
                    CompiledOrderLeg(
                        leg_id=f"leg_{intent.intent_id}_borrow",
                        leg_type=OrderLegType.MARGIN_BORROW,
                        symbol=intent.symbol,  # Needs mapping to base asset in reality
                        product=intent.product,
                        size=borrow_amount,
                    )
                )

        # 2. Add the trade leg
        trade_leg = CompiledOrderLeg(
            leg_id=f"leg_{intent.intent_id}_margin_trade",
            leg_type=OrderLegType.MARGIN_TRADE,
            symbol=intent.symbol,
            product=intent.product,
            side=intent.side,
            size=intent.size,
            borrow_mode=(
                BorrowMode.AUTO_BORROW if not legs else BorrowMode.EXPLICIT_BORROW
            ),
        )
        if legs:
            trade_leg.dependency_leg_ids.append(legs[0].leg_id)
        legs.append(trade_leg)

        # 3. Evaluate Repay logic
        if (
            intent.intent_type.value == "margin_repay_after_reduce"
            and intent.side == OrderSide.SELL
        ):
            # Add repay leg after sell
            repay_leg = CompiledOrderLeg(
                leg_id=f"leg_{intent.intent_id}_repay",
                leg_type=OrderLegType.MARGIN_REPAY,
                symbol=intent.symbol,
                product=intent.product,
                size=intent.size,  # Naive logic: repay what was sold
            )
            repay_leg.dependency_leg_ids.append(trade_leg.leg_id)
            legs.append(repay_leg)

        return legs
