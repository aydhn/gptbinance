from typing import Dict, List, Optional
from app.security_plane.models import SecurityBlastRadiusReport

class BlastRadiusCalculator:
    def calculate(self, asset_id: str) -> SecurityBlastRadiusReport:
        # Stub logic
        return SecurityBlastRadiusReport(
            report_id=f"br-{asset_id}",
            asset_scope=[asset_id]
        )
