from app.backtest.costs import CostCalculator
from app.backtest.models import CostModelConfig, SlippageModelConfig
from app.backtest.enums import CostModelType, SlippageModelType


def test_cost_calculation():
    c_cfg = CostModelConfig(model_type=CostModelType.FIXED_BPS, taker_fee_bps=4.0)
    s_cfg = SlippageModelConfig(model_type=SlippageModelType.ZERO_SLIPPAGE)
    calc = CostCalculator(c_cfg, s_cfg)

    # 1000 * 4 bps = 0.4
    fee = calc.calculate_cost(1000.0, is_maker=False)
    assert abs(fee - 0.4) < 1e-5


def test_slippage_calculation():
    c_cfg = CostModelConfig(model_type=CostModelType.ZERO_FEE)
    s_cfg = SlippageModelConfig(
        model_type=SlippageModelType.FIXED_BPS, slippage_bps=5.0
    )
    calc = CostCalculator(c_cfg, s_cfg)

    price = 100.0
    adjusted_buy = calc.apply_slippage_to_price(price, is_buy=True)
    assert adjusted_buy > price

    adjusted_sell = calc.apply_slippage_to_price(price, is_buy=False)
    assert adjusted_sell < price
