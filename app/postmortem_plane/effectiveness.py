from app.postmortem_plane.models import ActionVerificationRecord
from app.postmortem_plane.enums import EffectivenessClass

class EffectivenessEvaluator:
    @staticmethod
    def evaluate(record: ActionVerificationRecord) -> EffectivenessClass:
        return record.effectiveness if record.effectiveness else EffectivenessClass.PARTIAL_MITIGATION_ONLY
