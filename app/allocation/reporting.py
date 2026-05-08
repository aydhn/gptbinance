from app.allocation.models import AllocationManifest


class ReportingEngine:
    def generate_summary(self, manifest: AllocationManifest) -> str:
        report = f"Allocation Manifest: {manifest.manifest_id}\\n"
        report += f"Gross Exposure: {manifest.portfolio_gross_exposure}\\n"
        report += f"Net Exposure: {manifest.portfolio_net_exposure}\\n"
        report += f"Trust Verdict: {manifest.trust_verdict.value}\\n"
        for i in manifest.intents:
            report += f" - {i.symbol} [{i.sleeve_ref}]: {i.verdict.value} (Size: {i.clipped_size})\\n"
        return report
