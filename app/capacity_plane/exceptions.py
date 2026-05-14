class CapacityPlaneError(Exception):
    pass


class InvalidCapacityDefinition(CapacityPlaneError):
    pass


class InvalidQuotaDefinition(CapacityPlaneError):
    pass


class InvalidReservation(CapacityPlaneError):
    pass


class InvalidAllocation(CapacityPlaneError):
    pass


class InvalidSaturationState(CapacityPlaneError):
    pass


class ThrottlingViolation(CapacityPlaneError):
    pass


class SheddingViolation(CapacityPlaneError):
    pass


class FairnessViolation(CapacityPlaneError):
    pass


class CapacityStorageError(CapacityPlaneError):
    pass
