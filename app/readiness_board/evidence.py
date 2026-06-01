def get_readiness_bundle(assurance_record) -> dict:
    return {
        "assurance_trust": "high" if assurance_record.cases else "low",
        "claim_clarity": "clear" if assurance_record.cases else "unclear",
        "evidence_sufficiency": "sufficient" if any(c.is_complete for c in assurance_record.cases) else "insufficient",
        "attestation_integrity": "intact" if assurance_record.attestations else "missing",
        "surveillance_rigor": "strict" if assurance_record.surveillance else "lax",
        "caveat_visibility": "visible" if assurance_record.caveats else "none"
    }
