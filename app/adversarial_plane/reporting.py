from typing import Dict, Any, List

class ReportingEngine:
    @staticmethod
    def generate_summary(registry_data: Dict[str, Any]) -> str:
        lines = ["=== Adversarial Registry Summary ==="]
        lines.append(f"Total Objects: {registry_data.get('total_objects', 0)}")
        lines.append(f"Active Exploits: {registry_data.get('active_exploits', 0)}")
        lines.append(f"Metric Gaming Flags: {registry_data.get('gaming_flags', 0)}")
        return "\n".join(lines)
