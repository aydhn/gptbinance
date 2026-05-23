class ProvenanceActions:
    def record_precedent_action(self):
        pass

# Precedent Plane Integration added

class ProvenanceAction:
    def __init__(self):
        self.authority_ids = []
        self.mandate_creation_refs = []
        self.delegation_refs = []
        self.escalation_refs = []
        self.veto_refs = []
        self.override_refs = []
        self.ratification_refs = []
        self.authority_expiration_refs = []
