# Secret-Adjacent Configurations

Parameters marked as `SECRET_ADJACENT` are handled carefully:
- Values are redacted in `EffectiveConfigManifest` outputs unless explicitly requested.
- Lineage tracks that an override occurred without revealing the value.
- Diff semantics hide actual changes and only report that a secret changed.
