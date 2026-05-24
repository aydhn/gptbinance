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

# OBLIGATION PLANE INTEGRATION
def check_consumer_impact(consumer_impact_closed: bool, contractual_duty_open: bool) -> str:
    # consumer impact closed while contractual duty remains open explicit caution
    if consumer_impact_closed and contractual_duty_open:
        return "CAUTION: Consumer impact marked closed while contractual duty remains open."
    return "Consumer impact closure validated."
