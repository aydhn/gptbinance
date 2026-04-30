from app.governance.models import RefreshSummary, PromotionCandidateReport


class GovernanceReporter:
    def generate_refresh_summary(self, summary: RefreshSummary) -> str:
        return f"Refresh {summary.run_id} completed. Status: {summary.status}. Components: {summary.components_refreshed}. New bundles: {summary.new_bundles}"

    def generate_promotion_report(self, report: PromotionCandidateReport) -> str:
        return f"Promotion Report for {report.bundle_id}: Readiness={report.readiness.value}. RecStage={report.stage_recommendation.value}. Blockers={report.blockers}"
