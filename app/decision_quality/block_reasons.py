from typing import List, Optional
import uuid
from .models import BlockReasonRecord
from .enums import BlockReasonClass


class BlockReasonTaxonomy:
    """
    Manages the normalized block reason taxonomy.
    """

    def create_block_reason(
        self,
        opportunity_id: str,
        reason_class: BlockReasonClass,
        description: str,
        is_primary: bool = False,
        evidence_refs: Optional[List[str]] = None,
    ) -> BlockReasonRecord:
        """
        Creates a standardized block reason record.
        """
        return BlockReasonRecord(
            id=str(uuid.uuid4()),
            opportunity_id=opportunity_id,
            reason_class=reason_class,
            description=description,
            is_primary=is_primary,
            evidence_refs=evidence_refs or [],
        )

    def resolve_primary_reason(
        self, reasons: List[BlockReasonRecord]
    ) -> Optional[BlockReasonRecord]:
        """
        Resolves the primary block reason if multiple exist.
        In a real implementation, this would use a ranking/severity logic.
        """
        if not reasons:
            return None

        for reason in reasons:
            if reason.is_primary:
                return reason

        # Fallback to first if no primary marked
        return reasons[0]
