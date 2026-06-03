class MetaGovernancePlaneError(Exception):
    pass

class InvalidMetaGovernanceObjectError(MetaGovernancePlaneError):
    pass

class InvalidProposalError(MetaGovernancePlaneError):
    pass

class InvalidCanonVersionError(MetaGovernancePlaneError):
    pass

class InvalidSupersessionError(MetaGovernancePlaneError):
    pass

class InvalidDeprecationError(MetaGovernancePlaneError):
    pass

class InvalidMigrationError(MetaGovernancePlaneError):
    pass

class MetaGovernanceTheaterViolation(MetaGovernancePlaneError):
    pass

class MetaGovernanceStorageError(MetaGovernancePlaneError):
    pass
