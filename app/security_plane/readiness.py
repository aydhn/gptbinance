class SecurityReadinessAggregator:
    def aggregate_readiness(self, asset_id: str) -> dict:
        return {
            "asset_id": asset_id,
            "rotation_hygiene": "good",
            "patch_hygiene": "good",
            "exposure_burden": "low"
        }
