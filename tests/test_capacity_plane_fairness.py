from app.capacity_plane.fairness import report_fairness, list_fairness_reports
from app.capacity_plane.enums import FairnessClass


def test_fairness_report():
    report_fairness(
        "live_queue",
        FairnessClass.DOMINATED,
        {"workload_A": 0.9, "workload_B": 0.1},
        ["workload_B is starved"],
    )
    reports = list_fairness_reports()
    assert len(reports) > 0
    assert reports[-1].fairness_class == FairnessClass.DOMINATED
