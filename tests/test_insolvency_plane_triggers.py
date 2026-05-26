import pytest
from app.insolvency_plane.repository import InsolvencyRepository
from app.insolvency_plane.models import DistressTriggerRecord
from app.insolvency_plane.enums import DistressTriggerClass

def test_distress_trigger_manager():
    repo = InsolvencyRepository()
    trigger = DistressTriggerRecord(
        trigger_id="trg-001",
        trigger_class=DistressTriggerClass.CASH_FLOW_INSOLVENCY,
        description="Warning: missed payment",
        lineage_refs=[]
    )
    repo.trigger_manager.add_trigger(trigger)
    assert len(repo.trigger_manager.list_triggers()) == 1
