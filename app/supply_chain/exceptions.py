class SupplyChainError(Exception):
    """Base exception for supply chain integrity."""


class InvalidSourceSnapshotError(SupplyChainError):
    pass


class InvalidDependencySnapshotError(SupplyChainError):
    pass


class LockIntegrityViolation(SupplyChainError):
    pass


class BuildProvenanceError(SupplyChainError):
    pass


class ReproducibilityError(SupplyChainError):
    pass


class AttestationError(SupplyChainError):
    pass


class RuntimeEquivalenceError(SupplyChainError):
    pass


class TrustVerdictError(SupplyChainError):
    pass


class SupplyChainStorageError(SupplyChainError):
    pass
