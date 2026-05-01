from datetime import datetime, timezone
from app.automation.windows import evaluate_quiet_hours, evaluate_maintenance_policy
from app.automation.models import QuietHoursPolicy, MaintenanceAwarePolicy
from app.automation.enums import QuietHoursVerdict, MaintenanceAction


def test_evaluate_quiet_hours():
    policy = QuietHoursPolicy(
        enabled=True, start_hour=22, end_hour=6, defer_until_end=True
    )

    # Inside quiet hours
    dt1 = datetime(2023, 1, 1, 23, 30, tzinfo=timezone.utc)
    assert evaluate_quiet_hours(policy, dt1) == QuietHoursVerdict.DEFER

    # Outside quiet hours
    dt2 = datetime(2023, 1, 1, 10, 0, tzinfo=timezone.utc)
    assert evaluate_quiet_hours(policy, dt2) == QuietHoursVerdict.ALLOW


def test_evaluate_maintenance():
    policy = MaintenanceAwarePolicy(
        allow_during_maintenance=False, defer_during_maintenance=True
    )

    assert evaluate_maintenance_policy(policy, True) == MaintenanceAction.DEFER
    assert evaluate_maintenance_policy(policy, False) == MaintenanceAction.ALLOW

    policy2 = MaintenanceAwarePolicy(
        allow_during_maintenance=False, defer_during_maintenance=False
    )
    assert evaluate_maintenance_policy(policy2, True) == MaintenanceAction.BLOCK
