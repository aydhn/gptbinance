import pytest
from datetime import datetime, timezone, timedelta
from app.compliance_plane.models import (
    ComplianceRequirement,
    ControlObjective,
    ControlMapping,
    ComplianceRequirementRef,
    ControlObjectiveRef,
    AttestationRecord,
    ExceptionAcceptanceRecord,
    ComplianceRemediation,
    ComplianceEquivalenceReport,
)
from app.compliance_plane.enums import (
    RequirementClass,
    ControlClass,
    EvidenceClass,
    AttestationClass,
    ExceptionClass,
    EquivalenceVerdict,
)
from app.compliance_plane.registry import CanonicalComplianceRegistry
from app.compliance_plane.mappings import MappingRegistry
from app.compliance_plane.attestations import AttestationManager
from app.compliance_plane.exceptions_records import ExceptionManager
from app.compliance_plane.remediation import RemediationManager
from app.compliance_plane.equivalence import EquivalenceManager
from app.compliance_plane.exceptions import (
    InvalidRequirementDefinition,
    InvalidControlMapping,
)


def test_registry_requirement():
    registry = CanonicalComplianceRegistry()
    req = ComplianceRequirement(
        requirement_id="req-001",
        requirement_class=RequirementClass.ACCESS_CONTROL,
        scope={"env": "live"},
        owner_id="user-1",
        satisfaction_criteria="All access logged.",
        review_cadence_days=90,
        failure_severity="high",
        lineage_refs=[],
        is_mandatory=True,
    )
    registry.register_requirement(req)
    fetched = registry.get_requirement("req-001")
    assert fetched is not None
    assert fetched.requirement_id == "req-001"


def test_registry_control():
    registry = CanonicalComplianceRegistry()
    ctrl = ControlObjective(
        control_id="ctrl-001",
        control_class=ControlClass.PREVENTIVE,
        owner_id="user-1",
        cadence_days=30,
        is_automated=True,
        is_preventive=True,
        is_detective=False,
        is_corrective=False,
        is_compensating=False,
    )
    registry.register_control(ctrl)
    fetched = registry.get_control("ctrl-001")
    assert fetched is not None
    assert fetched.control_id == "ctrl-001"


def test_mapping_registry():
    mappings = MappingRegistry()
    mapping = ControlMapping(
        mapping_id="map-001",
        requirement_refs=[ComplianceRequirementRef(requirement_id="req-001")],
        control_ref=ControlObjectiveRef(control_id="ctrl-001"),
        evidence_classes_required=[EvidenceClass.SYSTEM_LOG],
    )
    mappings.register_mapping(mapping)
    req_maps = mappings.get_mappings_for_requirement("req-001")
    assert len(req_maps) == 1


def test_attestation_staleness():
    manager = AttestationManager()
    now = datetime.now(timezone.utc)
    att = AttestationRecord(
        attestation_id="att-001",
        attestation_class=AttestationClass.OPERATOR,
        target_ref="req-001",
        attester_id="user-1",
        attested_at=now - timedelta(days=10),
        expires_at=now - timedelta(days=1),  # Expired
        is_stale=False,
    )
    manager.register_attestation(att)
    manager.update_stale_states()
    assert manager.list_attestations()[0].is_stale is True


def test_exception_staleness():
    manager = ExceptionManager()
    now = datetime.now(timezone.utc)
    exc = ExceptionAcceptanceRecord(
        exception_id="exc-001",
        exception_class=ExceptionClass.SCOPE_BOUND,
        target_ref="req-001",
        scope={"env": "live"},
        reason="Legacy system",
        approver_ids=["user-1"],
        accepted_at=now - timedelta(days=10),
        expires_at=now - timedelta(days=1),  # Expired
        residual_risk_note="High",
        is_stale=False,
    )
    manager.register_exception(exc)
    manager.update_stale_states()
    assert manager.list_exceptions()[0].is_stale is True


def test_remediation_overdue():
    manager = RemediationManager()
    now = datetime.now(timezone.utc)
    rem = ComplianceRemediation(
        remediation_id="rem-001",
        finding_ref="find-001",
        owner_id="user-1",
        due_at=now - timedelta(days=1),  # Overdue
        verification_required=True,
        is_blocking=False,
        is_overdue=False,
        lineage_refs=[],
    )
    manager.register_remediation(rem)
    manager.update_overdue_states()
    assert manager.list_remediations()[0].is_overdue is True


def test_equivalence():
    manager = EquivalenceManager()
    rep = ComplianceEquivalenceReport(
        report_id="eq-001",
        target_requirement_ref=ComplianceRequirementRef(requirement_id="req-001"),
        verdict=EquivalenceVerdict.EQUIVALENT,
        replay_posture={"status": "ok"},
        paper_posture={"status": "ok"},
        probation_posture={"status": "ok"},
        live_posture={"status": "ok"},
    )
    manager.register_report(rep)
    assert len(manager.list_reports()) == 1
