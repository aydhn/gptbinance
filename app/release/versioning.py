from app.release.models import ReleaseVersion, SchemaVersionSnapshot
from app.release.enums import ReleaseStage


class VersionManager:
    def get_current_version(self) -> ReleaseVersion:
        return ReleaseVersion(
            version="1.0.0",
            stage=ReleaseStage.PRODUCTION,
            build_fingerprint="dev",
            config_schema_version="v1",
            state_schema_version="v1",
            artifact_schema_version="v1",
        )

    def get_schema_snapshot(self) -> SchemaVersionSnapshot:
        return SchemaVersionSnapshot(
            config_schema_version="v1",
            state_schema_version="v1",
            artifact_schema_version="v1",
        )
