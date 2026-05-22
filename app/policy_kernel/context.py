from typing import Dict, Any

class PolicyContextModifier:
    @staticmethod
    def modify(context: Dict[str, Any], adversarial_inputs: Dict[str, Any]) -> Dict[str, Any]:
        context["adversarial_posture"] = adversarial_inputs.get("posture")
        context["active_exploit_surfaces"] = adversarial_inputs.get("surfaces")
        return context
