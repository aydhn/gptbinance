class ContractConsumer:
    def evaluate_federated_consumer(self, has_federation_refs: bool) -> str:
        if not has_federation_refs:
            return "caution: hidden federated consumer"
        return "trusted"
