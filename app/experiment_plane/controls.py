from app.experiment_plane.models import ExperimentControl


def build_true_control(control_id: str, desc: str) -> ExperimentControl:
    return ExperimentControl(
        control_id=control_id,
        description=desc,
        is_true_control=True,
        contamination_checked=True,
    )
