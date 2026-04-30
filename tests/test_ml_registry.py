from app.ml.registry import ModelRegistry
from app.ml.models import ModelRegistryEntry
from app.ml.enums import RegistryStage, ModelStatus


def test_model_registry():
    registry = ModelRegistry()
    entry = ModelRegistryEntry(
        run_id="run_1",
        stage=RegistryStage.CANDIDATE,
        status=ModelStatus.INACTIVE,
        dataset_id="ds_1",
    )

    registry.register(entry)
    retrieved = registry.get("run_1")

    assert retrieved.stage == RegistryStage.CANDIDATE
