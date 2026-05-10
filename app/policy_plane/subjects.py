from app.policy_plane.models import PolicySubject
from app.policy_plane.enums import SubjectClass


class SubjectRegistry:
    pass


def create_human_operator(subject_id: str) -> PolicySubject:
    return PolicySubject(
        subject_class=SubjectClass.HUMAN_OPERATOR, subject_id=subject_id
    )


def create_workflow_job(subject_id: str) -> PolicySubject:
    return PolicySubject(subject_class=SubjectClass.WORKFLOW_JOB, subject_id=subject_id)
