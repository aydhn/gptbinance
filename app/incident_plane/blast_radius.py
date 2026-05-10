from typing import Dict, Any

class IncidentBlastRadiusEngine:
    @staticmethod
    def calculate(planes: list, symbols: list) -> Dict[str, Any]:
        if not planes and not symbols:
            return {"status": "UNKNOWN", "caution": "Unknown blast radius!"}
        return {"planes": planes, "symbols": symbols}
