import pytest
from app.data_governance import SchemaRegistry, DataSchema, SchemaField, SchemaVersionRef, InvalidSchemaVersionError
from datetime import datetime, timezone

def test_schema_registration():
    registry = SchemaRegistry()
    schema = DataSchema(
        schema_id="s1",
        version="v1",
        fields=[SchemaField(name="id", dtype="str", nullable=False)],
        created_at=datetime.now(timezone.utc)
    )
    registry.register_schema(schema)
    s = registry.get_schema(SchemaVersionRef(schema_id="s1", version="v1"))
    assert s.schema_id == "s1"

def test_schema_not_found():
    registry = SchemaRegistry()
    with pytest.raises(InvalidSchemaVersionError):
         registry.get_schema(SchemaVersionRef(schema_id="s1", version="v1"))
