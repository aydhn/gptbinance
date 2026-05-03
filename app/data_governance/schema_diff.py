from typing import Dict, List
from app.data_governance.models import DataSchema, SchemaDiffReport, SchemaVersionRef
from app.data_governance.enums import SchemaChangeType

class SchemaDiffAnalyzer:
    def diff(self, from_schema: DataSchema, to_schema: DataSchema) -> SchemaDiffReport:
        changes = {
            SchemaChangeType.FIELD_ADDED: [],
            SchemaChangeType.FIELD_REMOVED: [],
            SchemaChangeType.TYPE_CHANGED: [],
            SchemaChangeType.NULLABILITY_CHANGED: [],
            SchemaChangeType.METADATA_CHANGED: []
        }

        is_breaking = False

        from_fields = {f.name: f for f in from_schema.fields}
        to_fields = {f.name: f for f in to_schema.fields}

        for name, from_f in from_fields.items():
            if name not in to_fields:
                changes[SchemaChangeType.FIELD_REMOVED].append(name)
                is_breaking = True
            else:
                to_f = to_fields[name]
                if from_f.dtype != to_f.dtype:
                    changes[SchemaChangeType.TYPE_CHANGED].append(name)
                    is_breaking = True
                if from_f.nullable and not to_f.nullable:
                    changes[SchemaChangeType.NULLABILITY_CHANGED].append(f"{name} (now required)")
                    is_breaking = True
                elif not from_f.nullable and to_f.nullable:
                     changes[SchemaChangeType.NULLABILITY_CHANGED].append(f"{name} (now nullable)")

        for name in to_fields:
            if name not in from_fields:
                changes[SchemaChangeType.FIELD_ADDED].append(name)
                if not to_fields[name].nullable:
                     # adding required field is a breaking change for producers
                     # we'll conservatively flag it
                     is_breaking = True

        return SchemaDiffReport(
            from_schema=SchemaVersionRef(schema_id=from_schema.schema_id, version=from_schema.version),
            to_schema=SchemaVersionRef(schema_id=to_schema.schema_id, version=to_schema.version),
            changes=changes,
            is_breaking=is_breaking
        )
