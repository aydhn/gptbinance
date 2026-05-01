from app.automation.models import (
    JobDefinition,
    JobRunContext,
    QuietHoursPolicy,
    MaintenanceAwarePolicy,
)
from app.automation.enums import JobType, TriggerType, PreconditionAction
from app.automation.preconditions import (
    evaluate_all_preconditions,
    aggregate_precondition_verdict,
    QuietHoursPrecondition,
    MaintenancePrecondition,
)


def test_quiet_hours_precondition():
    job = JobDefinition(
        id="job1",
        type=JobType.DATA_REFRESH,
        name="Test",
        quiet_hours=QuietHoursPolicy(
            enabled=True, start_hour=0, end_hour=23, defer_until_end=True
        ),  # Always quiet hours basically
    )
    ctx = JobRunContext(trigger_type=TriggerType.TIME, run_key="key")

    checks = evaluate_all_preconditions(job, ctx, [QuietHoursPrecondition()])
    verdict = aggregate_precondition_verdict(checks)
    assert verdict == PreconditionAction.DEFER


def test_maintenance_precondition():
    job = JobDefinition(
        id="job1",
        type=JobType.DATA_REFRESH,
        name="Test",
        maintenance_policy=MaintenanceAwarePolicy(
            allow_during_maintenance=False, defer_during_maintenance=True
        ),
    )
    ctx = JobRunContext(trigger_type=TriggerType.TIME, run_key="key")

    checks = evaluate_all_preconditions(
        job, ctx, [MaintenancePrecondition(is_maintenance_active=True)]
    )
    verdict = aggregate_precondition_verdict(checks)
    assert verdict == PreconditionAction.DEFER
