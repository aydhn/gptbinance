class RolloutsIntegration:
    def evaluate_rollout(self):
        # rollout remediation snapshots, harmed cohort scope ve compensating actions taşısın
        pass


def verify_rollout_standing(rollout_id: str, rights_registry) -> str:
    if rights_registry.has_standing_buried(rollout_id):
        return "explicit anomaly: rollout fixed but beneficiary standing buried"
    return "trusted"
