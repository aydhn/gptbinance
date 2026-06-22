from typing import Dict, Any
from app.settlement_plane.models import InstructionRecord
from app.settlement_plane.enums import InstructionClass

class InstructionEvaluator:
    def evaluate(self, context: Dict[str, Any]) -> InstructionRecord:
        has_instruction = context.get("has_instruction", False)
        is_stale = context.get("is_stale", False)
        is_duplicate = context.get("is_duplicate", False)

        if not has_instruction:
            return InstructionRecord(
                id="inst_none",
                instruction_class=InstructionClass.PARTIAL_INSTRUCTION,
                details="Missing instruction",
                lineage_refs=[]
            )

        if is_stale:
            return InstructionRecord(
                id="inst_stale",
                instruction_class=InstructionClass.STALE_INSTRUCTION,
                details="Stale instruction",
                lineage_refs=[]
            )

        if is_duplicate:
            return InstructionRecord(
                id="inst_dup",
                instruction_class=InstructionClass.DUPLICATE_INSTRUCTION,
                details="Duplicate instruction",
                lineage_refs=[]
            )

        return InstructionRecord(
            id="inst_valid",
            instruction_class=InstructionClass.VALID_INSTRUCTION,
            details="Valid instruction",
            lineage_refs=[]
        )
