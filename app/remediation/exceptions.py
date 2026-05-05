class RemediationError(Exception):
    pass


class InvalidRemediationRecipe(RemediationError):
    pass


class StaleFindingError(RemediationError):
    pass


class ApplyPolicyViolation(RemediationError):
    pass


class VerificationError(RemediationError):
    pass


class BlastRadiusError(RemediationError):
    pass
