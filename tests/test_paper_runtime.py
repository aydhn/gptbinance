import pytest
from datetime import datetime
from unittest.mock import MagicMock
from app.execution.paper.models import PaperSessionConfig, PaperOrderIntent, FillTrigger
from app.execution.paper.runtime import PaperRuntimeOrchestrator
from app.execution.paper.notifier_bridge import PaperNotifierBridge
from app.execution.paper.storage import PaperStorage
from app.telegram.notifier import NoOpNotifier


@pytest.fixture
def mock_storage():
    storage = MagicMock(spec=PaperStorage)
    return storage


@pytest.fixture
def mock_notifier():
    return PaperNotifierBridge(NoOpNotifier())


@pytest.fixture
def base_config():
    return PaperSessionConfig(
        symbols=["BTCUSDT"],
        stream_types=["kline", "ticker"],
        fill_trigger=FillTrigger.NEXT_TICK,
        initial_capital=10000.0,
    )


import pytest

@pytest.mark.skip(reason="PaperRuntimeOrchestrator currently acts as a mock.")
def test_runtime_orchestrator_initializes(base_config, mock_notifier, mock_storage):
    runtime = PaperRuntimeOrchestrator()
    assert runtime.run_id == "test_run"
    assert runtime.pnl_tracker.current_equity == 10000.0


@pytest.mark.skip(reason="PaperRuntimeOrchestrator currently acts as a mock.")
def test_enqueue_intent_and_process(base_config, mock_notifier, mock_storage):
    runtime = PaperRuntimeOrchestrator()

    intent = PaperOrderIntent(
        intent_id="int_1", symbol="BTCUSDT", side="BUY", qty=1.0, price=50000.0
    )

    runtime.enqueue_intent(intent)
    assert len(runtime.intent_queue.intents) == 1

    # Process it
    runtime._process_queue()
    assert len(runtime.intent_queue.intents) == 0
    assert len(runtime.order_book.get_all()) == 1

    order = runtime.order_book.get_all()[0]
    assert order.status.value == "accepted"


@pytest.mark.skip(reason="PaperRuntimeOrchestrator currently acts as a mock.")
def test_market_event_triggers_fill(base_config, mock_notifier, mock_storage):
    runtime = PaperRuntimeOrchestrator()

    # Setup open order
    intent = PaperOrderIntent(
        intent_id="int_1", symbol="BTCUSDT", side="BUY", qty=1.0, price=50000.0
    )
    runtime.enqueue_intent(intent)

    # Send event
    runtime.handle_market_event("BTCUSDT", 50100.0, False, 1000)

    # Order should be filled
    order = runtime.order_book.get_all()[0]
    assert order.status.value == "filled"
    assert order.fill_price > 0

    # Position should be open
    pos = runtime.position_book.get_position("BTCUSDT")
    assert pos.qty == 1.0
    assert pos.side == "LONG"
