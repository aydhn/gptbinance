from app.workflow_plane.jobs import JobRegistry
from app.workflow_plane.models import JobContract
from app.workflow_plane.enums import JobClass

def test_job_registry():
    reg = JobRegistry()
    job = JobContract(job_id="j1", job_class=JobClass.DATA_REFRESH, description="desc", is_idempotent=True, mutability_class="read", recoverability_class="auto", required_trust_inputs=[])
    reg.register(job)
    assert reg.get("j1").description == "desc"
