class ExperimentReporter:
    def generate_summary(self, bundle: dict) -> str:
        h_id = bundle.get("hypothesis_id")
        comp = bundle.get("comparison", {})
        frag = bundle.get("fragility", {})
        promo = bundle.get("promotion_recommendation")

        report = "=== EXPERIMENT REPORT ===\n"
        report += f"Hypothesis ID: {h_id}\n"
        report += f"Verdict: {comp.get('verdict')}\n"
        report += f"Confidence: {comp.get('confidence')}\n"
        report += f"Caveats: {', '.join(comp.get('caveats', []))}\n"
        report += f"Fragility Summary: {frag.get('summary')}\n"
        report += f"Promotion Candidate Status: {promo}\n"
        report += "==========================\n"

        return report
