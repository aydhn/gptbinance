from app.stressrisk.enums import VulnerabilityType
from app.stressrisk.portfolio import PortfolioVulnerabilityAnalyzer


def test_portfolio_analyzer():
    analyzer = PortfolioVulnerabilityAnalyzer()
    vulns = analyzer.analyze({})
    assert len(vulns) == 1
    assert vulns[0].vulnerability_type == VulnerabilityType.CONCENTRATION
