from app.experiments.models import ExperimentDefinition, ExperimentScope, ExperimentArm
from app.experiments.enums import ExperimentType, ScopeType, ArmType


class ExperimentDefinitionBuilder:
    def __init__(self):
        self.arms = []

    def add_baseline_arm(self, baseline_id: str):
        self.arms.append(
            ExperimentArm(
                arm_id="arm_baseline",
                arm_type=ArmType.BASELINE,
                reference_id=baseline_id,
            )
        )
        return self

    def add_candidate_arm(self, candidate_id: str, arm_id: str = "arm_candidate_1"):
        self.arms.append(
            ExperimentArm(
                arm_id=arm_id, arm_type=ArmType.CANDIDATE, reference_id=candidate_id
            )
        )
        return self

    def build(
        self, definition_id: str, hypothesis_id: str, metrics: list
    ) -> ExperimentDefinition:
        scope = ExperimentScope(
            scope_type=ScopeType.PROFILE,
            allowed_profiles=["testnet_1"],
            allowed_symbols=["BTCUSDT"],
            time_windows=[],
            forbidden_surfaces=["live_trade_allowed"],
        )
        return ExperimentDefinition(
            definition_id=definition_id,
            hypothesis_id=hypothesis_id,
            experiment_type=ExperimentType.BASELINE_COMPARISON,
            scope=scope,
            arms=self.arms,
            metrics=metrics,
        )
