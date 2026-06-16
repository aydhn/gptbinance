class ReadinessEvidence:
    def get_insurance_metrics(self):
        return ['insurance_trust', 'policy_clarity', 'trigger_sufficiency', 'coverage_sufficiency', 'reserve_adequacy', 'payout_sufficiency']
    def check_blockers(self):
        return 'blocker/caution on critical insurance integrity failures'
