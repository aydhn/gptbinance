from app.ml.storage import MlStorage


def test_ml_storage():
    storage = MlStorage("/tmp/ml_test")
    assert storage.base_dir == "/tmp/ml_test"
