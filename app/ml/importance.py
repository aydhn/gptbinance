from app.ml.models import FeatureImportanceSummary


class ImportanceAnalyzer:
    def analyze(self, run_id: str, model, data, target) -> FeatureImportanceSummary:
        return FeatureImportanceSummary(
            run_id=run_id, importance_map={"f1": 0.6, "f2": 0.4}, stable=True
        )
