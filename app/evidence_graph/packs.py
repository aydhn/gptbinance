class EvidencePacks:
    PACKS = [
        "precedent_integrity_pack",
        "case_holding_review_pack",
        "rationale_analogy_review_pack",
        "conflict_hierarchy_review_pack"
    ]

# Precedent Plane Integration added

class EvidencePack:
    def __init__(self):
        self.authority_packs = ['authority integrity pack', 'mandate/right review pack', 'delegation/override review pack', 'ratification/quorum review pack']
