import pytest
from app.insolvency_plane.repository import InsolvencyRepository
from app.insolvency_plane.models import PlanRecord, InsolvencyObjectRef
from app.insolvency_plane.enums import PlanClass, InsolvencyClass

def test_plan_manager():
    repo = InsolvencyRepository()
    plan = PlanRecord(
        plan_id="pln-001",
        insolvency_ref=InsolvencyObjectRef(insolvency_id="ins-001", class_type=InsolvencyClass.SETTLEMENT_FAILURE_INSOLVENCY, owner="test-owner"),
        plan_class=PlanClass.PROPOSED,
        classes=[],
        support=[],
        lineage_refs=[]
    )
    repo.plan_manager.propose_plan(plan)
    assert repo.plan_manager.get_plan("pln-001") is not None
