from typing import List, Tuple
from app.optimizer.models import TrialResult, TrialRankingRow, ObjectiveScore
from app.optimizer.enums import RankingVerdict, GuardSeverity, PruningVerdict


class Ranker:
    @staticmethod
    def _determine_verdict(
        rank: int, max_rank: int, total_score: float, guard_severity: GuardSeverity
    ) -> RankingVerdict:
        if guard_severity == GuardSeverity.FAIL or total_score < -100:
            return RankingVerdict.REJECTED
        if guard_severity == GuardSeverity.WARNING:
            return RankingVerdict.MARGINAL

        if rank <= max_rank // 4 and rank <= 10:
            return RankingVerdict.TOP_TIER
        elif rank <= max_rank // 2:
            return RankingVerdict.ACCEPTABLE
        else:
            return RankingVerdict.MARGINAL

    @staticmethod
    def rank_trials(
        trials: List[TrialResult], top_n: int = 10
    ) -> List[TrialRankingRow]:
        valid_trials = []
        for t in trials:
            if t.error_message:
                continue
            if not t.objective or not t.metrics:
                continue
            if t.guard_report and t.guard_report.pruning_verdict != PruningVerdict.KEEP:
                continue
            valid_trials.append(t)

        valid_trials.sort(
            key=lambda t: (
                t.objective.total_score,
                t.metrics.benchmark_relative_strength,
                -t.metrics.max_drawdown_pct,
                t.metrics.total_trades,
            ),
            reverse=True,
        )

        ranked_rows = []
        for i, t in enumerate(valid_trials):
            rank = i + 1
            guard_sev = GuardSeverity.INFO
            if t.guard_report:
                severity_map = {
                    GuardSeverity.FAIL: 4,
                    GuardSeverity.WARNING: 3,
                    GuardSeverity.CAUTION: 2,
                    GuardSeverity.INFO: 1,
                }
                max_sev_val = 1
                for w in t.guard_report.warnings:
                    if severity_map[w.severity] > max_sev_val:
                        max_sev_val = severity_map[w.severity]
                        guard_sev = w.severity

            verdict = Ranker._determine_verdict(
                rank, len(valid_trials), t.objective.total_score, guard_sev
            )

            row = TrialRankingRow(
                trial_id=t.trial_id,
                rank=rank,
                candidate_values=t.config.candidate.values,
                total_score=t.objective.total_score,
                expectancy=t.metrics.expectancy,
                total_trades=t.metrics.total_trades,
                max_drawdown_pct=t.metrics.max_drawdown_pct,
                guard_severity=guard_sev.value,
                verdict=verdict,
            )
            ranked_rows.append(row)

        return ranked_rows[:top_n]
