from app.research_plane.models import ResearchItem


class QualityChecker:
    def check_quality(self, item: ResearchItem) -> dict:
        warnings = []
        if not item.contradictions:
            warnings.append("Missing contradiction surfaces.")
        if not item.hypotheses:
            warnings.append("Missing hypotheses.")
        elif not item.hypotheses[0].benchmark_expectation:
            warnings.append("Missing benchmark expectation.")

        quality_score = 100 - (len(warnings) * 20)
        return {"score": max(0, quality_score), "warnings": warnings}
