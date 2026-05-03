from typing import List
from app.knowledge.models import (
    KnowledgeCatalogEntry,
    FreshnessReport,
    OperatorReadinessRecord,
    KnowledgeSearchResult,
    Runbook,
    SopDocument,
    Playbook,
    LessonLearned,
)


class KnowledgeReporter:
    @staticmethod
    def format_catalog_summary(entries: List[KnowledgeCatalogEntry]) -> str:
        lines = ["=== KNOWLEDGE CATALOG ==="]
        for e in entries:
            lines.append(f"[{e.item_type.value.upper()}] {e.item_id} | {e.title}")
            lines.append(
                f"   Status: {e.status.value} | Freshness: {e.freshness_severity.value}"
            )
        return "\n".join(lines)

    @staticmethod
    def format_freshness_report(reports: List[FreshnessReport]) -> str:
        lines = ["=== FRESHNESS REPORT ==="]
        for r in reports:
            lines.append(
                f"Item: {r.item_id} | Severity: {r.severity.value} | Days since review: {r.days_since_review}"
            )
            if r.warnings:
                for w in r.warnings:
                    lines.append(f"   ! {w.reason}")
        return "\n".join(lines)

    @staticmethod
    def format_readiness(record: OperatorReadinessRecord) -> str:
        lines = [f"=== OPERATOR READINESS: {record.operator_id} ({record.role}) ==="]
        lines.append(f"Level: {record.readiness_level.value}")
        lines.append(f"Quizzes Passed: {len(record.completed_quizzes)}")
        if record.stale_readiness_reasons:
            lines.append("Advisories:")
            for reason in record.stale_readiness_reasons:
                lines.append(f"  - {reason}")
        return "\n".join(lines)

    @staticmethod
    def format_search_results(results: List[KnowledgeSearchResult]) -> str:
        lines = ["=== SEARCH RESULTS ==="]
        for r in results:
            warn = (
                " [STALE WARNING]" if r.freshness.value in ("stale", "critical") else ""
            )
            lines.append(f"[{r.score:.1f}] {r.item.title} ({r.item.item_id}){warn}")
            lines.append(f"    Reasons: {', '.join(r.match_reasons)}")
        return "\n".join(lines)

    @staticmethod
    def format_runbook(item: Runbook) -> str:
        lines = [f"=== RUNBOOK: {item.title} ({item.item_id}) ==="]
        lines.append(f"Description: {item.description}")
        lines.append(f"Owner: {item.owner.owner_id} ({item.owner.team})")
        lines.append("Investigation Steps:")
        for s in item.investigation_steps:
            lines.append(f"  - {s}")
        lines.append("Mitigation Steps:")
        for s in item.mitigation_steps:
            lines.append(f"  - {s}")
        return "\n".join(lines)

    @staticmethod
    def format_sop(item: SopDocument) -> str:
        lines = [f"=== SOP: {item.title} ({item.item_id}) ==="]
        lines.append(f"Description: {item.description}")
        lines.append("Steps:")
        for s in item.steps:
            lines.append(f"  - {s}")
        return "\n".join(lines)

    @staticmethod
    def format_playbook(item: Playbook) -> str:
        lines = [f"=== PLAYBOOK: {item.title} ({item.item_id}) ==="]
        lines.append(f"Description: {item.description}")
        lines.append("Triggers:")
        for s in item.trigger_conditions:
            lines.append(f"  - {s}")
        lines.append("Actions:")
        for s in item.response_actions:
            lines.append(f"  - {s}")
        return "\n".join(lines)

    @staticmethod
    def format_lesson(item: LessonLearned) -> str:
        lines = [f"=== LESSON: {item.title} ({item.item_id}) ==="]
        lines.append(f"Status: {item.lesson_status.value}")
        if item.source_incident_ref:
            lines.append(f"Incident Ref: {item.source_incident_ref}")
        lines.append("Findings:")
        for s in item.findings:
            lines.append(f"  - {s}")
        lines.append("Recommendations:")
        for s in item.recommendations:
            lines.append(f"  - {s}")
        return "\n".join(lines)
