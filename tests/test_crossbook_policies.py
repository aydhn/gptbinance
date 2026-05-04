from app.crossbook.policies import CrossBookPolicyManager

def test_crossbook_policies():
    manager = CrossBookPolicyManager()
    policy = manager.get_policy("default")
    assert policy["max_directional"] == 50000
