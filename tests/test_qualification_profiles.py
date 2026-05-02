from app.qualification.profiles import get_profile_definition
from app.qualification.enums import QualificationProfile


def test_paper_ready_profile():
    prof = get_profile_definition(QualificationProfile.PAPER_READY)
    assert "paper_execution_suite" in prof.required_suites
    assert "critical" in prof.forbidden_unresolved_criticalities
    assert "stale_approval_deny" in prof.mandatory_negative_tests


def test_full_live_profile():
    prof = get_profile_definition(QualificationProfile.FULL_LIVE)
    assert "full_live_suite" in prof.required_suites
    assert "critical" in prof.forbidden_unresolved_criticalities
    assert "mainnet_chaos_block" in prof.mandatory_negative_tests
