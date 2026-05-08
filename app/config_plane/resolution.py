from typing import Dict, List, Any
import hashlib
import json
import uuid
from datetime import datetime, timezone

from app.config_plane.models import (
    EffectiveConfigManifest,
    EffectiveConfigEntry,
    ConfigSourceRecord,
    ConfigLineageRecord,
    ConfigParameterRef,
    ConfigScope,
)
from app.config_plane.schemas import registry as schema_registry
from app.config_plane.layers import layer_registry
from app.config_plane.precedence import sort_sources_by_precedence
from app.config_plane.scopes import is_scope_applicable
from app.config_plane.enums import SecretVisibility, ParameterClass
from app.config_plane.exceptions import ConfigResolutionError


class ResolutionEngine:
    def resolve(
        self,
        profile: str,
        target_scope: ConfigScope,
        active_sources: List[ConfigSourceRecord],
    ) -> EffectiveConfigManifest:
        # Filter sources that apply to the target scope
        applicable_sources = [
            s for s in active_sources if is_scope_applicable(s.scope, target_scope)
        ]

        # Sort from lowest priority (base) to highest (patch)
        sorted_sources = sort_sources_by_precedence(applicable_sources)

        entries: Dict[str, EffectiveConfigEntry] = {}

        # We also need to process schemas to find hidden defaults (where param has default, but not explicitly set in any source)
        for domain, schema in schema_registry.list_schemas().items():
            for param_name, param_def in schema.parameters.items():
                ref_key = f"{domain.value}.{param_name}"
                ref = ConfigParameterRef(domain=domain, name=param_name)

                # Determine value from sources
                final_val = None
                final_source_id = None
                final_layer_id = None
                source_chain = []

                for source in sorted_sources:
                    if ref_key in source.payload:
                        final_val = source.payload[ref_key]
                        final_source_id = source.source_id
                        final_layer_id = source.layer_id
                        source_chain.append(source.source_id)

                is_hidden_default = False

                if final_val is None:
                    if param_def.has_default:
                        final_val = param_def.default_value
                        is_hidden_default = True
                        final_source_id = "hidden_default"
                        final_layer_id = "hidden_default_layer"
                        source_chain.append("default")
                    elif param_def.type_name != "Optional":
                        raise ConfigResolutionError(
                            f"Missing required parameter: {ref_key}"
                        )

                # Redaction logic for EffectiveConfig (actual value is stored but marked for downstream redaction)
                is_secret = param_def.parameter_class == ParameterClass.SECRET_ADJACENT

                lineage = ConfigLineageRecord(
                    parameter_ref=ref,
                    effective_value=final_val if not is_secret else "REDACTED",
                    source_chain=source_chain,
                    override_chain=[],  # Expand this logic if using explicit overrides
                    is_hidden_default=is_hidden_default,
                    secret_redacted=is_secret,
                )

                entries[ref_key] = EffectiveConfigEntry(
                    parameter_ref=ref,
                    value=final_val,
                    source_id=final_source_id,
                    layer_id=final_layer_id,
                    lineage=lineage,
                )

        # Generate hash
        hasher = hashlib.sha256()
        # Sort keys to ensure consistent hash
        for k in sorted(entries.keys()):
            hasher.update(f"{k}:{entries[k].value}".encode("utf-8"))

        manifest = EffectiveConfigManifest(
            manifest_id=f"eff_{uuid.uuid4().hex[:8]}",
            profile=profile,
            entries=entries,
            config_hash=hasher.hexdigest(),
            resolved_at=datetime.now(timezone.utc),
        )
        return manifest


resolution_engine = ResolutionEngine()
