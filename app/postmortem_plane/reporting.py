from app.postmortem_plane.models import PostmortemDefinition
from app.postmortem_plane.trust import TrustedPostmortemEngine

class PostmortemReporter:
    @staticmethod
    def summarize(postmortem: PostmortemDefinition) -> str:
        engine = TrustedPostmortemEngine()
        trust = engine.evaluate_trust(postmortem)

        summary = f"=== POSTMORTEM {postmortem.postmortem_id} ===\n"
        summary += f"Class: {postmortem.postmortem_class.value}\n"
        if postmortem.source_incidents:
             summary += f"Incidents: {','.join(postmortem.source_incidents.incident_ids)}\n"
        summary += f"Root Causes: {len(postmortem.root_causes)}\n"
        summary += f"Corrective Actions: {len(postmortem.corrective_actions)}\n"
        summary += f"Preventive Actions: {len(postmortem.preventive_actions)}\n"
        summary += f"Trust Verdict: {trust.verdict.value}\n"
        return summary
