from typing import Dict, Any
from .enums import SignalType, IncidentSeverity, IncidentScopeType
from .models import IncidentSignal

class SignalMapper:
    @staticmethod
    def create_signal(
        signal_id: str,
        signal_type: SignalType,
        domain: str,
        scope_type: IncidentScopeType,
        scope_ref: str,
        severity: IncidentSeverity,
        details: Dict[str, Any] = None
    ) -> IncidentSignal:
        return IncidentSignal(
            signal_id=signal_id,
            type=signal_type,
            source_domain=domain,
            scope_type=scope_type,
            scope_ref=scope_ref,
            severity_hint=severity,
            details=details or {}
        )
