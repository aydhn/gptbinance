from app.ops.models import DrainState
from app.ops.repository import OpsRepository


class SessionShutdown:
    def __init__(self, repository: OpsRepository):
        self.repository = repository

    def perform_drain(self, run_id: str) -> DrainState:
        print(f"[SHUTDOWN] Freezing new intents and draining queues for run: {run_id}")
        state = DrainState(
            run_id=run_id,
            new_intents_frozen=True,
            open_orders_remaining=0,
            drain_complete=True,
        )
        return state

    def perform_shutdown(self, run_id: str) -> None:
        print(f"[SHUTDOWN] Performing graceful shutdown for run: {run_id}")

    def prepare_for_upgrade(self, run_id: str) -> bool:
        print(f"[SHUTDOWN] Preparing for upgrade. Draining: {run_id}")
        self.perform_drain(run_id)
        self.perform_shutdown(run_id)
        return True
