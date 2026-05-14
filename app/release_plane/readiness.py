from app.capacity_plane.releases import check_rollout_capacity_sufficiency

def check_release_readiness():
    cap = check_rollout_capacity_sufficiency(["live_workload"])
    return {"capacity_readiness": cap}
