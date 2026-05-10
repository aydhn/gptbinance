class IncidentSignal:
    def __init__(self, signal_type: str, severity_hint: str, blast_radius: str):
        self.signal_type = signal_type
        self.severity_hint = severity_hint
        self.blast_radius = blast_radius

# Release-plane incident signals:
# - hidden_hotfix_detected
# - release_bundle_incomplete_critical
# - rollout_stage_drift_detected
# - rollback_package_missing
# - release_equivalence_broken
# - runtime_release_manifest_missing
