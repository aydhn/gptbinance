from typing import List, Dict, Optional
from uuid import UUID


class SeparationOfDutiesChecker:
    def check_conflict(
        self, producer_id: UUID, reviewer_id: UUID, adjudicator_id: UUID = None
    ) -> bool:
        """
        Returns True if there is a SoD conflict.
        Producer cannot be reviewer or adjudicator.
        Reviewer cannot be adjudicator (usually).
        """
        if producer_id == reviewer_id:
            return True
        if adjudicator_id:
            if producer_id == adjudicator_id or reviewer_id == adjudicator_id:
                return True
        return False


sod_checker = SeparationOfDutiesChecker()
