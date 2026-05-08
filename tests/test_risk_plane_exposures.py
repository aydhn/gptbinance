from app.risk_plane.exposures import calculate_risk_facing_exposure


def test_calculate_risk_facing_exposure():
    positions = [
        {"position_id": "p1", "notional": 1000.0},
        {"position_id": "p2", "notional": -500.0},
    ]
    # Without fake hedge masking allowed
    exposure = calculate_risk_facing_exposure(
        positions, fake_hedge_masking_allowed=False
    )
    assert exposure.gross_exposure == 1500.0
    assert exposure.net_exposure == 500.0
    assert exposure.hedge_adjusted_exposure == 1500.0  # Falls back to gross
    assert len(exposure.caveats) == 1

    # With fake hedge masking allowed
    exposure2 = calculate_risk_facing_exposure(
        positions, fake_hedge_masking_allowed=True
    )
    assert exposure2.hedge_adjusted_exposure == 500.0
    assert len(exposure2.caveats) == 0
