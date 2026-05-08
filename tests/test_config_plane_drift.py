from app.config_plane.drift import detect_drift
from app.config_plane.resolution import resolution_engine
from app.config_plane.models import ConfigScope
from app.config_plane.enums import ScopeClass


def test_drift_detection():
    manifest = resolution_engine.resolve(
        "test", ConfigScope(scope_class=ScopeClass.GLOBAL), []
    )
    runtime_dict = {"risk.max_daily_loss_pct": 5.0}  # Drifted value
    findings = detect_drift(manifest, runtime_dict)
    assert len(findings) == 1
    assert findings[0].actual_value == 5.0
