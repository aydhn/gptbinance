import os

files = {}

files["app/incident_plane/__init__.py"] = ""

files["app/incident_plane/enums.py"] = """from enum import Enum

class IncidentSeverity(str, Enum):
    SEV0_EMERGENCY = "sev0_emergency"
    SEV1_HIGH = "sev1_high"
    SEV2_MEDIUM = "sev2_medium"
    SEV3_LOW = "sev3_low"
    ADVISORY_ONLY = "advisory_only"

class IncidentUrgency(str, Enum):
    IMMEDIATE = "immediate"
    TIME_BOUNDED = "time_bounded"
    REVIEW_WINDOW = "review_window"
    BACKLOG = "backlog"

class IncidentStatus(str, Enum):
    DETECTED = "detected"
    TRIAGING = "triaging"
    INVESTIGATING = "investigating"
    CONTAINING = "containing"
    STABILIZED = "stabilized"
    RECOVERING = "recovering"
    VERIFYING = "verifying"
    RESOLVED = "resolved"
    CLOSED = "closed"
    REOPENED = "reopened"
    FALSE_POSITIVE = "false_positive"

class VerificationVerdict(str, Enum):
    VERIFIED = "verified"
    FAILED = "failed"
    PENDING_QUIET_PERIOD = "pending_quiet_period"
    INCONCLUSIVE = "inconclusive"

class IncidentTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
"""

files["app/incident_plane/exceptions.py"] = """class IncidentPlaneError(Exception):
    pass

class InvalidStatusTransition(IncidentPlaneError):
    pass

class InvalidClosureState(IncidentPlaneError):
    pass

class InvalidSeverityEscalation(IncidentPlaneError):
    pass

class MissingRecoveryVerification(IncidentPlaneError):
    pass
"""

files["app/incident_plane/models.py"] = """from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from app.incident_plane.enums import IncidentSeverity, IncidentUrgency, IncidentStatus, VerificationVerdict

class IncidentSignal(BaseModel):
    signal_id: str
    source_system: str
    raw_payload: Dict[str, Any]
    detected_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    confidence_score: float

class IncidentTriageRecord(BaseModel):
    incident_id: str
    provisional_facts: List[str]
    hypotheses: List[str]
    missing_information_blockers: List[str]
    proof_notes: str
    triaged_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    triaged_by: str

class RecoveryVerificationRecord(BaseModel):
    incident_id: str
    objective_checks_passed: bool
    no_regression_checks_passed: bool
    quiet_period_met: bool
    residual_risk_assessment: str
    verdict: VerificationVerdict
    verified_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    verified_by: str
    proof_notes: str

class IncidentStatusEvent(BaseModel):
    incident_id: str
    previous_status: Optional[IncidentStatus]
    new_status: IncidentStatus
    reason: str
    transitioned_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    transitioned_by: str

class IncidentManifest(BaseModel):
    incident_id: str
    family: str
    severity: IncidentSeverity
    urgency: IncidentUrgency
    current_status: IncidentStatus
    blast_radius: Dict[str, Any]
    primary_owner: str
    signals: List[IncidentSignal] = Field(default_factory=list)
    triage: Optional[IncidentTriageRecord] = None
    timeline: List[IncidentStatusEvent] = Field(default_factory=list)
    verification: Optional[RecoveryVerificationRecord] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
"""

