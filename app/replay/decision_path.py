import logging
from typing import List

from app.replay.models import DecisionPathSnapshot

logger = logging.getLogger(__name__)


class DummyDecisionPathBuilder:
    def build_dummy_path(
        self, policy_proof_ref: str = None
    ) -> List[DecisionPathSnapshot]:
        from datetime import datetime, timezone

        now = datetime.now(timezone.utc)
        path = [
            DecisionPathSnapshot(
                stage="signal",
                timestamp=now,
                inputs={"price": 100},
                decision={"signal": "buy"},
                evidence_refs=["ref1"],
            ),
            DecisionPathSnapshot(
                stage="risk",
                timestamp=now,
                inputs={"signal": "buy"},
                decision={
                    "approved": True,
                    "crossbook_conflicts": ["fake_hedge_conflict"],
                },
                evidence_refs=["ref2"],
            ),
        ]

        if policy_proof_ref:
            path.append(
                DecisionPathSnapshot(
                    stage="policy_kernel",
                    timestamp=now,
                    inputs={},
                    decision={
                        "policy_verdict": "BLOCK",
                        "reason": "Hard block explanation",
                    },
                    evidence_refs=[policy_proof_ref],
                )
            )

        return path
