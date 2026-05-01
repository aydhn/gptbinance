from datetime import datetime
from app.automation.models import QuietHoursPolicy, MaintenanceAwarePolicy
from app.automation.enums import QuietHoursVerdict, MaintenanceAction


def evaluate_quiet_hours(policy: QuietHoursPolicy, dt: datetime) -> QuietHoursVerdict:
    if not policy.enabled:
        return QuietHoursVerdict.ALLOW

    hour = dt.hour

    # Handle wrap-around (e.g., 22 to 06)
    if policy.start_hour > policy.end_hour:
        if hour >= policy.start_hour or hour < policy.end_hour:
            return (
                QuietHoursVerdict.DEFER
                if policy.defer_until_end
                else QuietHoursVerdict.ALLOW
            )
    else:
        if policy.start_hour <= hour < policy.end_hour:
            return (
                QuietHoursVerdict.DEFER
                if policy.defer_until_end
                else QuietHoursVerdict.ALLOW
            )

    return QuietHoursVerdict.ALLOW


def evaluate_maintenance_policy(
    policy: MaintenanceAwarePolicy, is_maintenance_active: bool
) -> MaintenanceAction:
    if not is_maintenance_active:
        return MaintenanceAction.ALLOW

    if policy.allow_during_maintenance:
        return MaintenanceAction.ALLOW

    if policy.defer_during_maintenance:
        return MaintenanceAction.DEFER

    return MaintenanceAction.BLOCK
