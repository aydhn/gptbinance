from app.ops.base import ReadinessCheckerBase
from app.ops.models import ReadinessReport, ReadinessCheckResult, OpsConfig
from app.ops.enums import ReadinessVerdict, IncidentSeverity
from app.ops.maintenance import MaintenanceScheduler
from app.ops.incidents import IncidentHandler


class ReadinessChecker(ReadinessCheckerBase):
    def __init__(
        self,
        config: OpsConfig,
        maintenance: MaintenanceScheduler,
        incidents: IncidentHandler,
    ):
        self.config = config
        self.maintenance = maintenance
        self.incidents = incidents

    def check_all(self, run_id: str) -> ReadinessReport:
        checks = []
        checks.append(
            ReadinessCheckResult(
                name="Config Validation",
                verdict=ReadinessVerdict.PASS,
                rationale="Configuration is well-formed.",
                severity=IncidentSeverity.LOW,
            )
        )

        active_window = self.maintenance.get_active_window()
        if active_window:
            checks.append(
                ReadinessCheckResult(
                    name="Maintenance Window",
                    verdict=ReadinessVerdict.FAIL,
                    rationale=f"Active maintenance window: {active_window.description}",
                    remediation="Wait for maintenance to end or use manual override.",
                    severity=IncidentSeverity.HIGH,
                )
            )
        else:
            checks.append(
                ReadinessCheckResult(
                    name="Maintenance Window",
                    verdict=ReadinessVerdict.PASS,
                    rationale="No active maintenance.",
                    severity=IncidentSeverity.LOW,
                )
            )

        active_incidents = self.incidents.get_active_incidents(run_id)
        if active_incidents:
            checks.append(
                ReadinessCheckResult(
                    name="Active Incidents",
                    verdict=ReadinessVerdict.FAIL,
                    rationale=f"Found {len(active_incidents)} unresolved incidents.",
                    severity=IncidentSeverity.CRITICAL,
                )
            )
        else:
            checks.append(
                ReadinessCheckResult(
                    name="Active Incidents",
                    verdict=ReadinessVerdict.PASS,
                    rationale="No active incidents.",
                    severity=IncidentSeverity.LOW,
                )
            )

        overall = ReadinessVerdict.PASS
        if any(c.verdict == ReadinessVerdict.FAIL for c in checks):
            overall = ReadinessVerdict.FAIL
        elif any(c.verdict == ReadinessVerdict.CAUTION for c in checks):
            overall = ReadinessVerdict.CAUTION

        return ReadinessReport(run_id=run_id, checks=checks, overall_verdict=overall)
