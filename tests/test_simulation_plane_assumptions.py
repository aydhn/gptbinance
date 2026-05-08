from app.simulation_plane.assumptions import AssumptionEvaluator
from app.simulation_plane.manifests import ManifestBuilder


def test_assumptions_zero_latency():
    evaluator = AssumptionEvaluator()
    manifest = ManifestBuilder.build_default("test1")
    manifest.latency.decision_to_order_ms = 0
    caveats = evaluator.evaluate(manifest)
    assert any("Zero latency assumption" in c for c in caveats)
