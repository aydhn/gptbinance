from .models import NetExposureSnapshot, DirectionalExposure
from datetime import datetime, timezone

class NetExposureCalculator:
    def calculate(self) -> NetExposureSnapshot:
        return NetExposureSnapshot(
            timestamp=datetime.now(timezone.utc),
            assets={},
            directional=DirectionalExposure(
                total_long_usd=0.0,
                total_short_usd=0.0,
                net_directional_usd=0.0
            )
        )
