class ExperimentLinkage:
    @staticmethod
    def validate_experiment_graduation(proof_of_value: bool, capacity_reserved: bool) -> bool:
        # No endless experiment limbo
        return proof_of_value and capacity_reserved
