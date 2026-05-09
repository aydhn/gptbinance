from app.experiment_plane.models import ExperimentObjective
from app.experiment_plane.enums import ObjectiveClass


def build_outperform_objective(target: str) -> ExperimentObjective:
    return ExperimentObjective(
        objective_class=ObjectiveClass.OUTPERFORM_BASELINE,
        description="Outperform baseline on specified metrics.",
        target_metrics=[target],
        non_goals=["Increase latency", "Increase risk limit breaches"],
        proof_notes="Validated via comparative attribution.",
    )


def build_reduce_drag_objective() -> ExperimentObjective:
    return ExperimentObjective(
        objective_class=ObjectiveClass.REDUCE_EXECUTION_DRAG,
        description="Reduce execution friction and slippage.",
        target_metrics=["slippage", "partial_fill_rate"],
        non_goals=["Increase trading volume artificially"],
        proof_notes="Validated via execution plane metrics.",
    )


# Other builders can be added here
