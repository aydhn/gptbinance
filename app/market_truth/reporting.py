class MarketTruthReporter:
    def format_summary(self, evidence_bundle) -> str:
        if not evidence_bundle:
            return "No Market Truth Evidence found."

        lines = [f"Market Truth Summary for {evidence_bundle.symbol}"]
        lines.append(f"Overall Verdict: {evidence_bundle.overall_verdict.value}")
        for v in evidence_bundle.verdicts:
            lines.append(
                f" - {v.domain.value}: {v.truth_class.value} (Reasons: {', '.join(v.reasons)})"
            )
        return "\n".join(lines)
