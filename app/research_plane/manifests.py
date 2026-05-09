from app.research_plane.models import ResearchItem, ResearchArtifactManifest
from app.research_plane.trust import TrustVerdictEngine
from app.research_plane.enums import ConfidenceClass


class ManifestBuilder:
    def build(self, item: ResearchItem) -> ResearchArtifactManifest:
        trust_engine = TrustVerdictEngine()
        trust_verdict = trust_engine.evaluate(item)

        q_refs = [item.question.question_id] if item.question else []
        obs_refs = [o.observation_id for o in item.observations]
        hyp_refs = [h.hypothesis_id for h in item.hypotheses]
        ev_refs = [b.bundle_id for b in item.evidence_bundles]
        cont_refs = [c.contradiction_id for c in item.contradictions]

        conf_class = (
            item.confidence.current_class
            if item.confidence
            else ConfidenceClass.SPECULATIVE
        )

        return ResearchArtifactManifest(
            manifest_id=f"manifest_{item.research_id}",
            research_id=item.research_id,
            question_refs=q_refs,
            observation_refs=obs_refs,
            hypothesis_refs=hyp_refs,
            evidence_refs=ev_refs,
            contradiction_refs=cont_refs,
            confidence_class=conf_class,
            trust_verdict=trust_verdict.verdict,
        )
