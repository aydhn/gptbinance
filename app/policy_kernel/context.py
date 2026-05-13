from app.policy_plane.contexts import ContextBuilder

def get_canonical_context(env: str, stage: str, observability_trust: str = "TRUSTED"):
    return ContextBuilder().with_environment(env).with_stage(stage).with_key("observability_trust", observability_trust).build()

def get_security_context(env: str, stage: str, security_posture: str = "TRUSTED"):
    return ContextBuilder().with_environment(env).with_stage(stage).with_key("security_posture", security_posture).build()
