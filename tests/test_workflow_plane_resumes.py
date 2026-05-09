from app.workflow_plane.resumes import ResumeManager

def test_resume_manager():
    mgr = ResumeManager()
    rec = mgr.resume_run("run-1", "chk-1", "System restart")
    assert rec.checkpoint_ref == "chk-1"
