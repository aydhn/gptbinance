class ExperimentDefinition:
    def define_experiment(self, candidate_id: str, baseline_manifest_id: str, candidate_manifest_id: str):
        # Experiment arms carry allocation manifests, sleeve budgets
        # Allocation-contractless usage rejected
        pass

class ExecutionExperimentArm:
    def __init__(self, manifest_ref: str, routing_policy: str):
        self.manifest_ref = manifest_ref
        self.routing_policy = routing_policy
