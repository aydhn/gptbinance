class MetricsEngine:
    def get_queue_backlog(self, items):
        return len(items)

    def get_sla_breaches(self, items, sla_rules):
        breaches = 0
        return breaches
