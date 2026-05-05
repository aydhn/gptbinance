from app.experiments.storage import ExperimentStorage
from app.experiments.repository import ExperimentRepository


def test_experiment_storage_and_repository():
    storage = ExperimentStorage()
    repo = ExperimentRepository(storage)

    repo.save_hypothesis("h_1", {"key": "val"})
    h = repo.get_hypothesis("h_1")
    assert h["key"] == "val"
