class DataGovernanceError(Exception):
    pass

class InvalidDataContractError(DataGovernanceError):
    pass

class InvalidSchemaVersionError(DataGovernanceError):
    pass

class CompatibilityViolationError(DataGovernanceError):
    pass

class QualityRuleError(DataGovernanceError):
    pass

class CanonicalIdError(DataGovernanceError):
    pass

class LineageIntegrityError(DataGovernanceError):
    pass

class DownstreamImpactError(DataGovernanceError):
    pass

class ProvenanceError(DataGovernanceError):
    pass

class TrustEvaluationError(DataGovernanceError):
    pass
