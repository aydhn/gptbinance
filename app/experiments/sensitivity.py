from app.experiments.models import SensitivityScan
from typing import Any


class SensitivityAnalyzer:
    def create_scan(
        self, scan_id: str, parameter: str, values: list[Any]
    ) -> SensitivityScan:
        return SensitivityScan(
            scan_id=scan_id, target_parameter=parameter, sweep_values=values
        )
