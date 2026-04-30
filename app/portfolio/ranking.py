from typing import List, Dict, Any
from app.portfolio.models import PortfolioCandidate, PortfolioContext, OpportunityRank
from app.portfolio.base import BaseRankingModel
from app.portfolio.enums import RankingReason


class SimpleRankingModel(BaseRankingModel):
    def rank_candidates(
        self, candidates: List[PortfolioCandidate], context: PortfolioContext
    ) -> List[PortfolioCandidate]:
        """Rank candidates based on simple heuristics."""

        for idx, candidate in enumerate(candidates):
            score = 100.0
            penalty_breakdown = {}
            primary_reason = RankingReason.DEFAULT

            # Simple heuristic: Use some score from intent metadata if exists, else default
            intent_score = 0.0
            if hasattr(candidate.intent, "metadata") and candidate.intent.metadata:
                intent_score = candidate.intent.metadata.get("risk_score", 0.0)
                score += intent_score
                if intent_score > 80:
                    primary_reason = RankingReason.HIGH_QUALITY

            # Penalize if it has overlap
            if (
                candidate.overlap_report
                and candidate.overlap_report.overlap_severity_score > 0
            ):
                penalty = candidate.overlap_report.overlap_severity_score * 10
                score -= penalty
                penalty_breakdown["overlap"] = penalty
                if penalty > 20:
                    primary_reason = RankingReason.OVERLAP_PENALTY

            # Penalize if target symbol sleeve is already highly utilized
            sleeve = context.symbol_sleeves.get(candidate.intent.symbol)
            if sleeve and sleeve.budget_notional > 0:
                utilization = sleeve.used_notional / sleeve.budget_notional
                if utilization > 0.8:
                    penalty = 20.0
                    score -= penalty
                    penalty_breakdown["sleeve_utilization"] = penalty
                    if penalty > penalty_breakdown.get("overlap", 0):
                        primary_reason = RankingReason.CONCENTRATION_PENALTY

            candidate.rank = OpportunityRank(
                intent_id=str(idx),  # fallback if no intent_id
                score=score,
                primary_reason=primary_reason,
                penalty_breakdown=penalty_breakdown,
                rationale=f"Base 100 + {intent_score} risk score - penalties {sum(penalty_breakdown.values())}",
            )

        # Sort candidates descending by score
        candidates.sort(key=lambda x: x.rank.score if x.rank else 0.0, reverse=True)
        return candidates
