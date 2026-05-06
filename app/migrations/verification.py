from app.migrations.models import MigrationPlan, MigrationVerificationResult
from app.migrations.enums import MigrationVerdict


class VerificationEngine:
    def verify(self, plan: MigrationPlan) -> MigrationVerificationResult:
        # Mock verification logic
        return MigrationVerificationResult(
            plan_id=plan.id,
            verdict=MigrationVerdict.SUCCESS,
            target_versions_reached=True,
            compatibility_preserved=True,
            policy_kernel_clean=True,
            evidence_integrity_preserved=True,
            shadow_state_integrity_preserved=True,
            notes="All verifications passed.",
        )

import uuid
from typing import Dict, Any
from app.incidents.enums import SignalType, IncidentSeverity, IncidentScopeType
from app.incidents.signals import SignalMapper
from app.incidents.intake import IncidentCommand

def emit_migration_failed_signal(workspace_id: str, details: Dict[str, Any] = None):
    cmd = IncidentCommand()
    signal = SignalMapper.create_signal(
        signal_id=f"mig-{uuid.uuid4().hex[:8]}",
        signal_type=SignalType.MIGRATION_FAILED,
        domain="migration",
        scope_type=IncidentScopeType.WORKSPACE,
        scope_ref=workspace_id,
        severity=IncidentSeverity.CRITICAL_INCIDENT,
        details=details or {"reason": "Migration failed"}
    )
    cmd.ingest_signal(signal)
