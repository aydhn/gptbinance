from typing import List, Dict, Any
from app.knowledge.models import KnowledgeSearchResult
from app.knowledge.catalog import catalog_registry
from app.knowledge.freshness import freshness_engine


class KnowledgeSearchEngine:
    def search(
        self, query: str, context: Dict[str, Any] = None
    ) -> List[KnowledgeSearchResult]:
        results = []
        query_lower = query.lower()

        for item in catalog_registry.list_all():
            score = 0.0
            reasons = []

            if query_lower in item.title.lower():
                score += 5.0
                reasons.append("Title match")

            if query_lower in item.description.lower():
                score += 2.0
                reasons.append("Description match")

            # Context match bonus
            if context:
                for r in item.applicability_rules:
                    if (
                        context.get("action")
                        and r.target_actions
                        and context["action"] in r.target_actions
                    ):
                        score += 3.0
                        reasons.append("Context Action match")
                        break

            if score > 0:
                freshness = freshness_engine.evaluate(item).severity
                results.append(
                    KnowledgeSearchResult(
                        item=item,
                        score=score,
                        match_reasons=reasons,
                        freshness=freshness,
                    )
                )

        # Sort by score desc
        results.sort(key=lambda x: x.score, reverse=True)
        return results


search_engine = KnowledgeSearchEngine()
