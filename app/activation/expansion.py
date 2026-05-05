from app.activation.models import ExpansionDecision, ProbationStatus
from app.activation.enums import ProbationVerdict, ExpansionVerdict, ActivationStage


class ExpansionEvaluator:
    @staticmethod
    def evaluate(probation_status: ProbationStatus) -> ExpansionDecision:
        if probation_status.verdict == ProbationVerdict.PASS:
            return ExpansionDecision(
                intent_id=probation_status.intent_id,
                verdict=ExpansionVerdict.REQUIRES_APPROVAL,
                recommended_stage=ActivationStage.STAGE_1_LIMITED_SYMBOLS,  # Example next step
                blockers=[],
            )
        else:
            return ExpansionDecision(
                intent_id=probation_status.intent_id,
                verdict=ExpansionVerdict.BLOCKED,
                blockers=probation_status.blockers,
            )
