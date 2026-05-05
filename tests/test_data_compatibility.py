from app.data_governance import (
    SchemaCompatibilityChecker,
    DataSchema,
    SchemaField,
    SchemaCompatibility,
)
from datetime import datetime, timezone


def test_schema_compatibility_backward_compatible():
    checker = SchemaCompatibilityChecker()
    schema1 = DataSchema(
        schema_id="s1",
        version="v1",
        fields=[SchemaField(name="id", dtype="str", nullable=False)],
        created_at=datetime.now(timezone.utc),
    )
    schema2 = DataSchema(
        schema_id="s1",
        version="v2",
        fields=[
            SchemaField(name="id", dtype="str", nullable=False),
            SchemaField(
                name="notes", dtype="str", nullable=True
            ),  # Adding nullable field is backward compat
        ],
        created_at=datetime.now(timezone.utc),
    )

    report = checker.check(schema1, schema2)
    assert report.compatibility == SchemaCompatibility.BACKWARD_COMPATIBLE
    assert not report.requires_migration


def test_schema_compatibility_incompatible():
    checker = SchemaCompatibilityChecker()
    schema1 = DataSchema(
        schema_id="s1",
        version="v1",
        fields=[SchemaField(name="id", dtype="str", nullable=False)],
        created_at=datetime.now(timezone.utc),
    )
    schema2 = DataSchema(
        schema_id="s1",
        version="v2",
        fields=[],  # Removed field is breaking
        created_at=datetime.now(timezone.utc),
    )

    report = checker.check(schema1, schema2)
    assert report.compatibility == SchemaCompatibility.INCOMPATIBLE
    assert report.requires_migration
