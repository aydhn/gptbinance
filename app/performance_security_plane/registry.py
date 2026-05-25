from typing import Dict, Any, List
from app.performance_security_plane.base import SecurityRegistryBase
from app.performance_security_plane.exceptions import InvalidSecurityObjectError

class PerformanceSecurityRegistry(SecurityRegistryBase):
    def __init__(self):
        self._registry: Dict[str, Any] = {}

    def register_security(self, security_object: Any) -> str:
        if not hasattr(security_object, "security_id") or not security_object.security_id:
            raise InvalidSecurityObjectError("security_id is required")
        if security_object.security_id in self._registry:
            raise InvalidSecurityObjectError(f"Security ID {security_object.security_id} already registered")

        self._registry[security_object.security_id] = security_object
        return security_object.security_id

    def get_security(self, security_id: str) -> Any:
        if security_id not in self._registry:
            raise InvalidSecurityObjectError(f"Security ID {security_id} not found")
        return self._registry[security_id]

    def list_securities(self) -> List[Any]:
        return list(self._registry.values())
