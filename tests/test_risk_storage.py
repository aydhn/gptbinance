from datetime import datetime
from app.risk.storage import RiskStorage
from app.risk.models import RiskAuditRecord


def test_storage():
    storage = RiskStorage()
    record = RiskAuditRecord(
        timestamp=datetime.now(),
        run_id="run1",
        symbol="BTC",
        intent_source="st1",
        side="BUY",
        verdict="APPROVE",
        requested_size=1.0,
        approved_size=1.0,
        rationale="Ok",
    )
    storage.save_audit(record)

    res = storage.get_by_run("run1")
    assert len(res) == 1
    assert res[0].symbol == "BTC"
