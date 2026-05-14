def check_continuity_capacity_readiness():
    pass



# Cost plane evaluation integration
def alert_unfunded_standby(costed_standby_posture: bool):
    if not costed_standby_posture:
        return "caution"
    return "ready"
