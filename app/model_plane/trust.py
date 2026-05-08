class ModelTrustVerdict:
    def get_trusted_signal_posture(self, model_id: str) -> bool:
        # Abstained/degraded signals tie into allocation trust
        return True
