import pytest
from datetime import datetime, timezone
from app.operating_model_plane.registry import CanonicalOperatingModelRegistry
from app.operating_model_plane.sod import evaluate_sod
from app.operating_model_plane.trust import OperatingModelTrustEngine
from app.operating_model_plane.equivalence import compare_equivalence
from app.operating_model_plane.models import OperatingModelObject, RoleRef, OwnershipAssignment, EscalationChain
from app.operating_model_plane.enums import OperatingObjectClass, RoleClass, OwnershipClass, CoverageClass, EquivalenceVerdict, TrustVerdict
from app.operating_model_plane.exceptions import OwnerlessCriticalSurfaceError, SegregationOfDutiesViolation

def test_ownerless_critical_surface_rejection():
    registry = CanonicalOperatingModelRegistry()
    obj = OperatingModelObject(
        operating_id="crit_1",
        object_class=OperatingObjectClass.SYSTEM_SURFACE,
        is_critical=True,
        primary_owner=None,
        backup_coverage=CoverageClass.NO_COVERAGE,
        escalation_chain=None
    )
    with pytest.raises(OwnerlessCriticalSurfaceError):
        registry.register(obj)

def test_segregation_of_duties_violation():
    role = RoleRef(role_id="user_1", role_name="Dev", role_class=RoleClass.RESPONSIBLE_EXECUTOR)
    with pytest.raises(SegregationOfDutiesViolation):
        evaluate_sod(role, role)

def test_trust_engine():
    role = RoleRef(role_id="user_2", role_name="Lead", role_class=RoleClass.ACCOUNTABLE_OWNER)
    owner = OwnershipAssignment(
        assignment_id="a1", target_id="surf_1", owner_role=role,
        ownership_class=OwnershipClass.PRIMARY, last_attested_at=datetime.now(timezone.utc)
    )
    obj = OperatingModelObject(
        operating_id="surf_1", object_class=OperatingObjectClass.SYSTEM_SURFACE,
        is_critical=True, primary_owner=owner, backup_coverage=CoverageClass.ON_CALL_24_7,
        escalation_chain=None
    )
    engine = OperatingModelTrustEngine()
    verdict = engine.evaluate(obj)
    assert verdict.verdict == TrustVerdict.DEGRADED
    assert verdict.broken_escalation_debt is True

def test_operating_model_equivalence():
    role = RoleRef(role_id="user_2", role_name="Lead", role_class=RoleClass.ACCOUNTABLE_OWNER)
    owner = OwnershipAssignment(
        assignment_id="a1", target_id="surf_1", owner_role=role,
        ownership_class=OwnershipClass.PRIMARY, last_attested_at=datetime.now(timezone.utc)
    )

    paper_obj = OperatingModelObject(
        operating_id="surf_1", object_class=OperatingObjectClass.SYSTEM_SURFACE,
        is_critical=True, primary_owner=owner, backup_coverage=CoverageClass.ON_CALL_24_7, escalation_chain=None
    )
    live_obj = OperatingModelObject(
        operating_id="surf_1", object_class=OperatingObjectClass.SYSTEM_SURFACE,
        is_critical=True, primary_owner=owner, backup_coverage=CoverageClass.BUSINESS_HOURS_ONLY, escalation_chain=None
    )

    assert compare_equivalence(paper_obj, live_obj) == EquivalenceVerdict.DIVERGED_COVERAGE
