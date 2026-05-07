from typing import List
import uuid
from app.config_plane.models import EffectiveConfigManifest, ConfigDriftFinding, ConfigParameterRef
from app.config_plane.enums import DriftSeverity
from datetime import datetime, timezone

def detect_drift(expected_manifest: EffectiveConfigManifest, actual_runtime_dict: dict) -> List[ConfigDriftFinding]:
    findings = []

    for key, expected_entry in expected_manifest.entries.items():
        if key in actual_runtime_dict:
            actual_val = actual_runtime_dict[key]
            if actual_val != expected_entry.value:
                findings.append(ConfigDriftFinding(
                    finding_id=f"drift_{uuid.uuid4().hex[:8]}",
                    parameter_ref=expected_entry.parameter_ref,
                    expected_value=expected_entry.value,
                    actual_value=actual_val,
                    severity=DriftSeverity.SEVERE,
                    description=f"Runtime drift detected for {key}"
                ))
    return findings
