from app.policy_plane.contexts import ContextBuilder

def get_canonical_context(env: str, stage: str):
    return ContextBuilder().with_environment(env).with_stage(stage).build()
