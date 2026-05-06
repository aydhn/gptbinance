import uuid
from typing import List, Dict, Any
from app.reliability.enums import ReliabilityDomain, ScorecardVerdict, BurnSeverity
from app.reliability.models import HealthScorecard, BurnRateReport, ReadinessDecayRecord


class DomainHealthScorecardBuilder:
    @staticmethod
    def build(
        domain: ReliabilityDomain,
        burn_reports: List[BurnRateReport],
        decay_records: List[ReadinessDecayRecord],
        specific_blockers: List[str] = None,
    ) -> HealthScorecard:
        verdict = ScorecardVerdict.HEALTHY
        blockers = specific_blockers or []
        caveats = []
        evidence_refs = []

        # Analyze Burn Reports
        for br in burn_reports:
            evidence_refs.append(f"burn_report:{br.report_id}")
            if br.severity == BurnSeverity.FAST_BURN:
                verdict = ScorecardVerdict.BLOCKED
                blockers.append(f"Fast burn on budget {br.budget_id}")
            elif (
                br.severity == BurnSeverity.SLOW_BURN
                and verdict != ScorecardVerdict.BLOCKED
            ):
                verdict = ScorecardVerdict.DEGRADED
                caveats.append(f"Slow burn on budget {br.budget_id}")
            elif br.severity == BurnSeverity.NORMAL and verdict not in [
                ScorecardVerdict.BLOCKED,
                ScorecardVerdict.DEGRADED,
            ]:
                verdict = ScorecardVerdict.CAUTION

        # Analyze Decay Records
        total_decay_severity = sum(r.severity_score for r in decay_records)
        for dr in decay_records:
            evidence_refs.append(f"decay_record:{dr.record_id}")
            if dr.severity_score > 0.8:
                if verdict != ScorecardVerdict.BLOCKED:
                    verdict = ScorecardVerdict.DEGRADED
                caveats.append(f"High decay: {dr.description}")
            elif dr.severity_score > 0.4 and verdict not in [
                ScorecardVerdict.BLOCKED,
                ScorecardVerdict.DEGRADED,
            ]:
                verdict = ScorecardVerdict.CAUTION
                caveats.append(f"Moderate decay: {dr.description}")

        if total_decay_severity > 2.0:
            verdict = ScorecardVerdict.REVIEW_REQUIRED
            blockers.append("Accumulated readiness decay too high.")

        if blockers:
            verdict = ScorecardVerdict.BLOCKED

        return HealthScorecard(
            scorecard_id=f"score_{uuid.uuid4().hex[:8]}",
            domain=domain,
            verdict=verdict,
            blockers=blockers,
            caveats=caveats,
            evidence_refs=evidence_refs,
        )
