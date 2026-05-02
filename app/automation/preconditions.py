from datetime import datetime, timezone
from typing import List

from app.automation.models import (
    JobDefinition,
    JobRunContext,
    GateCheckResult,
    PreconditionCheck,
)
from app.automation.enums import (
    PreconditionAction,
    QuietHoursVerdict,
    MaintenanceAction,
)
from app.automation.windows import evaluate_quiet_hours, evaluate_maintenance_policy
from app.automation.base import PreconditionCheckerBase


class QuietHoursPrecondition(PreconditionCheckerBase):
    def check(self, job_def: JobDefinition, context: JobRunContext) -> GateCheckResult:
        now = datetime.now(timezone.utc)
        verdict = evaluate_quiet_hours(job_def.quiet_hours, now)
        if verdict == QuietHoursVerdict.DEFER:
            return GateCheckResult(
                passed=False,
                rationale="In quiet hours",
                action=PreconditionAction.DEFER,
            )
        return GateCheckResult(
            passed=True, rationale="Not in quiet hours", action=PreconditionAction.ALLOW
        )


class MaintenancePrecondition(PreconditionCheckerBase):
    def __init__(self, is_maintenance_active: bool = False):
        self.is_maintenance_active = is_maintenance_active

    def check(self, job_def: JobDefinition, context: JobRunContext) -> GateCheckResult:
        action = evaluate_maintenance_policy(
            job_def.maintenance_policy, self.is_maintenance_active
        )
        if action == MaintenanceAction.DEFER:
            return GateCheckResult(
                passed=False,
                rationale="Maintenance active (defer)",
                action=PreconditionAction.DEFER,
            )
        elif action == MaintenanceAction.BLOCK:
            return GateCheckResult(
                passed=False,
                rationale="Maintenance active (block)",
                action=PreconditionAction.BLOCK,
            )
        return GateCheckResult(
            passed=True,
            rationale="Maintenance check passed",
            action=PreconditionAction.ALLOW,
        )


class IncidentPrecondition(PreconditionCheckerBase):
    def __init__(self, has_active_incident: bool = False):
        self.has_active_incident = has_active_incident

    def check(self, job_def: JobDefinition, context: JobRunContext) -> GateCheckResult:
        if self.has_active_incident and job_def.live_affecting:
            return GateCheckResult(
                passed=False,
                rationale="Active incident blocks live-affecting job",
                action=PreconditionAction.BLOCK,
            )
        return GateCheckResult(
            passed=True,
            rationale="Incident check passed",
            action=PreconditionAction.ALLOW,
        )


def evaluate_all_preconditions(
    job_def: JobDefinition,
    context: JobRunContext,
    checkers: List[PreconditionCheckerBase],
) -> List[PreconditionCheck]:
    results = []
    for checker in checkers:
        res = checker.check(job_def, context)
        results.append(PreconditionCheck(name=checker.__class__.__name__, result=res))
    return results


def aggregate_precondition_verdict(
    checks: List[PreconditionCheck],
) -> PreconditionAction:
    actions = [c.result.action for c in checks]

    if PreconditionAction.BLOCK in actions:
        return PreconditionAction.BLOCK
    if PreconditionAction.ESCALATE in actions:
        return PreconditionAction.ESCALATE
    if PreconditionAction.SKIP in actions:
        return PreconditionAction.SKIP
    if PreconditionAction.DEFER in actions:
        return PreconditionAction.DEFER

    return PreconditionAction.ALLOW


class AuthorizationPrecondition(PreconditionCheckerBase):
    def check(self, job_def: JobDefinition, context: JobRunContext) -> GateCheckResult:
        if getattr(job_def, "approval_required", False):
            auth_bundle = getattr(context, "authorization_bundle", None)
            if not auth_bundle or auth_bundle.verdict.value != "approved":
                return GateCheckResult(
                    passed=False,
                    rationale="Missing or denied authorization bundle for approval-required job",
                    action=PreconditionAction.BLOCK,
                )
        return GateCheckResult(
            passed=True,
            rationale="Authorization check passed or not required",
            action=PreconditionAction.ALLOW,
        )
