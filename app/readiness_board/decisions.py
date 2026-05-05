from typing import Optional
from app.readiness_board.storage import ReadinessBoardStorage
import uuid
from app.readiness_board.models import (
    GoNoGoDecision,
    ReadinessDossier,
    ConditionalGoTerms,
)
from app.readiness_board.enums import BoardVerdict, DomainVerdict


class DecisionEngine:
    def __init__(self, storage: ReadinessBoardStorage):
        self.storage = storage

    def evaluate_dossier(self, dossier: ReadinessDossier) -> GoNoGoDecision:
        unresolved_conflicts = [c for c in dossier.conflicts if not c.resolved]
        if unresolved_conflicts:
            return self._create_decision(
                dossier.dossier_id,
                BoardVerdict.NEEDS_REVIEW,
                "Unresolved evidence contradictions present.",
            )

        blockers = []
        for domain, verdict in dossier.domain_verdicts.items():
            if verdict.verdict == DomainVerdict.BLOCK:
                blockers.append(f"Domain {domain.value} is blocked.")

        if blockers:
            return self._create_decision(
                dossier.dossier_id,
                BoardVerdict.NO_GO,
                f"Blocked: {', '.join(blockers)}",
            )

        # Placeholder logic for CONDITIONAL_GO based on caveats
        caveats = any(
            v.verdict == DomainVerdict.CAUTION for v in dossier.domain_verdicts.values()
        )
        if caveats:
            # Just an example
            from datetime import datetime, timezone, timedelta
            from app.readiness_board.enums import ConditionalScope

            terms = ConditionalGoTerms(
                scopes=[ConditionalScope.TIME_BOUND],
                expires_at=datetime.now(timezone.utc) + timedelta(days=1),
                conditions=["Monitor error rates closely"],
                monitoring_expectations=["Hourly checkins"],
            )
            return self._create_decision(
                dossier.dossier_id,
                BoardVerdict.CONDITIONAL_GO,
                "Cautionary evidence found, granting conditional go.",
                terms,
            )

        return self._create_decision(
            dossier.dossier_id, BoardVerdict.GO, "All domains passed."
        )

    def _create_decision(
        self,
        dossier_id: str,
        verdict: BoardVerdict,
        rationale: str,
        terms: Optional[ConditionalGoTerms] = None,
    ) -> GoNoGoDecision:
        decision = GoNoGoDecision(
            decision_id=f"dec_{uuid.uuid4().hex[:8]}",
            dossier_id=dossier_id,
            verdict=verdict,
            rationale=rationale,
            conditional_terms=terms,
        )
        self.storage.save_decision(decision)
        return decision
