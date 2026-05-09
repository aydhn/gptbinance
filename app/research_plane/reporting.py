from app.research_plane.repository import ResearchRepository
from app.research_plane.trust import TrustVerdictEngine
from app.research_plane.readiness import ReadinessEvaluator
import json


class ResearchReporter:
    def __init__(self, repo: ResearchRepository):
        self.repo = repo

    def summary(self) -> str:
        items = self.repo.list_all()
        lines = ["=== Research Registry Summary ==="]
        for item in items:
            q = item.question.text if item.question else "No question"
            h = (
                item.hypotheses[0].claimed_effect
                if item.hypotheses
                else "No hypothesis"
            )
            lines.append(f"[{item.research_id}] {item.title}")
            lines.append(f"  Class: {item.research_class.name}")
            lines.append(f"  Q: {q}")
            lines.append(f"  H: {h}")
        return "\n".join(lines)

    def item_details(self, research_id: str) -> str:
        item = self.repo.get(research_id)
        if not item:
            return f"Item {research_id} not found."

        trust = TrustVerdictEngine().evaluate(item)
        readiness = ReadinessEvaluator().evaluate(item)

        lines = [
            f"=== Research Item: {item.research_id} ===",
            f"Title: {item.title}",
            f"Class: {item.research_class.name}",
            f"Trust: {trust.verdict.name} (Caveats: {len(trust.caveats)})",
            f"Readiness: {readiness.readiness_class.name} (Blockers: {len(readiness.blockers)})",
            "Observations: " + str(len(item.observations)),
            "Hypotheses: " + str(len(item.hypotheses)),
            "Evidence Bundles: " + str(len(item.evidence_bundles)),
            "Contradictions: " + str(len(item.contradictions)),
        ]
        return "\n".join(lines)
