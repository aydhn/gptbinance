# Mock implementation
class PostmortemContributors:
    pass


# Added Postmortem Contributors
CONTRIBUTORS = [
    "build_provenance_gap",
    "dependency_drift",
    "missing_attestation",
    "runtime_equivalence_mismatch",
    "non_deterministic_build",
]

class FeaturePostmortemContributors:
    def __init__(self):
        self.contributors = [
            "feature_leakage",
            "stale_feature_surfaces",
            "skew",
            "broken_dataset_contract",
            "hidden_transform_chain",
            "replay_contamination"
        ]
