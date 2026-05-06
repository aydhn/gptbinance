# Stub for promotion readiness
def is_ready_for_promotion(candidate_bundle, truthfulness_verdict):
    if truthfulness_verdict != "ALLOW":
        return False
    return True


# Exported rules to incident command: Block promotion on active critical incidents