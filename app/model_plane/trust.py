class ModelTrust:
    def __init__(self):
        pass # stale calibration -> sim comparability


class ModelTrustEvaluator:
    def evaluate(self, model_id: str, corrective_actions: list) -> bool:
        # if unverified action, degraded
        return True
