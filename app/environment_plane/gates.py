from app.environment_plane.models import PromotionGateRecord

def evaluate_gate(gate_name: str, passed: bool, lineage_refs: str) -> PromotionGateRecord:
    return PromotionGateRecord(gate_name=gate_name, passed=passed, lineage_refs=lineage_refs)
