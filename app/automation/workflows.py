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
