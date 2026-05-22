from app.commitment_plane.registry import commitment_registry

class ReportingManager:
    @staticmethod
    def generate_registry_summary() -> dict:
        commitments = commitment_registry.list_commitments()
        return {
            "total_commitments": len(commitments),
            "details": "Summary reporting structure"
        }
