def get_assurance_context(assurance_record) -> dict:
    return {
        "assurance_posture": "active" if assurance_record.cases else "insufficient",
        "active_caveats": len(assurance_record.caveats),
        "surveillance_status": "active" if assurance_record.surveillance else "lapsed",
        "expiry_exposure": assurance_record.expiry.is_expired if assurance_record.expiry else False,
        "contradiction_burden": len(assurance_record.contradictions)
    }

class ContextEnricherAccountability:
    @staticmethod
    def enrich(context: dict):
        context.update({'accountability_posture': 'ready', 'active_breaches': [], 'sanction_exposure': 'none', 'appeal_status': 'none', 'restitution_burden': 'none'})
        return context
