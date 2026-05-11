import pytest
from app.policy_plane.subjects import create_human_operator, create_workflow_job
from app.policy_plane.enums import SubjectClass


def test_human_operator():
    subj = create_human_operator("human1")
    assert subj.subject_class == SubjectClass.HUMAN_OPERATOR


def test_workflow_job():
    subj = create_workflow_job("job1")
    assert subj.subject_class == SubjectClass.WORKFLOW_JOB
