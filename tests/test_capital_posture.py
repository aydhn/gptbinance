from app.capital.posture import generate_posture_snapshot
from app.capital.enums import CapitalPostureState


def test_generate_posture():
    usage = {"total_deployed": 20.0, "total_reserved": 5.0, "total_frozen": 0.0}
    snap = generate_posture_snapshot("canary_micro", usage)

    assert snap.active_tier_id == "canary_micro"
    assert snap.posture_state == CapitalPostureState.NORMAL
    assert snap.available_headroom == 25.0  # 50 - 20 - 5
