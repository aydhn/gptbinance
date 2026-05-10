class LedgerReconciliationReport:
    def __init__(self, report_id: str):
        self.report_id = report_id

class LedgerReconciler:
    def export_divergence(self, release_rollout_state: str, hotfixes: list):
        # Ledger divergence visible after release rollout/hotfix
        pass

    def export_release_linked_account_truth_diffs(self):
        # Exports differences in account truth tied to releases
        pass
