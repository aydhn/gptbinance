from app.order_lifecycle.orphans import OrphanManager
from app.order_lifecycle.enums import OrphanSeverity


def test_orphan():
    mgr = OrphanManager()
    rec = mgr.register_orphan("v1", OrphanSeverity.HIGH, "test")
    assert rec.venue_order_id == "v1"
