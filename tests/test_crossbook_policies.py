def test_policy_manager():
    from app.crossbook.policies import CrossBookPolicyManager

    pm1 = CrossBookPolicyManager(profile="paper_default")
    assert pm1.get_max_combined_exposure() == 100000.0

    pm2 = CrossBookPolicyManager(profile="canary_live_caution")
    assert pm2.get_max_combined_exposure() == 50000.0
