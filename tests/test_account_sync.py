import pytest
from app.execution.live_runtime.account_sync import AccountSynchronizer
from unittest.mock import MagicMock


def test_account_synchronizer():
    # Mocking client logic
    client = MagicMock()
    sync = AccountSynchronizer(client)

    sync.hydrate("test_run_id")
    assert sync.current_snapshot is not None
    assert sync.current_snapshot.run_id == "test_run_id"

    usdt_free = sync.get_free_balance("USDT")
    assert usdt_free > 0.0
