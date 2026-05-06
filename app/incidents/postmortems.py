def generate_postmortem_seed(incident_id: str, severity: str, scopes: list):
    return {
        "incident_id": incident_id,
        "severity": severity,
        "affected_scopes": scopes,
        "status": "pending_postmortem"
    }
