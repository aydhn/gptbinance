from datetime import datetime
from app.research.regime.engine import RegimeEngine
from app.research.regime.models import RegimeFeatureBundle
from app.research.regime.enums import RegimeFamily


def test_regime_engine_eval():
    # Make sure we load evaluators
    import app.research.regime  # Trigger registry

    engine = RegimeEngine()
    bundle = RegimeFeatureBundle(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        features={
            "trend_sma_fast": 105.0,
            "trend_sma_slow": 100.0,
            "momentum_rsi": 65.0,
            "volatility_atr": 1.0,
            "volatility_bb_width": 1.0,
            "price_to_sma_dist": 0.01,
            "close": 100.0,
            "high": 101.0,
            "low": 99.0,
        },
    )

    ctx = engine.evaluate_bundle(bundle)
    assert RegimeFamily.TREND in ctx.evaluations
    assert RegimeFamily.VOLATILITY in ctx.evaluations
    assert "trend_following_core" in ctx.suitability.compatibilities
