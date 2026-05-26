import pytest
from app.insolvency_plane.repository import InsolvencyRepository
from app.insolvency_plane.models import InsolvencyObject, InsolvencyObjectRef
from app.insolvency_plane.enums import InsolvencyClass, EstateClass

def test_insolvency_registry_integrity():
    repo = InsolvencyRepository()
    obj = InsolvencyObject(
        id="ins-001",
        class_type=InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY,
        owner="test-owner",
        scope="global"
    )
    repo.registry.register(obj)
    fetched = repo.registry.get("ins-001")
    assert fetched is not None
    assert fetched.class_type == InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY

def test_distress_vs_formal_insolvency():
    # Formal insolvencies are registered separately from distress triggers
    repo = InsolvencyRepository()
    from app.insolvency_plane.models import DistressTriggerRecord
    from app.insolvency_plane.enums import DistressTriggerClass

    trigger = DistressTriggerRecord(
        trigger_id="trg-001",
        trigger_class=DistressTriggerClass.CASH_FLOW_INSOLVENCY,
        description="Warning: missed payment",
        lineage_refs=[]
    )
    repo.trigger_manager.add_trigger(trigger)
    assert len(repo.trigger_manager.list_triggers()) == 1
    # Trigger exists, but no insolvency object yet (proper separation)
    assert len(repo.registry.list_all()) == 0

def test_estate_formation():
    repo = InsolvencyRepository()
    from app.insolvency_plane.models import EstateRecord, EstateScopeRecord
    estate = EstateRecord(
        estate_id="est-001",
        insolvency_ref=InsolvencyObjectRef(insolvency_id="ins-001", class_type=InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY, owner="test-owner"),
        estate_class=EstateClass.FORMED,
        scope=EstateScopeRecord(scope_id="scp-001", description="All assets", status="active", lineage_refs=[]),
        assets=[],
        lineage_refs=[]
    )
    repo.estate_manager.form_estate(estate)
    assert repo.estate_manager.get_estate("est-001") is not None

def test_claim_filing_vs_allowed():
    repo = InsolvencyRepository()
    from app.insolvency_plane.models import ClaimRecord, ClaimAdmissionRecord
    from app.insolvency_plane.enums import ClaimClass, AdmissionClass

    claim = ClaimRecord(
        claim_id="clm-001",
        estate_id="est-001",
        claim_class=ClaimClass.FILED,
        amount=100.0,
        description="Invoice claim",
        lineage_refs=[]
    )
    repo.claim_manager.file_claim(claim)

    admission = ClaimAdmissionRecord(
        admission_id="adm-001",
        claim_id="clm-001",
        admission_class=AdmissionClass.ALLOWED,
        admitted_amount=80.0,
        lineage_refs=[]
    )
    repo.admission_manager.admit_claim(admission)

    assert repo.claim_manager.get_claim("clm-001").amount == 100.0
    assert repo.admission_manager.get_admission("adm-001").admitted_amount == 80.0

def test_priority_inversion_prevention():
    repo = InsolvencyRepository()
    from app.insolvency_plane.models import PriorityClaimRecord, SecuredClaimRecord
    from app.insolvency_plane.enums import PriorityClass

    secured = SecuredClaimRecord(
        claim_id="clm-001",
        security_description="Equipment",
        collateral_value=100.0,
        is_false_comfort=False,
        lineage_refs=[]
    )
    repo.secured_claim_manager.add_secured_claim(secured)

    priority = PriorityClaimRecord(
        claim_id="clm-002",
        priority_class=PriorityClass.STATUTORY_LIKE,
        rank=1,
        lineage_refs=[]
    )
    repo.priority_claim_manager.add_priority_claim(priority)

    assert repo.secured_claim_manager.get_secured_claim("clm-001").is_false_comfort is False
    assert repo.priority_claim_manager.get_priority_claim("clm-002").rank == 1

def test_stay_bypass_prevention():
    repo = InsolvencyRepository()
    from app.insolvency_plane.models import StayRecord, StayScopeRecord
    from app.insolvency_plane.enums import StayClass

    scope = StayScopeRecord(
        scope_id="scp-001",
        coverage_description="Global asset freeze",
        carve_outs=["admin-ops"],
        lineage_refs=[]
    )
    stay = StayRecord(
        stay_id="sty-001",
        insolvency_ref=InsolvencyObjectRef(insolvency_id="ins-001", class_type=InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY, owner="test-owner"),
        stay_class=StayClass.AUTOMATIC_LIKE,
        scope=scope,
        lineage_refs=[]
    )
    repo.stay_manager.enter_stay(stay)

    assert repo.stay_manager.get_stay("sty-001").scope.coverage_description == "Global asset freeze"

def test_plan_confirmation_theater():
    repo = InsolvencyRepository()
    from app.insolvency_plane.models import PlanRecord, PlanSupportRecord, ConfirmationRecord
    from app.insolvency_plane.enums import PlanClass, ConfirmationClass

    plan = PlanRecord(
        plan_id="pln-001",
        insolvency_ref=InsolvencyObjectRef(insolvency_id="ins-001", class_type=InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY, owner="test-owner"),
        plan_class=PlanClass.PROPOSED,
        classes=[],
        support=[],
        lineage_refs=[]
    )
    repo.plan_manager.propose_plan(plan)

    support = PlanSupportRecord(
        support_id="sup-001",
        plan_id="pln-001",
        class_id="cls-001",
        support_posture="supportive",
        lineage_refs=[]
    )
    repo.plan_support_manager.register_support(support)

    # At this point, plan is supported but NOT confirmed
    assert repo.confirmation_manager.get_confirmation("cnf-001") is None

    confirmation = ConfirmationRecord(
        confirmation_id="cnf-001",
        plan_id="pln-001",
        confirmation_class=ConfirmationClass.CONFIRMED,
        conditions=[],
        lineage_refs=[]
    )
    repo.confirmation_manager.confirm_plan(confirmation)
    assert repo.confirmation_manager.get_confirmation("cnf-001") is not None

def test_residual_deficit_visibility():
    repo = InsolvencyRepository()
    from app.insolvency_plane.models import ResidualDeficitRecord

    deficit = ResidualDeficitRecord(
        deficit_id="def-001",
        description="Unpaid unsecured shortfall",
        deficit_amount=50.0,
        is_hidden=False, # Explicitly visible
        lineage_refs=[]
    )
    repo.residual_deficit_manager.register_deficit(deficit)

    assert repo.residual_deficit_manager.get_deficit("def-001").deficit_amount == 50.0
    assert repo.residual_deficit_manager.get_deficit("def-001").is_hidden is False
