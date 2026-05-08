import pytest
from app.model_plane.registry import CanonicalModelRegistry
from app.model_plane.models import ModelDefinition
from app.model_plane.enums import ModelDomain, ModelClass
from app.model_plane.exceptions import InvalidModelDefinitionError


def test_model_registry_valid():
    registry = CanonicalModelRegistry()
    model = ModelDefinition(
        model_id="test_model_1",
        domain=ModelDomain.STRATEGY,
        model_class=ModelClass.SIGNAL_SCORER,
        schema_id="schema_1",
        description="Test model",
    )
    registry.register_model(model)
    assert registry.get_model("test_model_1") == model
    assert len(registry.get_models_by_class(ModelClass.SIGNAL_SCORER)) == 1


def test_model_registry_invalid_id():
    registry = CanonicalModelRegistry()
    with pytest.raises(InvalidModelDefinitionError):
        registry.register_model(
            ModelDefinition(
                model_id="",
                domain=ModelDomain.STRATEGY,
                model_class=ModelClass.SIGNAL_SCORER,
                schema_id="schema_1",
                description="Test",
            )
        )


def test_model_registry_invalid_class():
    registry = CanonicalModelRegistry()
    with pytest.raises(ValueError):
        ModelDefinition(
            model_id="test_model_1",
            domain=ModelDomain.STRATEGY,
            model_class="INVALID_CLASS",
            schema_id="schema_1",
            description="Test",
        )
