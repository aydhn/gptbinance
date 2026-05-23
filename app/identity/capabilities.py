class IdentityCapabilities:
    CAPABILITIES = [
        "inspect_precedent_manifest",
        "review_cases_and_holdings",
        "review_rationales_and_factors",
        "review_analogies_and_distinctions",
        "review_conflicts_hierarchy_and_overrides"
    ]

# Precedent Plane Integration added

class IdentityCapability:
    def __init__(self):
        self.authority_capabilities = ['inspect_authority_manifest', 'review_mandates_and_rights', 'review_delegations_and_overrides', 'review_ratifications_and_legitimacy_gaps', 'review_quorum_and_sod']
