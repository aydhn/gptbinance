class ReliabilityDomains:
    @staticmethod
    def get_domains() -> list:
        return [
            "system_uptime",
            "market_data_freshness",
            "execution_latency",
            "performance_integrity",
        ]