files["app/incident_plane/status.py"] = """from typing import List
from datetime import datetime, timezone
from app.incident_plane.enums import IncidentStatus
from app.incident_plane.exceptions import InvalidStatusTransition
from app.incident_plane.models import IncidentStatusEvent

class IncidentStatusMachine:
    VALID_TRANSITIONS = {
        IncidentStatus.DETECTED: [IncidentStatus.TRIAGING, IncidentStatus.FALSE_POSITIVE],
        IncidentStatus.TRIAGING: [IncidentStatus.INVESTIGATING, IncidentStatus.FALSE_POSITIVE],
        IncidentStatus.INVESTIGATING: [IncidentStatus.CONTAINING, IncidentStatus.RECOVERING],
        IncidentStatus.CONTAINING: [IncidentStatus.STABILIZED, IncidentStatus.RECOVERING],
        IncidentStatus.STABILIZED: [IncidentStatus.RECOVERING],
        IncidentStatus.RECOVERING: [IncidentStatus.VERIFYING],
        IncidentStatus.VERIFYING: [IncidentStatus.RESOLVED, IncidentStatus.REOPENED],
        IncidentStatus.RESOLVED: [IncidentStatus.CLOSED, IncidentStatus.REOPENED],
        IncidentStatus.CLOSED: [IncidentStatus.REOPENED],
        IncidentStatus.REOPENED: [IncidentStatus.TRIAGING, IncidentStatus.INVESTIGATING],
        IncidentStatus.FALSE_POSITIVE: []
    }

    @staticmethod
    def transition(current: IncidentStatus, target: IncidentStatus, reason: str, operator: str, incident_id: str = "TBD") -> IncidentStatusEvent:
        if target not in IncidentStatusMachine.VALID_TRANSITIONS.get(current, []):
            raise InvalidStatusTransition(f"Cannot transition from {current} to {target}. Rule violation.")

        return IncidentStatusEvent(
            incident_id=incident_id,
            previous_status=current,
            new_status=target,
            reason=reason,
            transitioned_by=operator
        )
"""

files["app/incident_plane/closure.py"] = """from app.incident_plane.models import IncidentManifest
from app.incident_plane.enums import IncidentStatus, VerificationVerdict, IncidentSeverity
from app.incident_plane.exceptions import InvalidClosureState

class ClosureReadinessEvaluator:
    @staticmethod
    def assert_ready_for_closure(manifest: IncidentManifest) -> bool:
        if manifest.current_status != IncidentStatus.RESOLVED:
            raise InvalidClosureState(f"Incident {manifest.incident_id} must be in RESOLVED state before CLOSURE.")

        if not manifest.verification or manifest.verification.verdict != VerificationVerdict.VERIFIED:
            raise InvalidClosureState(f"Incident {manifest.incident_id} lacks successful recovery verification. Closure blocked.")

        if manifest.severity in [IncidentSeverity.SEV0_EMERGENCY, IncidentSeverity.SEV1_HIGH]:
            pass # Postmortem check placeholder

        return True
"""

files["app/incident_plane/trust.py"] = """from app.incident_plane.models import IncidentManifest
from app.incident_plane.enums import IncidentTrustVerdict, IncidentStatus, VerificationVerdict, IncidentSeverity

class IncidentTrustEngine:
    @staticmethod
    def evaluate(manifest: IncidentManifest) -> IncidentTrustVerdict:
        if manifest.current_status not in [IncidentStatus.CLOSED, IncidentStatus.RESOLVED, IncidentStatus.FALSE_POSITIVE]:
            if manifest.severity == IncidentSeverity.SEV0_EMERGENCY:
                return IncidentTrustVerdict.BLOCKED
            if manifest.severity == IncidentSeverity.SEV1_HIGH:
                return IncidentTrustVerdict.DEGRADED

        if manifest.current_status in [IncidentStatus.RESOLVED, IncidentStatus.CLOSED]:
            if not manifest.verification or manifest.verification.verdict != VerificationVerdict.VERIFIED:
                return IncidentTrustVerdict.REVIEW_REQUIRED

        return IncidentTrustVerdict.TRUSTED
"""

files["app/incident_plane/registry.py"] = """from typing import List

class CanonicalIncidentRegistry:
    FAMILIES = [
        "data_integrity_incident",
        "execution_integrity_incident",
        "risk_breach_incident",
        "release_integrity_incident",
        "workflow_integrity_incident",
        "control_integrity_incident",
        "performance_integrity_incident",
        "strategy_integrity_incident",
        "simulation_integrity_incident",
        "market_truth_incident",
        "capital_ledger_incident",
        "crossbook_conflict_incident"
    ]

    @staticmethod
    def is_valid_family(family: str) -> bool:
        return family in CanonicalIncidentRegistry.FAMILIES
"""

