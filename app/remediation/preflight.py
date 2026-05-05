from typing import Dict, Any
from app.remediation.models import RemediationPack
from app.remediation.validation import PackValidator


class PreflightEngine:
    def __init__(self):
        self.validator = PackValidator()
        self.active_incidents = []  # Mock

    def run_preflight(self, pack: RemediationPack) -> Dict[str, Any]:
        report = {
            "pack_id": pack.pack_id,
            "passed": False,
            "blockers": [],
            "warnings": [],
        }

        try:
            self.validator.validate(pack)
        except Exception as e:
            report["blockers"].append(str(e))

        if self.active_incidents:
            report["warnings"].append("Active incidents found. Proceed with caution.")

        if pack.recipe.safety_class.value == "venue_affecting":
            report["warnings"].append(
                "This is a venue-affecting remediation. Direct apply is blocked."
            )

        if not report["blockers"]:
            report["passed"] = True

        return report
