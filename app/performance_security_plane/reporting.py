class ReportingManager:
    def generate_summary(self, registry) -> dict:
        return {
            "total_securities": len(registry.list_securities()),
            "status": "active"
        }
