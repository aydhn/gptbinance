from app.release.models import ReleaseSummary, HostProbeReport, CompatibilityReport, UpgradePlan, RollbackPlan
import json

class ReleaseReporter:
    def format_summary(self, summary: ReleaseSummary) -> str:
        return json.dumps(summary.model_dump(), indent=2)

    def format_host_probe(self, report: HostProbeReport) -> str:
        return json.dumps(report.model_dump(), indent=2)

    def format_compatibility(self, report: CompatibilityReport) -> str:
        return json.dumps(report.model_dump(), indent=2)

    def format_upgrade_plan(self, plan: UpgradePlan) -> str:
        return json.dumps(plan.model_dump(), indent=2)

    def format_rollback_plan(self, plan: RollbackPlan) -> str:
        return json.dumps(plan.model_dump(), indent=2)
