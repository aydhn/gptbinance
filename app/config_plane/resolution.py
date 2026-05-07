from typing import Dict
from datetime import datetime, timezone
import hashlib
import json
from app.config_plane.models import (
    EffectiveConfigManifest,
    EffectiveConfigEntry,
    ConfigScope,
)


class ResolutionEngine:
    def resolve(
        self,
        manifest_id: str,
        scope: ConfigScope,
        entries: Dict[str, EffectiveConfigEntry],
    ) -> EffectiveConfigManifest:
        config_hash = hashlib.sha256(
            json.dumps(
                {k: v.resolved_value for k, v in entries.items()}, sort_keys=True
            ).encode()
        ).hexdigest()
        return EffectiveConfigManifest(
            manifest_id=manifest_id,
            created_at=datetime.now(timezone.utc),
            scope=scope,
            entries=entries,
            config_hash=config_hash,
            unresolved_blockers=[],
        )
