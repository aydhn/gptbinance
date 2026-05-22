from typing import Dict, Any

class Capabilities:
    @staticmethod
    def get_capabilities() -> List[str]:
        return [
            "inspect_adversarial_manifest",
            "review_exploit_surfaces",
            "review_gaming_and_evasion_patterns"
        ]
