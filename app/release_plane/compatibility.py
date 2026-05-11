from app.policy_plane.evaluations import PolicyEvaluationEngine
from app.policy_plane.subjects import create_release_candidate
from app.policy_plane.actions import create_execute_action
from app.policy_plane.resources import create_environment_resource
from app.policy_plane.contexts import ContextBuilder

def check_compatibility(candidate_id: str, target_env: str):
    engine = PolicyEvaluationEngine()
    subject = create_release_candidate(candidate_id)
    action = create_execute_action()
    resource = create_environment_resource(target_env)
    context = ContextBuilder().with_environment(target_env).build()
    return engine.evaluate(subject, action, resource, context)

class ReleaseCompatibilityMigrationRef:
    def cutover_status(self, shim_debt=None):
        pass
