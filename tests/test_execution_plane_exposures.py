from app.execution_plane.exposures import ExposureDeltaEngine

def test_exposure_delta():
    delta = ExposureDeltaEngine.calculate_delta(fill_qty=1.5, price=10.0, side="buy")
    assert delta["qty_delta"] == 1.5
    assert delta["notional_delta"] == 15.0

    delta2 = ExposureDeltaEngine.calculate_delta(fill_qty=2.0, price=20.0, side="sell")
    assert delta2["qty_delta"] == -2.0
    assert delta2["notional_delta"] == -40.0
