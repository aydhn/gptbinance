from app.reliability.evidence import ReliabilityEvidenceBundleAssembly
from app.reliability.enums import ReliabilityDomain, ScorecardVerdict
from app.reliability.models import HealthScorecard


def test_evidence_bundle_packaging():
    scorecards = [
        HealthScorecard(
            scorecard_id="s1",
            domain=ReliabilityDomain.MARKET_TRUTH,
            verdict=ScorecardVerdict.HEALTHY,
        )
    ]
    metrics = {"test": 123}

    bundle = ReliabilityEvidenceBundleAssembly.assemble(metrics, scorecards)
    assert bundle.metrics["test"] == 123
    assert len(bundle.scorecards) == 1
