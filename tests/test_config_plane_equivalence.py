from app.config_plane.equivalence import evaluate_equivalence
from app.config_plane.resolution import resolution_engine
from app.config_plane.sources import ConfigSourceFactory
from app.config_plane.models import ConfigScope
from app.config_plane.enums import ScopeClass, EquivalenceVerdict


def test_equivalence_clean():
    baseline = resolution_engine.resolve(
        "test", ConfigScope(scope_class=ScopeClass.GLOBAL), []
    )
    target = resolution_engine.resolve(
        "test", ConfigScope(scope_class=ScopeClass.GLOBAL), []
    )
    report = evaluate_equivalence(baseline, target)
    assert report.verdict == EquivalenceVerdict.CLEAN
    assert len(report.divergences) == 0


def test_equivalence_degraded():
    baseline = resolution_engine.resolve(
        "test", ConfigScope(scope_class=ScopeClass.GLOBAL), []
    )
    source = ConfigSourceFactory.create_source(
        layer_id="profile_defaults_1",
        scope=ConfigScope(scope_class=ScopeClass.GLOBAL),
        payload={"risk.max_daily_loss_pct": 3.0},
    )
    target = resolution_engine.resolve(
        "test", ConfigScope(scope_class=ScopeClass.GLOBAL), [source]
    )
    report = evaluate_equivalence(baseline, target)
    assert report.verdict == EquivalenceVerdict.DEGRADED
    assert "risk.max_daily_loss_pct" in report.divergences
