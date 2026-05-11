from app.migration_plane.models import MigrationVersionPair
from app.migration_plane.exceptions import InvalidVersionPairError

class VersionManager:
    @staticmethod
    def validate_pair(pair: MigrationVersionPair) -> bool:
        if pair.source_version == pair.target_version:
            raise InvalidVersionPairError("Source and target versions cannot be the same")
        return True
