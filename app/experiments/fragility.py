from app.experiments.enums import FragilityClass


class FragilityAnalyzer:
    def analyze(self, run_id: str, comparison_results: dict) -> dict:
        # Dummy fragility analysis
        return {
            "report_id": "frag_123",
            "run_id": run_id,
            "fragility_classes": [FragilityClass.LOW_SAMPLE.value],
            "overfit_suspicion": False,
            "sample_size_warning": True,
            "summary": "Improvement seen, but sample size warrants caution.",
        }
