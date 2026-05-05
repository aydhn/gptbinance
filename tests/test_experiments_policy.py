from app.experiments.policy import ExperimentPolicyIntegration


def test_experiment_policy_integration():
    policy = ExperimentPolicyIntegration()
    assert policy.check_legality({"live_trading_enabled": True}) is False
    assert policy.check_legality({"risk_threshold": 0.5}) is True
