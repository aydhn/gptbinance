from app.security.retention import RetentionManager

def test_retention():
    rm = RetentionManager()
    policies = rm.get_policies()
    assert len(policies) > 0
