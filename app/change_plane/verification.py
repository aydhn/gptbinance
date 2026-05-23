# change verification liability


def verify_change_claims(change_id: str, rights_registry) -> str:
    if rights_registry.has_open_beneficiary_claims(change_id):
        return "explicit caution: verified change under open beneficiary claims"
    return "trusted"
