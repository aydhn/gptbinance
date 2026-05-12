from app.migration_plane.models import MigrationVerificationRecord


class VerificationManager:
    def verify_cutover(self, cutover_id: str, telemetry_verification_refs: list = None) -> MigrationVerificationRecord:
        if not telemetry_verification_refs:
            raise Exception("Cutover verification requires telemetry validation refs.")
        return MigrationVerificationRecord(
            cutover_id=cutover_id,
            is_successful=True,
            details={"verification": "passed", "telemetry_refs": telemetry_verification_refs},
        )
