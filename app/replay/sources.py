import logging
from typing import List, Dict, Any

from app.replay.models import ReplayConfig
from app.replay.exceptions import MissingReplaySource
from app.replay.base import ReplaySourceResolverBase


logger = logging.getLogger(__name__)


class DummyReplaySourceResolver(ReplaySourceResolverBase):
    def resolve_sources(self, config: ReplayConfig) -> List[Dict[str, Any]]:
        logger.info(f"Resolving sources for config scope: {config.scope}")
        if not config.sources:
            raise MissingReplaySource("No sources provided in config")

        resolved = []
        for src in config.sources:
            resolved.append(
                {
                    "source_type": src.source_type.value,
                    "ref_id": src.ref_id,
                    "data": {"mock": "data", "status": "resolved"},
                }
            )
        return resolved
