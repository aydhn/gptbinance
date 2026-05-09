import pytest
from app.experiment_plane.registry import CanonicalExperimentRegistry
from app.experiment_plane.models import ExperimentDefinition, ExperimentObjective, ExperimentArm, ExposureAllocationPlan, ExperimentBaseline
from app.experiment_plane.enums import ExperimentClass, ObjectiveClass, ArmClass, BaselineClass
from app.experiment_plane.exceptions import InvalidExperimentDefinitionError

def test_experiment_registry_success():
    registry = CanonicalExperimentRegistry()
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
    registry.register(experiment)
    assert registry.get("exp_1") is not None
    assert len(registry.list_all()) == 1

def test_experiment_registry_missing_arm():
    registry = CanonicalExperimentRegistry()
    experiment = ExperimentDefinition(
        experiment_id="exp_2",
        experiment_class=ExperimentClass.STRATEGY_VARIANT,
        objective=ExperimentObjective(
            objective_class=ObjectiveClass.OUTPERFORM_BASELINE,
            description="Test outperformance",
            target_metrics=["return"],
            non_goals=[]
        ),
        arms=[],
        baseline=ExperimentBaseline(
            baseline_id="base_1",
            baseline_class=BaselineClass.STATIC,
            description="Static baseline"
        ),
        exposure_plan=ExposureAllocationPlan(plan_id="plan_1", split_ratios={"arm_1": 1.0}),
        stopping_rules=[]
    )
    with pytest.raises(InvalidExperimentDefinitionError):
        registry.register(experiment)
