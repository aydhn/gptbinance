from app.remediation.models import RemediationFindingRef, RemediationDebtRecord
from app.remediation.enums import DebtSeverity


class DebtGovernance:
    def assess_debt(
        self, unresolved_findings: list[RemediationFindingRef]
    ) -> list[RemediationDebtRecord]:
        debts = []
        for finding in unresolved_findings:
            sev = DebtSeverity.WARNING
            if finding.severity == "critical":
                sev = DebtSeverity.BLOCKER

            debts.append(
                RemediationDebtRecord(
                    debt_id=f"DEBT-{finding.finding_id}",
                    finding_ref=finding,
                    severity=sev,
                    failed_attempts=1,
                    aging_days=2,
                    is_qualification_blocker=(sev == DebtSeverity.BLOCKER),
                )
            )
        return debts

import uuid
from typing import Dict, Any
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType
from app.incidents.signals import SignalMapper
from app.incidents.intake import IncidentCommand

def emit_remediation_failed_signal(profile_id: str, details: Dict[str, Any] = None):
    cmd = IncidentCommand()
    signal = SignalMapper.create_signal(
        signal_id=f"rem-{uuid.uuid4().hex[:8]}",
        signal_type=SignalType.REMEDIATION_FAILED,
        domain="remediation",
        scope_type=IncidentScopeType.PROFILE,
        scope_ref=profile_id,
        severity=IncidentSeverity.MAJOR_INCIDENT,
        details=details or {"reason": "Remediation failed"}
    )
    cmd.ingest_signal(signal)
