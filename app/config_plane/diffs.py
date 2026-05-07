from app.config_plane.models import ConfigDiffRecord, EffectiveConfigManifest
from app.config_plane.enums import DiffSeverity


class ConfigDiffEngine:
    def compare(
        self, left: EffectiveConfigManifest, right: EffectiveConfigManifest
    ) -> list[ConfigDiffRecord]:
        diffs = []
        for key in set(left.entries.keys()).union(right.entries.keys()):
            lv = left.entries.get(key).resolved_value if key in left.entries else None
            rv = right.entries.get(key).resolved_value if key in right.entries else None
            if lv != rv:
                diffs.append(
                    ConfigDiffRecord(
                        parameter_name=key,
                        left_value=lv,
                        right_value=rv,
                        semantic_class="value_change",
                        severity=DiffSeverity.MEDIUM,
                    )
                )
        return diffs
