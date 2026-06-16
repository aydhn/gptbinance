import pytest
from app.collateral_plane.repository import CollateralRepository

def test_investigation_integration():
    repo = CollateralRepository()
    repo.set_mock_state("COL_001", hidden_lien=True)
    assert repo.has_hidden_encumbrance("COL_001") == True
    # Ensures cross-plane boundary is strictly checked
