from app.backtest.exceptions import BacktestError


class WalkForwardError(BacktestError):
    pass


class InvalidWalkForwardConfigError(WalkForwardError):
    pass


class InvalidWindowPlanError(WalkForwardError):
    pass


class CandidateSelectionError(WalkForwardError):
    pass


class FrozenBundleError(WalkForwardError):
    pass


class OOSAggregationError(WalkForwardError):
    pass


class PromotionGateError(WalkForwardError):
    pass
