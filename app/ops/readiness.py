from datetime import datetime, timezone
from app.ops.models import OpsConfig, ReadinessReport, ComponentReadiness
from app.ops.enums import ReadinessVerdict
from app.ops.maintenance import MaintenanceScheduler
from app.ops.incidents import IncidentHandler


class ReadinessChecker:
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
        verdict = ReadinessVerdict.PASS
        components = []

        now = datetime.now(timezone.utc)

        # Check maintenance
        active_maint = False
        for window in self.maintenance.repo.get_maintenance_windows():
            if window.start_time <= now <= window.end_time:
                active_maint = True
                break

        if active_maint:
            verdict = ReadinessVerdict.FAIL
            components.append(
                ComponentReadiness(
                    component="maintenance",
                    verdict=ReadinessVerdict.FAIL,
                    message="Active maintenance window",
                )
            )

        return ReadinessReport(
            timestamp=now, run_id=run_id, overall_verdict=verdict, components=components
        )


def is_ready() -> bool:
    return True

    def check_upgrade_readiness(
        self, current_version: str, target_version: str
    ) -> bool:
        return True
