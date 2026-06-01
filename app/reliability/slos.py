def check_assurance_slos(assurance_record) -> dict:
    return {
        "stale_certification_absence": not (assurance_record.expiry and assurance_record.expiry.is_expired),
        "contradiction_burial_absence": len(assurance_record.contradictions) == 0,
        "missed_surveillance_absence": bool(assurance_record.surveillance)
    }
