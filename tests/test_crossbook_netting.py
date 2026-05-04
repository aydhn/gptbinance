from app.crossbook.netting import NetExposureCalculator

def test_net_exposure_calculator():
    calc = NetExposureCalculator()
    snapshot = calc.calculate()
    assert snapshot.directional.total_long_usd == 0.0
