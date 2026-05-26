import pytest
from app.recapitalization_plane.models import RecapitalizationObject, FundingRecord, ControlRightRecord, DilutionRecord
from app.recapitalization_plane.enums import RecapitalizationClass, FundingClass, DilutionClass, TrustVerdict
from app.recapitalization_plane.trust import evaluate_trust

def test_phantom_capital_blocks_trust():
    recap = RecapitalizationObject(
        recapitalization_id="R-001",
        recap_class=RecapitalizationClass.RESOLUTION_EXIT,
        owner="SYS",
        scope="GLOBAL",
        fundings=[FundingRecord(funding_id="F1", commitment_id="C1", amount_funded=0, status=FundingClass.UNFUNDED)],
        is_fully_effective=True
    )
    verdict = evaluate_trust(recap)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert verdict.phantom_capital_detected == True

def test_hidden_dilution_blocks_trust():
    recap = RecapitalizationObject(
        recapitalization_id="R-002",
        recap_class=RecapitalizationClass.RESOLUTION_EXIT,
        owner="SYS",
        scope="GLOBAL",
        dilutions=[DilutionRecord(dilution_id="D1", affected_class="COMMON", dilution_percentage=50.0, status=DilutionClass.HIDDEN)],
    )
    verdict = evaluate_trust(recap)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert verdict.hidden_dilution_detected == True
