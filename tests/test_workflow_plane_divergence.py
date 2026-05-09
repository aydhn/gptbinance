from app.workflow_plane.divergence import DivergenceEvaluator

def test_divergence_logging():
    evaluator = DivergenceEvaluator()
    report = evaluator.log_divergence("wf-1", "schedule_drift", "high", "Missed schedule by 10s")
    assert report.severity == "high"
    assert report.blast_radius == "isolated"
