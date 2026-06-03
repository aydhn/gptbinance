class EvidenceArtefacts:
    pass

def register_resilience_artefact(artefact_id):
    return {"status": "registered", "relations": ["resilient_under", "degraded_by", "contained_by", "backed_by_reserve", "recovered_by", "exhausted_by", "diverged_resilience_from"]}
