def export_assurance_diagnostics(assurance_record) -> dict:
    return {
        "false_assurance": not bool(assurance_record.cases),
        "stale_evidence": assurance_record.expiry.is_expired if assurance_record.expiry else False,
        "caveat_suppression": len(assurance_record.caveats) > 0,
        "scope_laundering": not bool(assurance_record.certifications),
        "surveillance_theater": not bool(assurance_record.surveillance)
    }
