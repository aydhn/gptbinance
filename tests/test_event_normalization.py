
from datetime import datetime, timezone
from app.events.normalization import DefaultEventNormalizer
from app.events.enums import EventSeverity


def test_default_normalizer():
    normalizer = DefaultEventNormalizer()
    raw = [
        {
            "id": "1",
            "title": "US NFP",
            "importance": "High",
            "time": datetime.now(timezone.utc).isoformat(),
        }
    ]
    normalized = normalizer.normalize(raw)
    assert len(normalized) == 1
    assert normalized[0].severity == EventSeverity.HIGH
