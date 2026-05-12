class ModelTrust:
    def __init__(self):
        pass # stale calibration -> sim comparability


class ModelTrustEvaluator:
    def evaluate(self, model_id: str, corrective_actions: list, runtime_blind_spots: list = None) -> bool:
        if runtime_blind_spots:
            return False
        # if unverified action, degraded
        return True
