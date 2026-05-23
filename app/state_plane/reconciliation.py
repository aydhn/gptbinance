# state reconciliation liability


def check_state_reconciliation_rights(state_id: str, rights_registry) -> str:
    if rights_registry.is_holder_beneficiary_mismatched(state_id):
        return "explicit caution: state reconciled but right holder unresolved"
    return "trusted"
