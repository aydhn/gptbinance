import pytest
from app.settlement_plane.models import ReleaseRecord, ReleaseClass
from app.settlement_plane.exceptions import InvalidReleaseError, OverreleaseViolationError
from app.settlement_plane.releases import evaluate_release

def test_evaluate_release_valid():
    release = ReleaseRecord(
        id="R1", settlement_id="S1", release_class=ReleaseClass.FULL, scope="all_claims"
    )
    result = evaluate_release(release, ["all_claims"])
    assert result["status"] == "valid"
    assert result["release_id"] == "R1"

def test_evaluate_release_no_scope():
    release = ReleaseRecord(
        id="R2", settlement_id="S1", release_class=ReleaseClass.FULL, scope=""
    )
    with pytest.raises(InvalidReleaseError):
        evaluate_release(release, [])

def test_evaluate_release_overrelease():
    release = ReleaseRecord(
        id="R3", settlement_id="S1", release_class=ReleaseClass.FULL, scope="global", inflation_caution=True
    )
    with pytest.raises(OverreleaseViolationError):
        evaluate_release(release, ["specific_claim"])
