from app.policy_plane.storage import storage
from app.policy_plane.models import PolicyDefinition


class PolicyRepository:
    def save_policy(self, policy: PolicyDefinition):
        storage.save(f"policy_{policy.policy_id}", policy)

    def get_policy(self, policy_id: str) -> PolicyDefinition:
        return storage.load(f"policy_{policy_id}")