files["app/incident_plane/repository.py"] = """from typing import Dict, Optional
from app.incident_plane.models import IncidentManifest

class IncidentRepository:
    def __init__(self):
        self._store: Dict[str, IncidentManifest] = {}

    def save(self, manifest: IncidentManifest):
        self._store[manifest.incident_id] = manifest

    def get_manifest(self, incident_id: str) -> Optional[IncidentManifest]:
        return self._store.get(incident_id)
"""

files["app/incident_plane/reporting.py"] = """from app.incident_plane.models import IncidentManifest, RecoveryVerificationRecord

class IncidentReporter:
    def format_registry(self) -> str:
        from app.incident_plane.registry import CanonicalIncidentRegistry
        lines = ["CANONICAL INCIDENT REGISTRY"]
        lines.extend([f" - {fam}" for fam in CanonicalIncidentRegistry.FAMILIES])
        return "\\n".join(lines)

    def format_manifest(self, manifest: IncidentManifest) -> str:
        if not manifest:
            return "Incident not found."
        lines = [
            f"INCIDENT MANIFEST [{manifest.incident_id}]",
            f"Family: {manifest.family}",
            f"Severity: {manifest.severity.value.upper()}",
            f"Urgency: {manifest.urgency.value.upper()}",
            f"Status: {manifest.current_status.value.upper()}",
            f"Owner: {manifest.primary_owner}",
            f"Blast Radius: {manifest.blast_radius}"
        ]
        return "\\n".join(lines)

    def format_verification(self, verification: RecoveryVerificationRecord) -> str:
        if not verification:
            return "No verification record found."
        lines = [
            f"RECOVERY VERIFICATION [{verification.incident_id}]",
            f"Verdict: {verification.verdict.value.upper()}",
            f"Objective Checks Passed: {verification.objective_checks_passed}",
            f"No-Regression Passed: {verification.no_regression_checks_passed}",
            f"Quiet Period Met: {verification.quiet_period_met}",
            f"Proof Notes: {verification.proof_notes}"
        ]
        return "\\n".join(lines)
"""

files["app/main.py"] = """import argparse
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def setup_incident_cli(parser: argparse.ArgumentParser):
    group = parser.add_argument_group("Incident Plane Governance")
    group.add_argument("--show-incident-registry", action="store_true", help="Show registered incident families")
    group.add_argument("--show-incident", type=str, metavar="ID", help="Show incident manifest")
    group.add_argument("--show-incident-verification", type=str, metavar="ID", help="Show recovery verification details")
    group.add_argument("--show-incident-trust", type=str, metavar="ID", help="Show trust verdict")

def handle_incident_commands(args):
    from app.incident_plane.reporting import IncidentReporter
    from app.incident_plane.repository import IncidentRepository
    from app.incident_plane.trust import IncidentTrustEngine
    from app.incident_plane.models import IncidentManifest
    from app.incident_plane.enums import IncidentSeverity, IncidentUrgency, IncidentStatus

    repo = IncidentRepository()
    reporter = IncidentReporter()

    # Mock data for demonstration
    manifest = IncidentManifest(
        incident_id="INC-20231024-001",
        family="execution_integrity_incident",
        severity=IncidentSeverity.SEV1_HIGH,
        urgency=IncidentUrgency.IMMEDIATE,
        current_status=IncidentStatus.RECOVERING,
        blast_radius={"scope": "Live Execution Engine", "symbol": "BTCUSDT"},
        primary_owner="operator_alpha"
    )
    repo.save(manifest)

    if args.show_incident_registry:
        print(reporter.format_registry())
        sys.exit(0)

    if args.show_incident:
        res = repo.get_manifest(args.show_incident)
        print(reporter.format_manifest(res))
        sys.exit(0)

    if args.show_incident_verification:
        res = repo.get_manifest(args.show_incident_verification)
        print(reporter.format_verification(res.verification if res else None))
        sys.exit(0)

    if args.show_incident_trust:
        res = repo.get_manifest(args.show_incident_trust)
        if res:
            verdict = IncidentTrustEngine.evaluate(res)
            print(f"Incident Trust Verdict for {res.incident_id}: {verdict.value.upper()}")
        else:
            print("Incident not found.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trading Platform CLI")
    setup_incident_cli(parser)
    args, unknown = parser.parse_known_args()

    if any([args.show_incident_registry, args.show_incident, args.show_incident_verification, args.show_incident_trust]):
        handle_incident_commands(args)
    else:
        print("Use --help to see available Incident Plane commands.")
"""

