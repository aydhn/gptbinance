import pytest
from app.execution.live.binance_executor import BinanceTestnetExecutor
from app.execution.derivatives.models import DerivativeExecutionIntent
from app.execution.derivatives.enums import DerivativeSide
from app.products.enums import ProductType

@pytest.mark.asyncio
async def test_live_derivative_testnet():
    executor = BinanceTestnetExecutor()
    intent = DerivativeExecutionIntent(product_type=ProductType.FUTURES_USDM, symbol="BTCUSDT", side=DerivativeSide.LONG, quantity=1.0)

    res = await executor.execute_derivative(intent, testnet_first=True)
    assert res == "testnet_mock_order_id"

@pytest.mark.asyncio
async def test_live_derivative_mainnet_blocked():
    executor = BinanceTestnetExecutor()
    intent = DerivativeExecutionIntent(product_type=ProductType.FUTURES_USDM, symbol="BTCUSDT", side=DerivativeSide.LONG, quantity=1.0)

    with pytest.raises(NotImplementedError):
        await executor.execute_derivative(intent, testnet_first=False)
