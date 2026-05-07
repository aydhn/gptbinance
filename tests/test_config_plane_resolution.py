from app.config_plane.resolution import resolution_engine
from app.config_plane.sources import ConfigSourceFactory
from app.config_plane.models import ConfigScope
from app.config_plane.enums import ScopeClass

def test_resolution_hidden_default():
    manifest = resolution_engine.resolve("test", ConfigScope(scope_class=ScopeClass.GLOBAL), [])
    entry = manifest.entries.get("risk.max_daily_loss_pct")
    assert entry is not None
    assert entry.value == 2.0
    assert entry.lineage.is_hidden_default == True

def test_resolution_with_override():
    source = ConfigSourceFactory.create_source(
        layer_id="profile_defaults_1",
        scope=ConfigScope(scope_class=ScopeClass.GLOBAL),
        payload={"risk.max_daily_loss_pct": 1.5}
    )
    manifest = resolution_engine.resolve("test", ConfigScope(scope_class=ScopeClass.GLOBAL), [source])
    entry = manifest.entries.get("risk.max_daily_loss_pct")
    assert entry.value == 1.5
    assert entry.lineage.is_hidden_default == False
