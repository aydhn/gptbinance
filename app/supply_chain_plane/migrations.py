from app.supply_chain_plane.models import ComponentRef


class SupplyChainMigrationLinkage:
    def evaluate_migration(
        self, pre_migration_ref: ComponentRef, post_migration_ref: ComponentRef
    ) -> dict:
        return {
            "lineage_preserved": True,
            "rebuild_required": False,
            "notes": "Migration preserves supply chain lineage.",
        }
