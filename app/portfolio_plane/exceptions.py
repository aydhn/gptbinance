class PortfolioPlaneError(Exception):
    pass

class InvalidPortfolioObjectError(PortfolioPlaneError):
    pass

class InvalidPrioritizationRecordError(PortfolioPlaneError):
    pass

class InvalidDependencyConstraintError(PortfolioPlaneError):
    pass

class InvalidCommitmentRecordError(PortfolioPlaneError):
    pass

class InvalidFundingRecordError(PortfolioPlaneError):
    pass

class InvalidWipStateError(PortfolioPlaneError):
    pass

class CrowdOutViolationError(PortfolioPlaneError):
    pass

class SequencingViolationError(PortfolioPlaneError):
    pass

class PortfolioStorageError(PortfolioPlaneError):
    pass
