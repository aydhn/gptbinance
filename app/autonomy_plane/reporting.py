from app.autonomy_plane.registry import registry

class AutonomyReporter:
    def generate_summary(self) -> str:
        objects = registry.list_all()
        return f"Autonomy Registry Summary: {len(objects)} objects"

reporter = AutonomyReporter()
