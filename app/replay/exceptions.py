class ReplayError(Exception):
    pass


class InvalidReplayConfig(ReplayError):
    pass


class MissingReplaySource(ReplayError):
    pass


class SnapshotResolutionError(ReplayError):
    pass


class TimelineReconstructionError(ReplayError):
    pass


class ReplayDeterminismError(ReplayError):
    pass


class CounterfactualError(ReplayError):
    pass


class ReplayDiffError(ReplayError):
    pass


class ForensicBundleError(ReplayError):
    pass


class UnsupportedReplayScopeError(ReplayError):
    pass
