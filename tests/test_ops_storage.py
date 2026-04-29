from app.ops.storage import OpsStorage
from app.ops.repository import OpsRepository
from app.ops.models import OpsAuditRecord


def test_storage_append_and_load(tmp_path):
    storage = OpsStorage(str(tmp_path))
    repo = OpsRepository(storage)

    rec1 = OpsAuditRecord(run_id="run-x", action="test1", details="")
    rec2 = OpsAuditRecord(run_id="run-x", action="test2", details="")

    repo.append_audit_record(rec1)
    repo.append_audit_record(rec2)

    loaded = repo.get_audit_records("run-x")
    assert len(loaded) == 2
    assert loaded[0].action == "test1"
    assert loaded[1].action == "test2"
