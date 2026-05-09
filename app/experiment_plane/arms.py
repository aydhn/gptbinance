from app.experiment_plane.models import ExperimentArm
from app.experiment_plane.enums import ArmClass


def build_candidate_arm(arm_id: str, desc: str) -> ExperimentArm:
    return ExperimentArm(arm_id=arm_id, arm_class=ArmClass.CANDIDATE, description=desc)


def build_baseline_arm(arm_id: str, desc: str) -> ExperimentArm:
    return ExperimentArm(arm_id=arm_id, arm_class=ArmClass.BASELINE, description=desc)


def build_control_arm(arm_id: str, desc: str) -> ExperimentArm:
    return ExperimentArm(arm_id=arm_id, arm_class=ArmClass.CONTROL, description=desc)
