import pytest
from app.model_plane.schemas import ModelSchemaRegistry
from app.model_plane.models import ModelSchema, OutputSchema, ModelSchemaVersion
from app.model_plane.enums import OutputClass
from app.model_plane.exceptions import InvalidModelDefinitionError
from datetime import datetime


def test_schema_registry_valid():
    registry = ModelSchemaRegistry()
    schema = ModelSchema(
        schema_id="test_schema_1",
        input_feature_manifest_id="feat_manifest_1",
        output_schema=OutputSchema(
            output_class=OutputClass.SCALAR_SCORE, description="Test output"
        ),
    )
    registry.register_schema(schema)
    assert registry.get_schema("test_schema_1") == schema


def test_schema_registry_missing_fields():
    registry = ModelSchemaRegistry()
    with pytest.raises(InvalidModelDefinitionError):
        registry.register_schema(
            ModelSchema(
                schema_id="",
                input_feature_manifest_id="feat_manifest_1",
                output_schema=OutputSchema(
                    output_class=OutputClass.SCALAR_SCORE, description="Test output"
                ),
            )
        )

    with pytest.raises(InvalidModelDefinitionError):
        registry.register_schema(
            ModelSchema(
                schema_id="schema_2",
                input_feature_manifest_id="",
                output_schema=OutputSchema(
                    output_class=OutputClass.SCALAR_SCORE, description="Test output"
                ),
            )
        )


def test_schema_version_registration():
    registry = ModelSchemaRegistry()
    schema = ModelSchema(
        schema_id="schema_1",
        input_feature_manifest_id="m_1",
        output_schema=OutputSchema(
            output_class=OutputClass.SCALAR_SCORE, description="desc"
        ),
    )
    registry.register_schema(schema)

    version = ModelSchemaVersion(
        version_id="v1", schema_id="schema_1", created_at=datetime.now()
    )
    registry.register_version(version)

    versions = registry.get_versions("schema_1")
    assert len(versions) == 1
    assert versions[0] == version


def test_schema_version_missing_schema():
    registry = ModelSchemaRegistry()
    version = ModelSchemaVersion(
        version_id="v1", schema_id="schema_missing", created_at=datetime.now()
    )
    with pytest.raises(InvalidModelDefinitionError):
        registry.register_version(version)
