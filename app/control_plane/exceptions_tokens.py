from app.policy_plane.exceptions_tokens import issue_scoped_exception

def issue_token(policy_id: str, issuer: str, reason: str):
    return issue_scoped_exception(policy_id, issuer, reason, ttl_minutes=60, scope={})
