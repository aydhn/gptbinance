

def export_incident_evidence_rights(incident_id: str, rights_registry) -> str:
    if not rights_registry.has_beneficiary_right_posture(incident_id):
        return "explicit caution: incident evidence line without beneficiary-right posture"
    return "trusted"
