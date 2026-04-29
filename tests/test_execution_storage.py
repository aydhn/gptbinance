import os
from app.execution.live.storage import ExecutionStorage


def test_execution_storage(tmp_path):
    storage = ExecutionStorage(base_path=str(tmp_path))
    storage.save_audit_record("run1", {"test": "data"})

    audit_file = tmp_path / "run1" / "audit.jsonl"
    assert audit_file.exists()

    with open(audit_file) as f:
        content = f.read()
        assert "data" in content
