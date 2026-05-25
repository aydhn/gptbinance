# change verification liability


def verify_change_claims(change_id: str, rights_registry) -> str:
    if rights_registry.has_open_beneficiary_claims(change_id):
        return "explicit caution: verified change under open beneficiary claims"
    return "trusted"

# OBLIGATION PLANE INTEGRATION
def check_change_verification(verified_label: bool, unresolved_mandatory_duty: bool) -> str:
    # verified label under unresolved mandatory duty explicit caution
    if verified_label and unresolved_mandatory_duty:
        return "CAUTION: Change marked verified while mandatory duty remains unresolved."
    return "Change verification validated."

def verified_changes_closed_via_settlement():
    pass # Added for Phase 124