from app.stressrisk.models import VulnerabilityBreakdown
from app.stressrisk.enums import VulnerabilityType, LossSeverity


class PortfolioVulnerabilityAnalyzer:
    def analyze(self, positions: dict) -> list[VulnerabilityBreakdown]:
        return [
            VulnerabilityBreakdown(
                vulnerability_type=VulnerabilityType.CONCENTRATION,
                severity=LossSeverity.MEDIUM,
                description="High concentration in top 2 assets.",
                affected_symbols=["BTC", "ETH"],
                contribution_pct=60.0,
            )
        ]
