from app.policy_plane.invariants import create_environment_separation_invariant

def get_central_invariants():
    return [create_environment_separation_invariant("Env must be isolated", "Checked at startup")]
