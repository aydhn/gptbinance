import pytest
from app.automation.models import WorkflowDefinition, WorkflowStep, WorkflowType
from app.automation.dependencies import get_execution_order, check_cycles
from app.automation.exceptions import DependencyError


def test_dependency_sorting():
    wf = WorkflowDefinition(
        id="wf1",
        type=WorkflowType.NIGHTLY_RESEARCH_REFRESH,
        name="Test WF",
        steps=[
            WorkflowStep(id="stepC", job_id="jobC", dependencies=["stepB"]),
            WorkflowStep(id="stepB", job_id="jobB", dependencies=["stepA"]),
            WorkflowStep(id="stepA", job_id="jobA", dependencies=[]),
        ],
    )

    order = get_execution_order(wf)
    assert order == ["stepA", "stepB", "stepC"]


def test_cycle_detection():
    wf = WorkflowDefinition(
        id="wf1",
        type=WorkflowType.NIGHTLY_RESEARCH_REFRESH,
        name="Test WF",
        steps=[
            WorkflowStep(id="stepA", job_id="jobA", dependencies=["stepB"]),
            WorkflowStep(id="stepB", job_id="jobB", dependencies=["stepC"]),
            WorkflowStep(id="stepC", job_id="jobC", dependencies=["stepA"]),
        ],
    )

    with pytest.raises(DependencyError):
        check_cycles(wf)
