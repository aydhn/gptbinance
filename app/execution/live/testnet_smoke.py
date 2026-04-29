import asyncio
import logging
from decimal import Decimal
import uuid
from app.execution.live.models import ExecutionConfig, ExecutionIntent
from app.execution.live.enums import ExecutionEnvironment
from app.execution.live.pretrade_validation import PretradeValidator
from app.execution.live.safety_gates import SafetyGateManager, MainnetDisarmedGate
from app.execution.live.client_order_ids import ClientOrderIdGenerator
from app.execution.live.binance_executor import BinanceTestnetExecutor
from app.execution.live.order_state_store import InMemoryOrderStateStore
from app.execution.live.order_router import OrderRouter
from app.core.models import OrderSide, OrderType

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def run_smoke_test(
    symbol: str, side: str, order_type: str, quantity: str, price: str = None
):
    logger.info("=== STARTING TESTNET SMOKE TEST ===")

    # Setup
    config = ExecutionConfig(
        environment=ExecutionEnvironment.TESTNET, mainnet_armed=False
    )
    gates = SafetyGateManager()
    gates.add_gate(MainnetDisarmedGate())

    rules = {
        symbol: {
            "minQty": Decimal("0.0001"),
            "tickSize": Decimal("0.01"),
            "stepSize": Decimal("0.0001"),
        }
    }
    validator = PretradeValidator(rules)

    id_gen = ClientOrderIdGenerator(session_id="SMOKE001")
    store = InMemoryOrderStateStore()

    class MockRestClient:
        async def post(self, *args, **kwargs):
            return {
                "clientOrderId": kwargs.get("data", {}).get("newClientOrderId", "mock"),
                "orderId": "123",
                "status": "NEW",
            }

    executor = BinanceTestnetExecutor(MockRestClient())
    router = OrderRouter(config, executor, store, validator, gates, id_gen)

    intent = ExecutionIntent(
        symbol=symbol,
        side=OrderSide[side.upper()],
        order_type=OrderType[order_type.upper()],
        quantity=Decimal(quantity),
        price=Decimal(price) if price else None,
        intent_id=uuid.uuid4().hex[:8],
    )

    logger.info(f"Submitting intent: {intent}")
    result = await router.submit_intent(intent)

    logger.info(f"Execution Result: {result}")

    state = store.get_state(result.client_order_id)
    logger.info(f"Final local state: {state}")

    logger.info("=== SMOKE TEST COMPLETE ===")


if __name__ == "__main__":
    asyncio.run(run_smoke_test("BTCUSDT", "BUY", "LIMIT", "0.001", "30000.0"))
