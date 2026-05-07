# Mock implementation
class EvidenceArtefacts:
    pass

class FeatureEvidenceArtefacts:
    def __init__(self):
        self.families = [
            "feature_definitions",
            "dataset_contracts",
            "feature_manifests",
            "equivalence_skew_drift_reports",
            "trusted_feature_verdicts"
        ]
        self.relations = [
            "computed_from",
            "constrained_by_contract",
            "diverged_feature_from",
            "equivalent_feature_to",
            "leaked_into"
        ]
