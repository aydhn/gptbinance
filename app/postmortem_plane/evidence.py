from typing import Dict, Any

class PostmortemEvidence:
    @staticmethod
    def get_bundles(context: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "adversarial_refs": context.get("adversarial_refs", [])
        }
