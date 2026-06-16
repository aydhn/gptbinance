class EvidenceGraphArtefacts:
    def get_insurance_families(self):
        return ['insurance_reports']
    def get_relations(self):
        return ['insured_under', 'triggered_under', 'reserved_by', 'paid_by', 'exhausted_under', 'contributed_by', 'diverged_insurance_from']
