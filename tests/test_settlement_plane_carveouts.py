import pytest
from app.settlement_plane.models import CarveOutRecord, CarveOutClass
from app.settlement_plane.exceptions import InvalidCarveOutError
from app.settlement_plane.carveouts import evaluate_carveout

def test_evaluate_carveout_valid():
    carveout = CarveOutRecord(
        id="CO1", settlement_id="S1", carveout_class=CarveOutClass.CLAIM, details="Claim 123 is not released"
    )
    result = evaluate_carveout(carveout)
    assert result["status"] == "valid"
    assert result["carveout_id"] == "CO1"

def test_evaluate_carveout_invalid():
    carveout = CarveOutRecord(
        id="CO2", settlement_id="S1", carveout_class=CarveOutClass.CLAIM, details=""
    )
    with pytest.raises(InvalidCarveOutError):
        evaluate_carveout(carveout)
