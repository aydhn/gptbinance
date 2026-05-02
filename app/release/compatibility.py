from app.release.models import CompatibilityReport, ReleaseManifest
from app.release.enums import CompatibilityVerdict
from app.release.versioning import VersionManager


class CompatibilityChecker:
    def __init__(self):
        self.version_manager = VersionManager()

    def check(self, target_release: ReleaseManifest) -> CompatibilityReport:
        current_version = self.version_manager.get_current_version()

        warnings = []
        migrations_required = []
        verdict = CompatibilityVerdict.COMPATIBLE

        if (
            current_version.config_schema_version
            != target_release.version.config_schema_version
        ):
            migrations_required.append("config")
            verdict = CompatibilityVerdict.MIGRATION_REQUIRED

        return CompatibilityReport(
            target_version=target_release.version.version,
            current_version=current_version.version,
            verdict=verdict,
            migrations_required=migrations_required,
            warnings=warnings,
        )
