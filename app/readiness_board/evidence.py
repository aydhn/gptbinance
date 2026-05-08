class ReadinessEvidence:
    def add_allocation_reports(self, trust_report: dict, equivalence_report: dict):
        # Includes critical allocation integrity failures
        pass

class ExecutionEvidenceBundle:
    def __init__(self, trust_summary: str, filter_integrity: str):
        self.trust_summary = trust_summary
        self.filter_integrity = filter_integrity
        self.critical_failures = []
