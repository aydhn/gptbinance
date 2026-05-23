class ConsumerImpact:
    def __init__(self):
        self.authority_plane_beneficiary_facing_authority = None
        self.signatory_authority = None
        self.mandate_refs = []
    def __init__(self):
        self.precedent_refs = []

# Precedent Plane Integration added


def check_contract_consumer_impact(impact_closure: dict, rights_registry) -> str:
    if not rights_registry.has_beneficiary_right_map(impact_closure):
        return "explicit caution: consumer impact closed without beneficiary right map"
    return "trusted"
