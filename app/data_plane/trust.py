from .models import DataTrustVerdict


class TrustEngine:
    def evaluate(self, inputs: dict) -> DataTrustVerdict:
        pass
