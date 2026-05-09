from app.experiment_plane.trust import StandardTrustEvaluator
from app.experiment_plane.models import ExperimentDefinition, ExperimentObjective, ExperimentArm, ExposureAllocationPlan, ExperimentBaseline, FairnessCheckResult, ExperimentDecisionRecord
from app.experiment_plane.enums import ExperimentClass, ObjectiveClass, ArmClass, BaselineClass, FairnessClass, StoppingClass, TrustVerdict

def test_trust_evaluator_fair():
    evaluator = StandardTrustEvaluator()
    experiment = ExperimentDefinition(
        experiment_id="exp_1",
        experiment_class=ExperimentClass.STRATEGY_VARIANT,
        objective=ExperimentObjective(
            objective_class=ObjectiveClass.OUTPERFORM_BASELINE,
            description="Test outperformance",
            target_metrics=["return"],
            non_goals=[]
        ),
        arms=[
            ExperimentArm(arm_id="arm_1", arm_class=ArmClass.CANDIDATE, description="Candidate arm")
        ],
        baseline=ExperimentBaseline(
            baseline_id="base_1",
            baseline_class=BaselineClass.STATIC,
            description="Static baseline"
        ),
        exposure_plan=ExposureAllocationPlan(plan_id="plan_1", split_ratios={"arm_1": 1.0}),
        stopping_rules=[]
    )
    fairness = FairnessCheckResult(fairness_class=FairnessClass.FAIR, severity="NONE", rationale="ok")
    decision = ExperimentDecisionRecord(decision_id="dec_1", stopping_class=StoppingClass.CONTINUE, rationale="ok")
    result = evaluator.evaluate(experiment, fairness, decision)
    assert result.verdict == TrustVerdict.TRUSTED

def test_trust_evaluator_caution():
    evaluator = StandardTrustEvaluator()
    experiment = ExperimentDefinition(
        experiment_id="exp_1",
        experiment_class=ExperimentClass.STRATEGY_VARIANT,
        objective=ExperimentObjective(
            objective_class=ObjectiveClass.OUTPERFORM_BASELINE,
            description="Test outperformance",
            target_metrics=["return"],
            non_goals=[]
        ),
        arms=[
            ExperimentArm(arm_id="arm_1", arm_class=ArmClass.CANDIDATE, description="Candidate arm")
        ],
        baseline=ExperimentBaseline(
            baseline_id="base_1",
            baseline_class=BaselineClass.STATIC,
            description="Static baseline"
        ),
        exposure_plan=ExposureAllocationPlan(plan_id="plan_1", split_ratios={"arm_1": 1.0}),
        stopping_rules=[]
    )
    fairness = FairnessCheckResult(fairness_class=FairnessClass.IMBALANCED_EXPOSURE, severity="HIGH", rationale="bad split")
    decision = ExperimentDecisionRecord(decision_id="dec_1", stopping_class=StoppingClass.CONTINUE, rationale="ok")
    result = evaluator.evaluate(experiment, fairness, decision)
    assert result.verdict == TrustVerdict.CAUTION
