from app.compliance_plane.models import ExceptionAcceptanceRecord
from typing import Dict, List
from datetime import datetime, timezone


class ExceptionManager:
    def __init__(self):
        self._exceptions: Dict[str, ExceptionAcceptanceRecord] = {}

    def register_exception(self, exception: ExceptionAcceptanceRecord) -> None:
        self._exceptions[exception.exception_id] = exception

    def update_stale_states(self) -> None:
        now = datetime.now(timezone.utc)
        for exc in self._exceptions.values():
            if now > exc.expires_at:
                exc.is_stale = True

    def get_active_exceptions(self) -> List[ExceptionAcceptanceRecord]:
        return [e for e in self._exceptions.values() if not e.is_stale]

    def list_exceptions(self) -> List[ExceptionAcceptanceRecord]:
        return list(self._exceptions.values())
