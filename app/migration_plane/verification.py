class MigrationVerificationIntegration:
    def evaluate_verification(self):
        # cutover defect remedy, rollback assist, data restoration ve notification remedy refs ile canonical hale gelsin
        pass


def verify_migration_portability(migration_id: str, rights_registry) -> str:
    if rights_registry.has_broken_portability_right(migration_id):
        return "trust lowered: migration complete claim under broken portability right"
    return "trusted"
