from app.cost_plane.security import SecurityLinkage
def test_security_linkage():
    linkage = SecurityLinkage()
    assert linkage.evaluate_hardening_overhead()["security_tool_cost"] == 500
