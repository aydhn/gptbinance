from typing import Dict, Any, List
from app.performance_security_plane.registry import PerformanceSecurityRegistry

class PerformanceSecurityRepository:
    def __init__(self, registry: PerformanceSecurityRegistry):
        self.registry = registry
        self.securities: Dict[str, Any] = {}
        self.draws: Dict[str, Any] = {}
        self.releases: Dict[str, Any] = {}

    def save_security_record(self, record: Any):
        self.securities[record.security_id] = record

    def get_security_record(self, security_id: str) -> Any:
        return self.securities.get(security_id)
