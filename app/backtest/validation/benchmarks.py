from typing import Dict, Any, Type
from app.backtest.validation.enums import BenchmarkType
from app.backtest.validation.models import BaselineStrategyDescriptor
from app.strategies.base import BaseStrategy
from app.backtest.models import BacktestStepContext

# We will define simple baseline strategies here that inherit from BaseStrategy
# so they can be run by the regular backtest engine.


class FlatBaselineStrategy(BaseStrategy):
    @property
    def name(self) -> str:
        return "FlatBaselineStrategy"

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def evaluate(self, ctx: BacktestStepContext) -> None:
        pass

    """Never trades. Risk-free, cost-free baseline."""

    def on_kline(self, kline: Dict[str, Any]) -> None:
        pass


class BuyAndHoldBaselineStrategy(BaseStrategy):
    @property
    def name(self) -> str:
        return "BuyAndHoldBaselineStrategy"

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def evaluate(self, ctx: BacktestStepContext) -> None:
        pass

    """Buys on the first kline and holds until the end."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.has_bought = False

    def on_kline(self, kline: Dict[str, Any]) -> None:
        if not self.has_bought:
            price = kline.get("close", 0)
            if price > 0:
                self.broker.execute_market_order(
                    self.symbol, "BUY", 1.0
                )  # Buy 1 unit (simplified)
                self.has_bought = True


class NaiveTrendFollowBaselineStrategy(BaseStrategy):
    @property
    def name(self) -> str:
        return "NaiveTrendFollowBaselineStrategy"

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def evaluate(self, ctx: BacktestStepContext) -> None:
        pass

    """Buys if close > SMA(20), sells if close < SMA(20). Simplified."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history = []
        self.period = 20

    def on_kline(self, kline: Dict[str, Any]) -> None:
        price = kline.get("close", 0)
        if price <= 0:
            return

        self.history.append(price)
        if len(self.history) > self.period:
            self.history.pop(0)

        if len(self.history) == self.period:
            sma = sum(self.history) / self.period
            position = self.broker.get_position(self.symbol)

            if price > sma and position == 0:
                self.broker.execute_market_order(self.symbol, "BUY", 1.0)
            elif price < sma and position > 0:
                self.broker.execute_market_order(self.symbol, "SELL", position)


class NaiveMeanReversionBaselineStrategy(BaseStrategy):
    @property
    def name(self) -> str:
        return "NaiveMeanReversionBaselineStrategy"

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def evaluate(self, ctx: BacktestStepContext) -> None:
        pass

    """Buys if close < SMA(20) - threshold, sells if close > SMA(20) + threshold."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history = []
        self.period = 20
        self.threshold_pct = 0.02  # 2% deviation

    def on_kline(self, kline: Dict[str, Any]) -> None:
        price = kline.get("close", 0)
        if price <= 0:
            return

        self.history.append(price)
        if len(self.history) > self.period:
            self.history.pop(0)

        if len(self.history) == self.period:
            sma = sum(self.history) / self.period
            position = self.broker.get_position(self.symbol)

            lower_bound = sma * (1 - self.threshold_pct)
            upper_bound = sma * (1 + self.threshold_pct)

            if price < lower_bound and position == 0:
                self.broker.execute_market_order(self.symbol, "BUY", 1.0)
            elif price > upper_bound and position > 0:
                self.broker.execute_market_order(self.symbol, "SELL", position)


class SimpleBreakoutBaselineStrategy(BaseStrategy):
    @property
    def name(self) -> str:
        return "SimpleBreakoutBaselineStrategy"

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def restore_state(self, state):
        pass

    def get_state_snapshot(self):
        return {}

    def is_ready(self):
        return True

    def evaluate(self, ctx) -> None:
        pass

    def evaluate(self, ctx: BacktestStepContext) -> None:
        pass

    """Buys if price breaks 20-period high."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.history = []
        self.period = 20

    def on_kline(self, kline: Dict[str, Any]) -> None:
        price = kline.get("close", 0)
        if price <= 0:
            return

        self.history.append(price)
        if len(self.history) > self.period:
            self.history.pop(0)

        if len(self.history) == self.period:
            highest_high = max(self.history[:-1])  # exclude current
            position = self.broker.get_position(self.symbol)

            if price > highest_high and position == 0:
                self.broker.execute_market_order(self.symbol, "BUY", 1.0)
            # Simplistic exit: trailing stop or hold
            elif position > 0 and price < sum(self.history) / self.period:  # SMA exit
                self.broker.execute_market_order(self.symbol, "SELL", position)


BENCHMARK_STRATEGY_MAP: Dict[BenchmarkType, Type[BaseStrategy]] = {
    BenchmarkType.FLAT: FlatBaselineStrategy,
    BenchmarkType.BUY_AND_HOLD: BuyAndHoldBaselineStrategy,
    BenchmarkType.NAIVE_TREND_FOLLOW: NaiveTrendFollowBaselineStrategy,
    BenchmarkType.NAIVE_MEAN_REVERSION: NaiveMeanReversionBaselineStrategy,
    BenchmarkType.SIMPLE_BREAKOUT: SimpleBreakoutBaselineStrategy,
}

BENCHMARK_DESCRIPTORS: Dict[BenchmarkType, BaselineStrategyDescriptor] = {
    BenchmarkType.FLAT: BaselineStrategyDescriptor(
        name="Flat Baseline",
        benchmark_type=BenchmarkType.FLAT,
        description="Never trades. Provides a 0-risk, 0-cost baseline.",
    ),
    BenchmarkType.BUY_AND_HOLD: BaselineStrategyDescriptor(
        name="Buy and Hold",
        benchmark_type=BenchmarkType.BUY_AND_HOLD,
        description="Buys on the first candle and holds until the end.",
    ),
    BenchmarkType.NAIVE_TREND_FOLLOW: BaselineStrategyDescriptor(
        name="Naive Trend Follow",
        benchmark_type=BenchmarkType.NAIVE_TREND_FOLLOW,
        description="Buys when price is above SMA20, sells when below.",
    ),
    BenchmarkType.NAIVE_MEAN_REVERSION: BaselineStrategyDescriptor(
        name="Naive Mean Reversion",
        benchmark_type=BenchmarkType.NAIVE_MEAN_REVERSION,
        description="Buys on -2% deviation from SMA20, sells on +2% deviation.",
    ),
    BenchmarkType.SIMPLE_BREAKOUT: BaselineStrategyDescriptor(
        name="Simple Breakout",
        benchmark_type=BenchmarkType.SIMPLE_BREAKOUT,
        description="Buys on breaking 20-period high, exits on SMA20 cross down.",
    ),
}
