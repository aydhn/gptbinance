from typing import Dict, List, Optional
from app.observability.models import RunbookRef


class RunbookRegistry:
    def __init__(self):
        self._runbooks: Dict[str, RunbookRef] = {}
        self._seed_runbooks()

    def _seed_runbooks(self):
        self.register(
            RunbookRef(
                ref_id="RB-STREAM-001",
                title="Stream Stale Investigation",
                description="Steps to investigate when market data streams become stale.",
                investigation_steps=[
                    "Check Binance API status page.",
                    "Verify network connectivity to Binance WS endpoints.",
                    "Check supervisor logs for disconnects.",
                ],
                mitigation_steps=[
                    "Restart the data stream component via supervisor.",
                    "Failover to backup node if available.",
                ],
            )
        )
        self.register(
            RunbookRef(
                ref_id="RB-EXEC-001",
                title="Execution Reject Storm",
                description="Steps to handle a spike in order rejections.",
                investigation_steps=[
                    "Check exchange API limits and error codes in execution logs.",
                    "Verify available balance and margin requirements.",
                    "Review recent strategy signals for anomalies.",
                ],
                mitigation_steps=[
                    "Halt new order generation temporarily.",
                    "Clear stuck orders in the reconciliation layer.",
                ],
            )
        )

    def register(self, runbook: RunbookRef) -> None:
        self._runbooks[runbook.ref_id] = runbook

    def get_runbook(self, ref_id: str) -> Optional[RunbookRef]:
        return self._runbooks.get(ref_id)

    def list_runbooks(self) -> List[RunbookRef]:
        return list(self._runbooks.values())


registry = RunbookRegistry()
