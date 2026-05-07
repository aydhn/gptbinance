class FeaturePlaneError(Exception):
    pass


class InvalidFeatureDefinitionError(FeaturePlaneError):
    pass


class InvalidDatasetContractError(FeaturePlaneError):
    pass


class LeakageViolationError(FeaturePlaneError):
    pass


class PointInTimeViolationError(FeaturePlaneError):
    pass


class FeatureEquivalenceError(FeaturePlaneError):
    pass


class SkewEvaluationError(FeaturePlaneError):
    pass


class DriftEvaluationError(FeaturePlaneError):
    pass


class FreshnessEvaluationError(FeaturePlaneError):
    pass


class FeatureStorageError(FeaturePlaneError):
    pass
