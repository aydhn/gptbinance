from typing import List, Dict, Any
import uuid
from app.config_plane.models import (
    EffectiveConfigManifest,
    ConfigDiffRecord,
    ConfigParameterRef,
)
from app.config_plane.enums import DiffSeverity
from app.config_plane.schemas import registry as schema_registry


def evaluate_diff_severity(
    param_ref: ConfigParameterRef, left_val: Any, right_val: Any
) -> DiffSeverity:
    # A real implementation would examine the magnitude of change or parameter annotations
    return DiffSeverity.MODERATE


def calculate_diff(
    left: EffectiveConfigManifest, right: EffectiveConfigManifest
) -> List[ConfigDiffRecord]:
    diffs = []
    all_keys = set(left.entries.keys()).union(right.entries.keys())

    for key in all_keys:
        left_entry = left.entries.get(key)
        right_entry = right.entries.get(key)

        left_val = left_entry.value if left_entry else None
        right_val = right_entry.value if right_entry else None

        if left_val != right_val:
            domain_str, name_str = key.split(".", 1)
            # Find parameter for mutability class
            schema = schema_registry.get_schema(
                left_entry.parameter_ref.domain
                if left_entry
                else right_entry.parameter_ref.domain
            )
            mutability = (
                schema.parameters[name_str].mutability_class if schema else None
            )

            diffs.append(
                ConfigDiffRecord(
                    diff_id=f"diff_{uuid.uuid4().hex[:8]}",
                    left_manifest_id=left.manifest_id,
                    right_manifest_id=right.manifest_id,
                    parameter_ref=left_entry.parameter_ref
                    if left_entry
                    else right_entry.parameter_ref,
                    left_value=left_val,
                    right_value=right_val,
                    severity=evaluate_diff_severity(
                        left_entry.parameter_ref
                        if left_entry
                        else right_entry.parameter_ref,
                        left_val,
                        right_val,
                    ),
                    mutability_class=mutability,
                )
            )
    return diffs
