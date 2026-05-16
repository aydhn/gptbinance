import json

class PortfolioReporter:
    @staticmethod
    def generate_summary(registry, commitments, wip_manager):
        summary = {
            "total_objects": len(registry.get_all()),
            "commitments": len(commitments.get_all()),
            "wip_records": len(wip_manager.get_all())
        }
        return json.dumps(summary, indent=2)
