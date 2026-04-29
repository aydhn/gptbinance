from app.execution.live.execution_parser import ExecutionParser
from app.execution.live.enums import OrderLifecycleStatus
from decimal import Decimal


def test_parse_execution_report():
    payload = {
        "e": "executionReport",
        "E": 1612345678901,
        "s": "BTCUSDT",
        "c": "web_xyz",
        "S": "BUY",
        "o": "LIMIT",
        "f": "GTC",
        "q": "1.00000000",
        "p": "30000.00000000",
        "X": "PARTIALLY_FILLED",
        "i": 4293153,
        "z": "0.50000000",
        "l": "0.50000000",
        "L": "30000.00000000",
    }

    event = ExecutionParser.parse_execution_report(payload)
    assert event.client_order_id == "web_xyz"
    assert event.status == OrderLifecycleStatus.PARTIALLY_FILLED
    assert event.details["filled_qty"] == Decimal("0.5")
