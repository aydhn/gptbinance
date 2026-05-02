from app.qualification.storage import QualificationStorage
from app.qualification.models import QualificationRun, QualificationConfig
from app.qualification.enums import QualificationProfile


def test_storage():
    storage = QualificationStorage()
    run = QualificationRun(
        run_id="test-run-storage",
        profile=QualificationProfile.PAPER_READY,
        config=QualificationConfig(),
    )
    storage.save_run(run)

    loaded = storage.get_run("test-run-storage")
    assert loaded is not None
    assert loaded.run_id == "test-run-storage"
    assert loaded.profile == QualificationProfile.PAPER_READY
