import pytest
from app.settlement_plane.models import ConsiderationRecord, ConsiderationClass
from app.settlement_plane.exceptions import InvalidConsiderationError
from app.settlement_plane.consideration import evaluate_consideration

def test_evaluate_consideration_valid():
    consideration = ConsiderationRecord(
        id="C1", settlement_id="S1", consideration_class=ConsiderationClass.MONETARY, value={"amount": 1000, "currency": "USD"}
    )
    result = evaluate_consideration(consideration)
    assert result["status"] == "valid"
    assert result["consideration_id"] == "C1"

def test_evaluate_consideration_insufficient():
    consideration = ConsiderationRecord(
        id="C2", settlement_id="S1", consideration_class=ConsiderationClass.INSUFFICIENT, value={"amount": 1, "currency": "USD"}
    )
    with pytest.raises(InvalidConsiderationError):
        evaluate_consideration(consideration)

def test_evaluate_consideration_no_value():
    consideration = ConsiderationRecord(
        id="C3", settlement_id="S1", consideration_class=ConsiderationClass.MONETARY, value={}
    )
    with pytest.raises(InvalidConsiderationError):
        evaluate_consideration(consideration)
