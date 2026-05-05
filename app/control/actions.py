from app.activation.repository import activation_repo
from app.activation.intents import IntentCompiler
from app.activation.plans import RolloutPlanner

class ActivationControlActions:
    @staticmethod
    def request_activation_intent(board_decision: dict):
        compiler = IntentCompiler()
        intent = compiler.compile_intent(board_decision)
        activation_repo.save_intent(intent)

        planner = RolloutPlanner()
        plan = planner.build_plan(intent)
        activation_repo.save_plan(plan)
        return intent.intent_id

    @staticmethod
    def request_rollout_stage_transition(intent_id: str, next_stage: str):
        # Implementation to transition stages using StageManager
        pass

    @staticmethod
    def request_activation_halt(intent_id: str):
        # Request immediate halt
        pass

    @staticmethod
    def request_activation_revert_review(intent_id: str):
        # Request revert review
        pass
