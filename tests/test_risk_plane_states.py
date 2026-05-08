from app.risk_plane.states import CanonicalRiskStateBuilder
from app.risk_plane.enums import RiskDomain


def test_risk_state_builder():
    builder = CanonicalRiskStateBuilder()
    state = builder.build_risk_state(
        state_id="st_1",
        domain=RiskDomain.ACCOUNT,
        target_id="MAIN",
        authoritative=True,
        source_position_refs=["pos_1"],
        source_ledger_refs=["led_1"],
        source_market_truth_refs=["mt_1"],
    )
    assert state.state_id == "st_1"
    assert state.authoritative is True
    assert state.completeness_summary == "PARTIAL: "
