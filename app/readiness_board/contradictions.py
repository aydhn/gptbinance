import uuid
from typing import List, Dict
from app.readiness_board.models import EvidenceConflict, ReadinessDomainVerdict
from app.readiness_board.enums import ContradictionClass, DomainVerdict, ReadinessDomain


class ContradictionDetector:
    def detect(
        self, domain_verdicts: Dict[ReadinessDomain, ReadinessDomainVerdict]
    ) -> List[EvidenceConflict]:
        conflicts = []

        # Example: Policy is blocked but Qualification is passed (mock qualification logic)
        policy = domain_verdicts.get(ReadinessDomain.POLICY)
        qual = domain_verdicts.get(ReadinessDomain.QUALIFICATION)

        if (
            policy
            and policy.verdict == DomainVerdict.BLOCK
            and qual
            and qual.verdict == DomainVerdict.PASS
        ):
            conflicts.append(
                EvidenceConflict(
                    conflict_id=f"conf_{uuid.uuid4().hex[:8]}",
                    contradiction_class=ContradictionClass.EXPERIMENT_VS_POLICY,
                    description="Policy is blocked but Qualification passed",
                    involved_domains=[
                        ReadinessDomain.POLICY,
                        ReadinessDomain.QUALIFICATION,
                    ],
                )
            )

        return conflicts
