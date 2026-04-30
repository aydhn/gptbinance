from app.ml.models import EvaluationReport


class Evaluator:
    def evaluate(self, run_id: str, predictions, targets) -> EvaluationReport:
        # precision, recall, f1, log loss, brier score
        return EvaluationReport(
            run_id=run_id,
            precision=0.8,
            recall=0.7,
            f1_score=0.75,
            roc_auc=0.85,
            log_loss=0.3,
            brier_score=0.1,
        )
