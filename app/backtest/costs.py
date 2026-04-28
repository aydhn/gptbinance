from app.backtest.models import CostModelConfig, SlippageModelConfig
from app.backtest.enums import CostModelType, SlippageModelType


class CostCalculator:
    def __init__(
        self, cost_config: CostModelConfig, slippage_config: SlippageModelConfig
    ):
        self.cost_config = cost_config
        self.slippage_config = slippage_config

    def calculate_cost(self, notional_value: float, is_maker: bool = False) -> float:
        if self.cost_config.model_type == CostModelType.ZERO_FEE:
            return 0.0

        fee_bps = (
            self.cost_config.maker_fee_bps
            if is_maker
            else self.cost_config.taker_fee_bps
        )
        return notional_value * (fee_bps / 10000.0)

    def calculate_slippage(self, notional_value: float) -> float:
        if self.slippage_config.model_type == SlippageModelType.ZERO_SLIPPAGE:
            return 0.0

        return notional_value * (self.slippage_config.slippage_bps / 10000.0)

    def apply_slippage_to_price(self, price: float, is_buy: bool) -> float:
        """
        Adjust price worse by slippage amount.
        Buy -> price goes up
        Sell -> price goes down
        """
        if self.slippage_config.model_type == SlippageModelType.ZERO_SLIPPAGE:
            return price

        slippage_ratio = self.slippage_config.slippage_bps / 10000.0
        if is_buy:
            return price * (1.0 + slippage_ratio)
        else:
            return price * (1.0 - slippage_ratio)
