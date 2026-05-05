class PolicyKernelError(Exception):
    pass


class InvalidPolicyRuleError(PolicyKernelError):
    pass


class InvalidInvariantError(PolicyKernelError):
    pass


class PolicyConflictError(PolicyKernelError):
    pass


class PrecedenceResolutionError(PolicyKernelError):
    pass


class StaleEvidencePolicyError(PolicyKernelError):
    pass


class NonWaivableRuleError(PolicyKernelError):
    pass


class PolicyDriftError(PolicyKernelError):
    pass


class ProofGenerationError(PolicyKernelError):
    pass


class PolicyStorageError(PolicyKernelError):
    pass
