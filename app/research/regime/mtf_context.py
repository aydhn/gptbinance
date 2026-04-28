from typing import Dict
from app.research.regime.models import MultiTimeframeRegimeContext, RegimeContext
from app.research.regime.enums import RegimeFamily


def build_mtf_context(
    base_context: RegimeContext, higher_contexts: Dict[str, RegimeContext]
) -> MultiTimeframeRegimeContext:
    """
    Builds a MultiTimeframeRegimeContext without lookahead bias.
    Assuming the caller provides contexts appropriately aligned in time.
    """
    contexts = {base_context.interval: base_context}
    contexts.update(higher_contexts)

    warnings = []
    consistency_score = 1.0

    # Simple consistency check: e.g. base trend vs higher trend
    base_trend = base_context.evaluations.get(RegimeFamily.TREND)
    for interval, hc in higher_contexts.items():
        hc_trend = hc.evaluations.get(RegimeFamily.TREND)

        if base_trend and hc_trend:
            b_name = base_trend.label.name
            h_name = hc_trend.label.name

            if "UPTREND" in b_name and "DOWNTREND" in h_name:
                warnings.append(
                    f"Trend contradiction: Base({base_context.interval}) is Uptrend but Higher({interval}) is Downtrend."
                )
                consistency_score -= 0.3
            elif "DOWNTREND" in b_name and "UPTREND" in h_name:
                warnings.append(
                    f"Trend contradiction: Base({base_context.interval}) is Downtrend but Higher({interval}) is Uptrend."
                )
                consistency_score -= 0.3

    consistency_score = max(0.0, consistency_score)

    return MultiTimeframeRegimeContext(
        timestamp=base_context.timestamp,
        symbol=base_context.symbol,
        base_interval=base_context.interval,
        contexts=contexts,
        consistency_score=consistency_score,
        contradiction_warnings=warnings,
    )
