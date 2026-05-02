from app.security.storage import SecurityStorage
import os


def test_storage(tmp_path):
    storage = SecurityStorage()
    storage.save_record(str(tmp_path), "test.json", '{"a": 1}')
    assert os.path.exists(tmp_path / "test.json")
