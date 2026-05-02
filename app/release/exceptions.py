class ReleaseError(Exception):
    pass


class InvalidReleaseConfig(ReleaseError):
    pass


class BundleBuildError(ReleaseError):
    pass


class HostProbeError(ReleaseError):
    pass


class CompatibilityError(ReleaseError):
    pass


class MigrationError(ReleaseError):
    pass


class UpgradePlanError(ReleaseError):
    pass


class RollbackPlanError(ReleaseError):
    pass


class BootstrapError(ReleaseError):
    pass


class VerificationError(ReleaseError):
    pass
