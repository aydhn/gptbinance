import pytest
from unittest.mock import MagicMock
from app.execution.live_runtime.runtime import LiveOrchestrator
from app.execution.live_runtime.models import (
    LiveSessionConfig,
    LiveCapitalCaps,
    LiveSymbolAllowance,
    LiveFillRecord,
)
from app.execution.live_runtime.enums import LiveRolloutMode, LiveSessionStatus


import pytest
@pytest.mark.asyncio
async def test_live_runtime_orchestrator():
    config = LiveSessionConfig(
        rollout_mode=LiveRolloutMode.CANARY_LIVE,
        capital_caps=LiveCapitalCaps(
            max_session_notional_usd=1000.0,
            max_daily_loss_usd=100.0,
            max_live_exposure_usd=500.0,
            max_new_orders_per_session=10,
            allowlist=[
                LiveSymbolAllowance(
                    symbol="BTCUSDT", max_notional_usd=100.0, max_orders=5
                )
            ],
        ),
        require_telegram_notify=False,
    )

    mock_gateway = MagicMock()
    mock_sync = MagicMock()
    mock_notifier = MagicMock()

    orchestrator = LiveOrchestrator(
        config=config,
        run_id="test_run",
        execution_gateway=mock_gateway,
        account_sync=mock_sync,
        notifier=mock_notifier,
    )

    context = {
        "mainnet_armed": True,
        "ops_readiness_pass": True,
        "reconciliation_clean": True,
    }

    started = orchestrator.start_session(context)
    assert started
    assert orchestrator.run.state.status == LiveSessionStatus.RUNNING

    # Process intent
    intent = {"symbol": "BTCUSDT", "qty": 0.001, "price": 50000.0, "side": "BUY"}
    res = await orchestrator.process_intent(intent)
    assert res
    mock_gateway.submit_order.assert_called_once()

    # Handle fill
    fill = LiveFillRecord(
        fill_id="f1",
        order_id="o1",
        client_order_id="c1",
        symbol="BTCUSDT",
        side="BUY",
        qty=0.001,
        price=50000.0,
        fee=1.0,
        fee_asset="USDT",
    )
    orchestrator.handle_fill(fill)

    book = orchestrator.position_manager.get_book()
    assert "BTCUSDT" in book.positions
    assert book.positions["BTCUSDT"].qty == 0.001

    orchestrator.stop_session()
    assert orchestrator.run.state.status == LiveSessionStatus.COMPLETED
