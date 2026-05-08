import pytest
import os
import shutil
from pathlib import Path
from app.model_plane.storage import ModelPlaneStorage
from app.model_plane.repository import ModelPlaneRepository
from app.model_plane.models import ModelDefinition
from app.model_plane.enums import ModelDomain, ModelClass


@pytest.fixture
def temp_storage_path(tmp_path):
    path = tmp_path / "model_plane_data"
    yield str(path)
    if path.exists():
        shutil.rmtree(path)


def test_storage_save_load(temp_storage_path):
    storage = ModelPlaneStorage(base_path=temp_storage_path)
    repo = ModelPlaneRepository(storage)

    model = ModelDefinition(
        model_id="m1",
        domain=ModelDomain.STRATEGY,
        model_class=ModelClass.SIGNAL_SCORER,
        schema_id="s1",
        description="test",
    )

    repo.save_model(model)
    loaded_model = repo.get_model("m1")

    assert loaded_model is not None
    assert loaded_model.model_id == "m1"
    assert loaded_model.domain == ModelDomain.STRATEGY


def test_storage_load_missing(temp_storage_path):
    storage = ModelPlaneStorage(base_path=temp_storage_path)
    repo = ModelPlaneRepository(storage)

    loaded_model = repo.get_model("missing_model")
    assert loaded_model is None
