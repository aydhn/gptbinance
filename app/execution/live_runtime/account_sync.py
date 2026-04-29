from app.execution.live_runtime.base import AccountSyncBase
from app.execution.live_runtime.models import LiveAccountSnapshot, LiveBalanceSnapshot
from app.execution.live_runtime.exceptions import AccountSyncError
from typing import Any, Dict
import logging

logger = logging.getLogger(__name__)


class AccountSynchronizer(AccountSyncBase):
    def __init__(self, binance_client: Any):
        self.binance_client = binance_client
        self.current_snapshot: LiveAccountSnapshot | None = None
        self.run_id: str | None = None

    def fetch_snapshot(self, run_id: str) -> LiveAccountSnapshot:
        try:
            # In a real impl, this would await self.binance_client.get_account()
            # For this phase, we mock a safe default
            raw_balances = [{"asset": "USDT", "free": "1000.0", "locked": "0.0"}]
            balances = [
                LiveBalanceSnapshot(
                    asset=b["asset"], free=float(b["free"]), locked=float(b["locked"])
                )
                for b in raw_balances
            ]
            snapshot = LiveAccountSnapshot(run_id=run_id, balances=balances)
            self.current_snapshot = snapshot
            return snapshot
        except Exception as e:
            logger.error(f"Failed to fetch live account snapshot: {e}")
            raise AccountSyncError(f"Failed to sync account: {e}")

    def hydrate(self, run_id: str) -> None:
        self.run_id = run_id
        self.fetch_snapshot(run_id)
        logger.info(f"Account state hydrated for run {run_id}")

    def get_free_balance(self, asset: str) -> float:
        if not self.current_snapshot:
            return 0.0
        for b in self.current_snapshot.balances:
            if b.asset == asset:
                return b.free
        return 0.0
