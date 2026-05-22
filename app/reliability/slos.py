from typing import Dict, Any

class ReliabilitySLOs:
    @staticmethod
    def evaluate(context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "low_cost_exploit_path_absence": context.get("low_cost_exploit_path_absence", True),
            "unresolved_material_suspicion_ceiling": context.get("unresolved_material_suspicion_ceiling", True)
        }
