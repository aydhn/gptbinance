# Stub for profile evidence
def verify_qualification(profile, evidence_bundle):
    if (
        profile == "canary_live_caution_ready"
        and evidence_bundle.overall_verdict == "BLOCK"
    ):
        return False
    return True
