from typing import Dict, List, Optional
from app.security_plane.models import SecurityExceptionRecord
from datetime import datetime, timezone

class ExceptionManager:
    def __init__(self):
        self._exceptions: Dict[str, SecurityExceptionRecord] = {}

    def grant_exception(self, record: SecurityExceptionRecord) -> None:
        self._exceptions[record.exception_id] = record

    def get_active_exceptions(self, scope: str = None) -> List[SecurityExceptionRecord]:
        now = datetime.now(timezone.utc)
        active = [e for e in self._exceptions.values() if e.ttl_expires_at > now]
        if scope:
            active = [e for e in active if e.scope == scope]
        return active
