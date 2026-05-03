from app.perf.admission import AdmissionController
from app.perf.enums import WorkloadType, HostClass


def test_admission_controller():
    cautions = AdmissionController.get_cautions(
        [WorkloadType.PAPER_RUNTIME_CYCLE, WorkloadType.ANALYTICS_BATCH],
        HostClass.LOCAL_MINIMAL,
    )
    assert len(cautions) > 0
