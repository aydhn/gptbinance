from app.data_governance.models import DataSchema, CompatibilityReport, SchemaVersionRef
from app.data_governance.enums import SchemaCompatibility
from app.data_governance.schema_diff import SchemaDiffAnalyzer

class SchemaCompatibilityChecker:
    def __init__(self):
        self.diff_analyzer = SchemaDiffAnalyzer()

    def check(self, from_schema: DataSchema, to_schema: DataSchema) -> CompatibilityReport:
        diff_report = self.diff_analyzer.diff(from_schema, to_schema)

        if not diff_report.is_breaking:
             # If there are changes but they are not breaking, it's backward compatible at least
             # If no changes, fully compatible
             has_changes = any(len(v) > 0 for v in diff_report.changes.values())
             compatibility = SchemaCompatibility.BACKWARD_COMPATIBLE if has_changes else SchemaCompatibility.FULLY_COMPATIBLE
             requires_migration = False
        else:
             compatibility = SchemaCompatibility.INCOMPATIBLE
             requires_migration = True

        breaking_changes = []
        if diff_report.is_breaking:
            breaking_changes.extend([f"Removed: {f}" for f in diff_report.changes.get(SchemaChangeType.FIELD_REMOVED, [])])
            breaking_changes.extend([f"Type changed: {f}" for f in diff_report.changes.get(SchemaChangeType.TYPE_CHANGED, [])])
            # add more logic as needed for reporting breaking changes

        return CompatibilityReport(
            from_schema=SchemaVersionRef(schema_id=from_schema.schema_id, version=from_schema.version),
            to_schema=SchemaVersionRef(schema_id=to_schema.schema_id, version=to_schema.version),
            compatibility=compatibility,
            breaking_changes=breaking_changes,
            requires_migration=requires_migration
        )
