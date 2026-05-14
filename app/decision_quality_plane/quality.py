from app.decision_quality_plane.models import DecisionManifest

class DecisionQualityChecker:
    def check(self, manifest: DecisionManifest) -> dict:
        warnings = []
        if len(manifest.options) < 2:
            warnings.append("Missing options warning")
        if not manifest.assumptions:
            warnings.append("Hidden assumption warning")
        if manifest.evidence and all(not e.is_contradictory for e in manifest.evidence):
            warnings.append("One-sided evidence warning")
        if manifest.confidence and manifest.confidence.confidence_level.value == "very_high" and not manifest.evidence:
            warnings.append("Inflated confidence warning")
        if not manifest.premortems:
            warnings.append("Missing premortem warning")
        if manifest.outcome and not manifest.counterfactuals:
            warnings.append("Missing counterfactual warning")

        return {
            "verdict": "OK" if not warnings else "NEEDS_IMPROVEMENT",
            "warnings": warnings
        }
