# Stub for observability alerts integrating with decision quality
class DecisionQualityAlerts:
    def __init__(self, notifier):
        self.notifier = notifier

    def check_funnel_health(self, summary):
        # Implementation to check if funnel is degraded
        pass

    def check_block_clusters(self, block_reasons):
        # Implementation to check for block reason clusters
        pass
