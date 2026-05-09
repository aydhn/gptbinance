from app.experiment_plane.stopping import StandardStoppingEvaluator
from app.experiment_plane.models import ExperimentDefinition, ExperimentObjective, ExperimentArm, ExposureAllocationPlan, ExperimentBaseline, StoppingRule
from app.experiment_plane.enums import ExperimentClass, ObjectiveClass, ArmClass, BaselineClass, StoppingClass

def test_stopping_evaluator_continue():
    evaluator = StandardStoppingEvaluator()
    experiment = ExperimentDefinition(
        experiment_id="exp_1",
        experiment_class=ExperimentClass.STRATEGY_VARIANT,
        objective=ExperimentObjective(
            objective_class=ObjectiveClass.OUTPERFORM_BASELINE,
            description="desc", target_metrics=[], non_goals=[]
        ),
        arms=[ExperimentArm(arm_id="arm_1", arm_class=ArmClass.CANDIDATE, description="desc")],
        baseline=ExperimentBaseline(baseline_id="base", baseline_class=BaselineClass.STATIC, description="desc"),
        exposure_plan=ExposureAllocationPlan(plan_id="p1", split_ratios={"arm_1": 1.0}),
        stopping_rules=[]
    )
    res = evaluator.evaluate(experiment)
    assert res.stopping_class == StoppingClass.CONTINUE
