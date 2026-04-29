from app.ops.repository import OpsRepository


class OpsReporter:
    def __init__(self, repository: OpsRepository):
        self.repository = repository

    def generate_readiness_summary(self, run_id: str) -> str:
        report = self.repository.get_readiness_report(run_id)
        if not report:
            return f"No readiness report found for run_id: {run_id}"
        return f"Readiness Report: {report.overall_verdict.value.upper()} at {report.timestamp}"

    def generate_incident_summary(self, run_id: str) -> str:
        incidents = self.repository.get_incidents(run_id)
        return f"Total Incidents: {len(incidents)}. Unresolved: {len([i for i in incidents if not i.resolved])}"

    def generate_recovery_summary(self, run_id: str) -> str:
        res = self.repository.get_recovery_result(run_id)
        if not res:
            return f"No recovery result found for run_id: {run_id}"
        return f"Recovery Verdict: {res.verdict.value.upper()}"
