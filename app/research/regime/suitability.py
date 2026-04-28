from app.research.regime.enums import (
    RegimeFamily,
    SuitabilityVerdict,
    TrendRegime,
    VolatilityRegime,
)
from app.research.regime.models import (
    RegimeContext,
    RegimeSuitabilityMap,
    StrategyRegimeCompatibility,
)


def calculate_suitability(context: RegimeContext) -> RegimeSuitabilityMap:
    """
    Maps current regime context to strategy suitability.
    """
    compatibilities = {}

    trend_eval = context.evaluations.get(RegimeFamily.TREND)
    vol_eval = context.evaluations.get(RegimeFamily.VOLATILITY)

    trend_name = trend_eval.label.name if trend_eval else ""
    vol_name = vol_eval.label.name if vol_eval else ""

    # 1. Trend Following Strategy Family
    tf_verdict = SuitabilityVerdict.CAUTION
    tf_score = 0.5
    tf_rationale = "Neutral environment for trend following."
    if trend_name in [
        TrendRegime.STRONG_UPTREND.name,
        TrendRegime.STRONG_DOWNTREND.name,
    ]:
        if vol_name != VolatilityRegime.NOISY_HIGH_VOL.name:
            tf_verdict = SuitabilityVerdict.OPTIMAL
            tf_score = 0.9
            tf_rationale = "Strong trend detected without excessive noise."
    elif trend_name == TrendRegime.NO_TREND.name:
        tf_verdict = SuitabilityVerdict.AVOID
        tf_score = 0.1
        tf_rationale = "No trend detected, avoid trend strategies."

    compatibilities["trend_following_core"] = StrategyRegimeCompatibility(
        strategy_family="trend_following_core",
        verdict=tf_verdict,
        suitability_score=tf_score,
        rationale=tf_rationale,
    )

    # 2. Mean Reversion Strategy Family
    mr_verdict = SuitabilityVerdict.CAUTION
    mr_score = 0.5
    mr_rationale = "Neutral environment for mean reversion."
    if (
        trend_name == TrendRegime.NO_TREND.name
        or vol_name == VolatilityRegime.LOW_ENERGY.name
    ):
        mr_verdict = SuitabilityVerdict.ALLOW
        mr_score = 0.7
        mr_rationale = "Range-bound or low energy market favors mean reversion."
    elif trend_name in [
        TrendRegime.STRONG_UPTREND.name,
        TrendRegime.STRONG_DOWNTREND.name,
    ]:
        mr_verdict = SuitabilityVerdict.AVOID
        mr_score = 0.2
        mr_rationale = "Strong trend makes mean reversion dangerous."

    compatibilities["mean_reversion_core"] = StrategyRegimeCompatibility(
        strategy_family="mean_reversion_core",
        verdict=mr_verdict,
        suitability_score=mr_score,
        rationale=mr_rationale,
    )

    return RegimeSuitabilityMap(
        timestamp=context.timestamp,
        symbol=context.symbol,
        interval=context.interval,
        compatibilities=compatibilities,
    )
