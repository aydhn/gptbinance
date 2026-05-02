from app.automation.models import (
    WorkflowDefinition,
    WorkflowStep,
    WorkflowType,
    JobSchedule,
)
from app.automation.enums import ScheduleType


# Pre-defined workflow templates or factories can go here.
def create_nightly_research_workflow(id: str) -> WorkflowDefinition:
    return WorkflowDefinition(
        id=id,
        type=WorkflowType.NIGHTLY_RESEARCH_REFRESH,
        name="Nightly Research Refresh",
        schedule=JobSchedule(type=ScheduleType.FIXED_TIME, expression="daily@03:00"),
        steps=[
            WorkflowStep(
                id="step_data", job_id="job_data_refresh_nightly", dependencies=[]
            ),
            WorkflowStep(
                id="step_feature",
                job_id="job_feature_refresh_nightly",
                dependencies=["step_data"],
            ),
            WorkflowStep(
                id="step_analytics",
                job_id="job_analytics_summary_nightly",
                dependencies=["step_feature"],
            ),
        ],
    )

def create_pre_upgrade_workflow(workflow_id: str) -> WorkflowDefinition:
    return WorkflowDefinition(id=workflow_id, name="Pre-Upgrade Checks", type=WorkflowType.NIGHTLY_RESEARCH_REFRESH, steps=[])

def create_post_restore_readiness_workflow(workflow_id: str) -> WorkflowDefinition:
    return WorkflowDefinition(id=workflow_id, name="Post-Restore Readiness", type=WorkflowType.NIGHTLY_RESEARCH_REFRESH, steps=[])

def create_weekly_release_hygiene_workflow(workflow_id: str) -> WorkflowDefinition:
    return WorkflowDefinition(id=workflow_id, name="Weekly Release Hygiene", type=WorkflowType.NIGHTLY_RESEARCH_REFRESH, steps=[])
