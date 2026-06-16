import pytest
from app.collateral_plane.trust import TrustedCollateralVerdictEngine
from app.collateral_plane.repository import CollateralRepository
from app.collateral_plane.enums import TrustVerdictType

def test_trusted_collateral_verdict():
    repo = CollateralRepository()
    engine = TrustedCollateralVerdictEngine(repo)

    # Clean scenario
    repo.set_mock_state("COL_001", hidden_lien=False, stale=False, fake_seg=False)
    verdict = engine.evaluate("COL_001")
    assert verdict.verdict == TrustVerdictType.TRUSTED
    assert len(verdict.cautions) == 0

    # Degraded scenario (stale valuation)
    repo.set_mock_state("COL_002", hidden_lien=False, stale=True, fake_seg=False)
    verdict2 = engine.evaluate("COL_002")
    assert verdict2.verdict == TrustVerdictType.DEGRADED
    assert not verdict2.valuation_sufficiency
    assert len(verdict2.cautions) > 0

    # Review Required scenario (fake segregation)
    repo.set_mock_state("COL_003", hidden_lien=False, stale=False, fake_seg=True)
    verdict3 = engine.evaluate("COL_003")
    assert verdict3.verdict == TrustVerdictType.REVIEW_REQUIRED
    assert not verdict3.asset_clarity
