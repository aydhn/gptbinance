from app.experiment_plane.arms import build_candidate_arm, build_baseline_arm, build_control_arm
from app.experiment_plane.enums import ArmClass

def test_arms_builder():
    arm = build_candidate_arm("cand_1", "desc")
    assert arm.arm_class == ArmClass.CANDIDATE

    base = build_baseline_arm("base_1", "desc")
    assert base.arm_class == ArmClass.BASELINE

    control = build_control_arm("ctrl_1", "desc")
    assert control.arm_class == ArmClass.CONTROL
