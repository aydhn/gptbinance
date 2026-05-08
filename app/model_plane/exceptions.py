class ModelPlaneError(Exception):
    pass


class InvalidModelDefinitionError(ModelPlaneError):
    pass


class InvalidInferenceContractError(ModelPlaneError):
    pass


class InvalidCheckpointRecordError(ModelPlaneError):
    pass


class CalibrationError(ModelPlaneError):
    pass


class UncertaintyError(ModelPlaneError):
    pass


class ServingEquivalenceError(ModelPlaneError):
    pass


class ThresholdPolicyViolation(ModelPlaneError):
    pass


class ModelDriftError(ModelPlaneError):
    pass


class ModelStorageError(ModelPlaneError):
    pass
