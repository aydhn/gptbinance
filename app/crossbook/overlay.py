from app.policy_kernel.enums import PolicyDomain, PolicyVerdict
from typing import Dict, Any


class CrossbookOverlay:
    def provide_remediation_suggestions(self):
        pass  # Placeholder

    def get_policy_domain_outputs(self, mock_verdict_str: str) -> Dict[str, Any]:
        """Expose Crossbook Overlay outputs for Policy Kernel Domain format"""
        verdict = PolicyVerdict.ALLOW
        if mock_verdict_str == "BLOCK":
            verdict = PolicyVerdict.BLOCK
        elif mock_verdict_str == "CAUTION":
            verdict = PolicyVerdict.CAUTION

        return {
            "domain": PolicyDomain.CROSS_BOOK,
            "reasons": ["Crossbook overlay assessment"],
            "verdict": verdict,
        }

import uuid
from typing import Dict, Any
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType
from app.incidents.signals import SignalMapper
from app.incidents.intake import IncidentCommand

def emit_crossbook_conflict_signal(symbol: str, details: Dict[str, Any] = None):
    cmd = IncidentCommand()
    signal = SignalMapper.create_signal(
        signal_id=f"cb-{uuid.uuid4().hex[:8]}",
        signal_type=SignalType.CROSS_BOOK_CONFLICT,
        domain="crossbook",
        scope_type=IncidentScopeType.SYMBOL,
        scope_ref=symbol,
        severity=IncidentSeverity.CRITICAL_INCIDENT,
        details=details or {"reason": "Fake hedge detected"}
    )
    cmd.ingest_signal(signal)
