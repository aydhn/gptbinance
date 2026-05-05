class ExperimentGovernanceError(Exception):
    pass


class InvalidHypothesisError(ExperimentGovernanceError):
    pass


class InvalidExperimentDefinitionError(ExperimentGovernanceError):
    pass


class MissingBaselineError(ExperimentGovernanceError):
    pass


class CandidateScopeMismatchError(ExperimentGovernanceError):
    pass


class ExperimentPolicyViolationError(ExperimentGovernanceError):
    pass


class FragilityAnalysisError(ExperimentGovernanceError):
    pass


class EvidenceInsufficiencyError(ExperimentGovernanceError):
    pass


class PromotionCandidacyError(ExperimentGovernanceError):
    pass


class ExperimentStorageError(ExperimentGovernanceError):
    pass