files["tests/test_incident_plane_governance.py"] = """import pytest
from app.incident_plane.status import IncidentStatusMachine
from app.incident_plane.closure import ClosureReadinessEvaluator
from app.incident_plane.enums import IncidentStatus, IncidentSeverity, IncidentUrgency, VerificationVerdict
from app.incident_plane.exceptions import InvalidStatusTransition, InvalidClosureState
from app.incident_plane.models import IncidentManifest, RecoveryVerificationRecord
from datetime import datetime, timezone

def test_status_transition_enforces_rules():
    event = IncidentStatusMachine.transition(IncidentStatus.DETECTED, IncidentStatus.TRIAGING, "Start Triage", "operator_1")
    assert event.new_status == IncidentStatus.TRIAGING

    with pytest.raises(InvalidStatusTransition):
        IncidentStatusMachine.transition(IncidentStatus.DETECTED, IncidentStatus.RESOLVED, "Quick fix", "operator_1")

def test_closure_requires_verification():
    manifest = IncidentManifest(
        incident_id="INC-001",
        family="data_integrity_incident",
        severity=IncidentSeverity.SEV2_MEDIUM,
        urgency=IncidentUrgency.TIME_BOUNDED,
        current_status=IncidentStatus.RESOLVED,
        blast_radius={"scope": "market_data"},
        primary_owner="operator_1",
        signals=[],
        triage=None,
        timeline=[],
        verification=None,
        created_at=datetime.now(timezone.utc),
        updated_at=datetime.now(timezone.utc)
    )

    with pytest.raises(InvalidClosureState, match="lacks successful recovery verification"):
        ClosureReadinessEvaluator.assert_ready_for_closure(manifest)

    manifest.verification = RecoveryVerificationRecord(
        incident_id="INC-001",
        objective_checks_passed=True,
        no_regression_checks_passed=True,
        quiet_period_met=True,
        residual_risk_assessment="None",
        verdict=VerificationVerdict.VERIFIED,
        verified_by="operator_2",
        proof_notes="Logs checked, data flowing",
        verified_at=datetime.now(timezone.utc)
    )

    assert ClosureReadinessEvaluator.assert_ready_for_closure(manifest) is True
"""

files["docs/386_incident_plane_ve_response_recovery_governance_mimarisi.md"] = """# Phase 76: Incident Plane & Response Recovery Governance

This document outlines the architecture for the Incident Plane.

## Core Flow
`Signals -> Triage -> Incident -> Containment -> Recovery -> Verification -> Closure`

## Key Principles
1. **Containment != Recovery != Resolved**: An incident being contained does not mean it has recovered. Recovery does not mean it can be closed.
2. **No Hidden Severity Changes**: All escalations and downgrades must be logged and justified.
3. **Recovery Verification is Mandatory**: An incident cannot enter a `CLOSED` state without explicit, documented verification.
"""

files["docs/390_phase_76_definition_of_done.md"] = """# Phase 76 Definition of Done

## Completion Criteria
- Incident plane framework is operational.
- Canonical incident registry, signals, and triage surfaces exist.
- State transitions enforce strict logic (e.g., Verification is required for Closure).
- Trust logic propagates incident impact correctly to other planes.
- CLI handles incident querying.
- Tests pass.

## Deferred
- Automatic execution halts (Auto-Rollbacks/Auto-Kills).
- Integration with external Pager/Ticketing SaaS APIs.

## Proceed to Next Phase
Phase 77 will cover Remediation Orchestration & Debt Governance.
"""

for path, content in files.items():
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

print("Project structure created successfully.")
