class CrossBookError(Exception):
    pass

class InvalidPositionMappingError(CrossBookError):
    pass

class ExposureGraphError(CrossBookError):
    pass

class CollateralDependencyError(CrossBookError):
    pass

class BorrowDependencyError(CrossBookError):
    pass

class FakeHedgeDetectionError(CrossBookError):
    pass

class LiquidationSensitivityError(CrossBookError):
    pass

class ScopeMismatchError(CrossBookError):
    pass

class StaleSnapshotError(CrossBookError):
    pass

class OverlayEvaluationError(CrossBookError):
    pass
