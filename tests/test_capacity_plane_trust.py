from app.capacity_plane.trust import evaluate_capacity_trust
from app.capacity_plane.enums import CapacityTrustVerdict
from app.capacity_plane.isolation import report_isolation_breach


def test_evaluate_trust():
    tv = evaluate_capacity_trust()
    # By default in isolated tests without breaches, it should be trusted
    # Actually wait, let's inject a breach
    report_isolation_breach(
        "live", "research_job", True, "Research hit live DB directly"
    )
    tv = evaluate_capacity_trust()
    assert tv.verdict == CapacityTrustVerdict.BLOCKED
    assert "Live isolation breached." in tv.blockers
