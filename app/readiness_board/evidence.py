class ReadinessBundle:
    def __init__(self, bundle_id: str):
        self.bundle_id = bundle_id
        self.release_trust_summary = None
        self.bundle_completeness_summary = None
        self.rollout_readiness_summary = None
        self.canary_evidence_summary = None
        self.rollback_readiness_summary = None

    def check_integrity_failures(self):
        # Critical release integrity failures act as blockers/caution
        pass


class ReadinessEvidenceBuilder:
    def add_postmortem_debt(self, bundle: dict, debt_records: list):
        bundle['postmortem_debt'] = debt_records
