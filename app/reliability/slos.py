def check_assurance_slos(assurance_record) -> dict:
    return {
        "stale_certification_absence": not (assurance_record.expiry and assurance_record.expiry.is_expired),
        "contradiction_burial_absence": len(assurance_record.contradictions) == 0,
        "missed_surveillance_absence": bool(assurance_record.surveillance)
    }

ACCOUNTABILITY_SLOS = ['unresolved ownerless-critical-risk ceiling', 'symbolic-sanction absence', 'unresolved restitution absence', 'opaque-appeal absence', 'trusted accountability degraded ratio']


# Incentive Plane Reliability SLOs
INCENTIVE_SLOS = {
    "unresolved_material_gaming_ceiling": 0,
    "hidden_conflict_absence": True,
    "symbolic_penalty_absence": True,
    "missing_clawback_absence": True,
    "trusted_incentive_degraded_ratio": 0.05
}
