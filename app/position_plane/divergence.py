# Relies on models and enums already defined
from app.position_plane.reconciliation import ReconciliationEngine


class DivergenceDetector:
    @staticmethod
    def detect(*args, **kwargs):
        return ReconciliationEngine.reconcile(*args, **kwargs)
