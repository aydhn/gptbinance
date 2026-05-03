from app.perf.storage import PerfStorage
from app.perf.repository import PerfRepository
from app.perf.models import HostQualificationReport
from app.perf.enums import HostClass, ReadinessVerdict
import shutil


def test_storage():
    s = PerfStorage("data/test_perf")
    repo = PerfRepository(s)
    report = HostQualificationReport(
        host_class=HostClass.LOCAL_AVERAGE,
        tested_workloads=[],
        readiness=ReadinessVerdict.READY,
        evidence_refs=[],
    )
    repo.save_qualification_report(report)
    loaded = repo.get_qualification_report(HostClass.LOCAL_AVERAGE.value)
    assert loaded is not None
    assert loaded.readiness == ReadinessVerdict.READY
    shutil.rmtree("data/test_perf", ignore_errors=True)
