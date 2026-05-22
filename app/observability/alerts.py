from typing import Dict, Any

class Alerts:
    @staticmethod
    def get_alert_families() -> List[str]:
        return [
            "material_exploit_surface_detected",
            "metric_gaming_detected",
            "review_evasion_detected"
        ]
