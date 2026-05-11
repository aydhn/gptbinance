from app.policy_plane.obligations import create_must_wait_for_approval_obligation

def require_approval(reason: str):
    return create_must_wait_for_approval_obligation(reason)
