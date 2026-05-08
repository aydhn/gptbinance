class DataPlaneError(Exception):
    pass


class InvalidSourceDefinition(DataPlaneError):
    pass


class InvalidFieldSchema(DataPlaneError):
    pass


class InvalidTimestampSemantics(DataPlaneError):
    pass


class InvalidRevisionRecord(DataPlaneError):
    pass


class BackfillViolation(DataPlaneError):
    pass


class GapHandlingError(DataPlaneError):
    pass


class AnomalyHandlingError(DataPlaneError):
    pass


class EquivalenceError(DataPlaneError):
    pass


class DataStorageError(DataPlaneError):
    pass
