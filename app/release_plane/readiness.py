from app.capacity_plane.releases import check_rollout_capacity_sufficiency

def check_release_readiness():
    cap = check_rollout_capacity_sufficiency(["live_workload"])
    return {"capacity_readiness": cap}



# Cost plane evaluation integration
def get_economic_readiness(unit_economics_ok: bool, attribution_ok: bool):
    if not unit_economics_ok or not attribution_ok:
        return "caution"
    return "ready"
