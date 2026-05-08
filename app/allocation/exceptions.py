class AllocationPlaneError(Exception):
    pass


class InvalidSleeveDefinition(AllocationPlaneError):
    pass


class InvalidBudget(AllocationPlaneError):
    pass


class InvalidAllocationCandidate(AllocationPlaneError):
    pass


class AllocationConstraintViolation(AllocationPlaneError):
    pass


class ArbitrationError(AllocationPlaneError):
    pass


class NettingError(AllocationPlaneError):
    pass


class CapacityError(AllocationPlaneError):
    pass


class EquivalenceError(AllocationPlaneError):
    pass


class AllocationStorageError(AllocationPlaneError):
    pass
