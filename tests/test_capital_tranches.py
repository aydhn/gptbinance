from app.capital.models import CapitalTranche
from app.capital.tranches import TrancheManager


def test_tranche_activation():
    manager = TrancheManager()
    manager.register_tranche(CapitalTranche(tranche_id="t1", size_amount=100.0))

    act = manager.activate_tranche("t1")
    assert act.active is True

    active = manager.get_active_tranches()
    assert len(active) == 1
    assert manager.get_total_active_tranche_size() == 100.0

    deact = manager.deactivate_tranche("t1")
    assert deact.active is False
    assert manager.get_total_active_tranche_size() == 0.0
