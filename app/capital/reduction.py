from typing import Dict, Any
import uuid
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType
from app.incidents.signals import SignalMapper
from app.incidents.intake import IncidentCommand

class CapitalReduction:
    def advisory_to_remediation_pack(self):
        pass

    def emit_capital_freeze(self, workspace_id: str, details: Dict[str, Any] = None):
        cmd = IncidentCommand()
        signal = SignalMapper.create_signal(
            signal_id=f"cap-{uuid.uuid4().hex[:8]}",
            signal_type=SignalType.CAPITAL_FREEZE_ESCALATED,
            domain="capital_governance",
            scope_type=IncidentScopeType.WORKSPACE,
            scope_ref=workspace_id,
            severity=IncidentSeverity.MAJOR_INCIDENT,
            details=details
        )
        cmd.ingest_signal(signal)
