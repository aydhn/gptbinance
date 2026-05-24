# state reconciliation liability


def check_state_reconciliation_rights(state_id: str, rights_registry) -> str:
    if rights_registry.is_holder_beneficiary_mismatched(state_id):
        return "explicit caution: state reconciled but right holder unresolved"
    return "trusted"

# OBLIGATION PLANE INTEGRATION
def check_state_reconciliation(state_reconciled: bool, mandatory_downstream_duties_open: bool) -> str:
    # state reconciled but mandatory downstream duties open explicit caution
    if state_reconciled and mandatory_downstream_duties_open:
        return "CAUTION: State reconciled but mandatory downstream duties remain open."
    return "State reconciliation validated."
