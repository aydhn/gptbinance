class MlError(Exception):
    """Base exception for ML layer."""

    pass


class InvalidDatasetSpecError(MlError):
    pass


class InvalidLabelSpecError(MlError):
    pass


class TrainingError(MlError):
    pass


class EvaluationError(MlError):
    pass


class CalibrationError(MlError):
    pass


class RegistryError(MlError):
    pass


class DriftError(MlError):
    pass


class InferenceError(MlError):
    pass


class PromotionGateError(MlError):
    pass
