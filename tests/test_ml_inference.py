from app.ml.inference import InferenceEngine
from app.ml.models import InferenceRequest
from app.ml.enums import InferenceVerdict
from datetime import datetime, timezone


def test_inference_engine():
    engine = InferenceEngine()
    req = InferenceRequest(
        run_id="run_1",
        features={"f1": 0.5},
        symbol="BTCUSDT",
        timestamp=datetime.now(timezone.utc),
    )

    res = engine.predict(req)
    assert res.run_id == "run_1"
    assert res.verdict == InferenceVerdict.PASS
