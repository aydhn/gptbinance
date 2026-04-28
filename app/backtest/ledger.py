from typing import List, Optional
import uuid
from app.backtest.models import SimulatedFill, TradeRecord
from app.backtest.enums import PositionSide, TradeStatus, OrderSide


class Ledger:
    def __init__(self):
        self.fills: List[SimulatedFill] = []
        self.trades: List[TradeRecord] = []
        self._current_trade: Optional[TradeRecord] = None

    def record_fill(
        self,
        fill: SimulatedFill,
        position_side_before: PositionSide,
        position_side_after: PositionSide,
    ):
        self.fills.append(fill)
        decision = fill.decision

        # Trade mapping logic
        if (
            position_side_before == PositionSide.FLAT
            and position_side_after != PositionSide.FLAT
        ):
            # Open new trade
            self._current_trade = TradeRecord(
                trade_id=str(uuid.uuid4()),
                symbol=fill.intent.symbol,
                side=position_side_after,
                entry_timestamp=decision.fill_timestamp,
                entry_price=decision.fill_price,
                quantity=decision.fill_quantity,
                strategy_source=fill.intent.intent_source,
                total_fees=decision.fee_paid,
                total_slippage=decision.slippage_applied,
            )
            self.trades.append(self._current_trade)

        elif self._current_trade and self._current_trade.status == TradeStatus.OPEN:
            # We have an open trade
            is_reduce_or_close = False

            if (
                self._current_trade.side == PositionSide.LONG
                and fill.intent.side == OrderSide.SELL
            ):
                is_reduce_or_close = True
            elif (
                self._current_trade.side == PositionSide.SHORT
                and fill.intent.side == OrderSide.BUY
            ):
                is_reduce_or_close = True

            if is_reduce_or_close:
                # Accumulate PnL and fees
                self._current_trade.realized_pnl += fill.realized_pnl
                self._current_trade.total_fees += decision.fee_paid
                self._current_trade.total_slippage += decision.slippage_applied
                self._current_trade.exit_price = (
                    decision.fill_price
                )  # Store last exit price
                self._current_trade.exit_timestamp = decision.fill_timestamp

                if position_side_after == PositionSide.FLAT:
                    self._current_trade.status = TradeStatus.CLOSED
                    self._current_trade = None
                elif position_side_after != position_side_before:
                    # Reverse occurred. Close current, open new.
                    self._current_trade.status = TradeStatus.CLOSED

                    # Assume remaining qty is the new open qty
                    remaining_qty = (
                        fill.decision.fill_quantity - self._current_trade.quantity
                    )
                    self._current_trade = TradeRecord(
                        trade_id=str(uuid.uuid4()),
                        symbol=fill.intent.symbol,
                        side=position_side_after,
                        entry_timestamp=decision.fill_timestamp,
                        entry_price=decision.fill_price,
                        quantity=abs(remaining_qty),
                        strategy_source=fill.intent.intent_source,
                        total_fees=0.0,  # Approximate, already counted mostly in close
                        total_slippage=0.0,
                    )
                    self.trades.append(self._current_trade)
            else:
                # Adding to position
                self._current_trade.total_fees += decision.fee_paid
                self._current_trade.total_slippage += decision.slippage_applied
                # Update average entry price roughly
                total_val = (
                    self._current_trade.quantity * self._current_trade.entry_price
                ) + (decision.fill_quantity * decision.fill_price)
                self._current_trade.quantity += decision.fill_quantity
                self._current_trade.entry_price = (
                    total_val / self._current_trade.quantity
                )

    def get_completed_trades(self) -> List[TradeRecord]:
        return [t for t in self.trades if t.status == TradeStatus.CLOSED]
