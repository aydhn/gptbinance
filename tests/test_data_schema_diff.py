from app.data_governance import SchemaDiffAnalyzer, DataSchema, SchemaField, SchemaChangeType
from datetime import datetime, timezone

def test_schema_diff_analyzer():
    analyzer = SchemaDiffAnalyzer()
    schema1 = DataSchema(
        schema_id="s1", version="v1",
        fields=[SchemaField(name="id", dtype="str", nullable=False)],
        created_at=datetime.now(timezone.utc)
    )
    schema2 = DataSchema(
        schema_id="s1", version="v2",
        fields=[SchemaField(name="id", dtype="int", nullable=False)], # Type change
        created_at=datetime.now(timezone.utc)
    )

    report = analyzer.diff(schema1, schema2)
    assert report.is_breaking
    assert "id" in report.changes[SchemaChangeType.TYPE_CHANGED]
