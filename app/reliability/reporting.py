from typing import List, Dict
from app.reliability.models import (
    DomainHealthSummary,
    ErrorBudget,
    BurnRateReport,
    ReadinessDecayRecord,
    FreezeRecommendation,
    HoldRecommendation,
    HealthScorecard,
    OperationalCadenceArtifact,
    ReliabilityTrendReport,
    SLODefinition,
)


class ReliabilityReporter:
    @staticmethod
    def format_summary(summary: DomainHealthSummary) -> str:
        out = [
            f"=== RELIABILITY SUMMARY ===",
            f"Overall Verdict: {summary.overall_verdict.value.upper()}",
        ]
        out.append("Scorecards:")
        for domain, sc in summary.scorecards.items():
            out.append(f"  - {domain}: {sc.verdict.value.upper()}")
            if sc.blockers:
                out.append(f"    Blockers: {', '.join(sc.blockers)}")
        return "\n".join(out)

    @staticmethod
    def format_slos(slos: List[SLODefinition]) -> str:
        out = ["=== SLO REGISTRY ==="]
        for slo in slos:
            out.append(
                f"[{slo.slo_class.value.upper()}] {slo.name} ({slo.domain.value})"
            )
            out.append(f"  Target: {slo.target.target_value} {slo.target.unit}")
        return "\n".join(out)

    @staticmethod
    def format_budgets(budgets: List[ErrorBudget]) -> str:
        out = ["=== ERROR BUDGETS ==="]
        for b in budgets:
            pct = (
                (b.remaining_budget / b.total_budget_value) * 100
                if b.total_budget_value > 0
                else 0
            )
            out.append(
                f"Budget {b.budget_id} ({b.budget_class.value}): {b.remaining_budget:.2f} / {b.total_budget_value:.2f} ({pct:.1f}% remaining)"
            )
        return "\n".join(out)

    @staticmethod
    def format_burn_rates(burns: List[BurnRateReport]) -> str:
        out = ["=== BURN RATES ==="]
        for b in burns:
            out.append(f"Budget {b.budget_id}: {b.severity.value.upper()}")
            out.append(f"  Short window burn: {b.short_window_burn_rate:.2%}")
            out.append(f"  Long window burn: {b.long_window_burn_rate:.2%}")
            if b.projected_exhaustion_hours:
                out.append(
                    f"  Projected exhaustion: {b.projected_exhaustion_hours:.1f} hours"
                )
            if b.caveats:
                out.append(f"  Caveats: {', '.join(b.caveats)}")
        return "\n".join(out)

    @staticmethod
    def format_decay(decays: List[ReadinessDecayRecord]) -> str:
        out = ["=== READINESS DECAY ==="]
        for d in decays:
            out.append(
                f"[{d.domain.value}] {d.decay_class.value}: {d.description} (Severity: {d.severity_score:.2f})"
            )
        return "\n".join(out)

    @staticmethod
    def format_scorecards(scorecards: List[HealthScorecard]) -> str:
        out = ["=== HEALTH SCORECARDS ==="]
        for s in scorecards:
            out.append(f"Domain: {s.domain.value} -> {s.verdict.value.upper()}")
            if s.blockers:
                out.append(f"  Blockers: {', '.join(s.blockers)}")
            if s.caveats:
                out.append(f"  Caveats: {', '.join(s.caveats)}")
            if s.evidence_refs:
                out.append(f"  Evidence: {', '.join(s.evidence_refs)}")
        return "\n".join(out)

    @staticmethod
    def format_freeze(freezes: List[FreezeRecommendation]) -> str:
        out = ["=== FREEZE RECOMMENDATIONS ==="]
        for f in freezes:
            out.append(f"[{f.freeze_class.value.upper()}] Scope: {f.scope}")
            out.append(f"  Rationale: {f.rationale}")
        return "\n".join(out)

    @staticmethod
    def format_holds(holds: List[HoldRecommendation]) -> str:
        out = ["=== OPERATIONAL HOLDS ==="]
        for h in holds:
            out.append(f"[{h.hold_class.value.upper()}] Scope: {h.scope}")
            out.append(f"  Rationale: {h.rationale}")
            out.append(f"  Expiry Conditions: {', '.join(h.expiry_conditions)}")
        return "\n".join(out)

    @staticmethod
    def format_trends(trends: List[ReliabilityTrendReport]) -> str:
        out = ["=== RELIABILITY TRENDS ==="]
        for t in trends:
            out.append(f"Domain: {t.domain.value} -> {t.trend_class.value.upper()}")
            if t.repeated_failure_families:
                out.append(
                    f"  Repeated Failures: {', '.join(t.repeated_failure_families)}"
                )
        return "\n".join(out)

    @staticmethod
    def format_cadence(cadences: List[OperationalCadenceArtifact]) -> str:
        out = ["=== OPERATIONAL CADENCE ARTIFACTS ==="]
        for c in cadences:
            out.append(f"Artifact: {c.artifact_id} ({c.artifact_type})")
            out.append(f"  Overall Verdict: {c.domain_summary.overall_verdict.value}")
            out.append(f"  Timestamp: {c.timestamp}")
        return "\n".join(out)
