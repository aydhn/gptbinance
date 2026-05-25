from app.settlement_plane.breach import evaluate_breach
from app.settlement_plane.models import BreachOfSettlementRecord

def test_evaluate_breach_material():
    breach = BreachOfSettlementRecord(id="B1", settlement_id="S1", breach_type="material")
    res = evaluate_breach(breach)
    assert res["status"] == "material_breach"

def test_evaluate_breach_technical():
    breach = BreachOfSettlementRecord(id="B2", settlement_id="S1", breach_type="technical")
    res = evaluate_breach(breach)
    assert res["status"] == "technical_breach"
