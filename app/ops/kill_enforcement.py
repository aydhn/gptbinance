from app.ops.repository import OpsRepository


class KillEnforcement:
    def __init__(self, repository: OpsRepository):
        self.repository = repository
        self._hard_kill_active = False
        self._kill_reason = ""

    def enforce_kill(self, run_id: str, reason: str) -> None:
        self._hard_kill_active = True
        self._kill_reason = reason

    def is_kill_active(self) -> bool:
        return self._hard_kill_active

    def clear_kill(self, clearance_code: str) -> bool:
        if clearance_code == "MANUAL_OVERRIDE_CONFIRM":
            self._hard_kill_active = False
            self._kill_reason = ""
            return True
        return False
