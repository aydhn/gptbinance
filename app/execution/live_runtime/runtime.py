# Stub for active runtime summary
def get_runtime_posture(degraded_feed):
    if degraded_feed:
        return "DEGRADED"
    return "HEALTHY"
