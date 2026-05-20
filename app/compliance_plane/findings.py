def check_compliance_provenance(finding_id: str, provenance_gaps: bool) -> str:
    if provenance_gaps:
        return 'FINDING: regulated-field provenance gaps detected'
    return 'TRUSTED'
