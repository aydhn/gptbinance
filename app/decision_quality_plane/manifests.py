from app.decision_quality_plane.models import DecisionManifest, DecisionDefinition
from app.decision_quality_plane.enums import DecisionClass

class DecisionManifestBuilder:
    def build_empty(self, decision_id: str, owner: str, intent: str, dclass: DecisionClass) -> DecisionManifest:
        dec = DecisionDefinition(
            decision_id=decision_id,
            decision_class=dclass,
            owner=owner,
            intent=intent
        )
        return DecisionManifest(decision=dec)
