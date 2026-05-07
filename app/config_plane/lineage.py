from app.config_plane.models import ConfigLineageRecord


class LineageTracker:
    def get_lineage(self, parameter_name: str) -> ConfigLineageRecord:
        return ConfigLineageRecord(
            parameter_name=parameter_name,
            value="mock",
            source_chain=[],
            override_chain=[],
            review_refs=[],
        )
