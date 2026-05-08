from typing import List, Dict, Optional
from datetime import datetime, timezone
import uuid
from app.config_plane.models import (
    ConfigOverride,
    ConfigParameterRef,
    ConfigSourceRecord,
)
from app.config_plane.enums import ConfigDomain


class OverrideEngine:
    def __init__(self):
        self._overrides: Dict[str, ConfigOverride] = {}

    def register_override(self, override: ConfigOverride):
        self._overrides[override.override_id] = override

    def get_overrides_for_param(
        self, domain: ConfigDomain, name: str
    ) -> List[ConfigOverride]:
        return [
            o
            for o in self._overrides.values()
            if o.parameter_ref.domain == domain and o.parameter_ref.name == name
        ]


override_engine = OverrideEngine()
