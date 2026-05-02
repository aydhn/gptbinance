from app.qualification.traceability import (
    build_traceability_matrix,
    get_uncovered_requirements,
)


def test_traceability_matrix():
    matrix = build_traceability_matrix()
    assert len(matrix) > 0
    # Assuming REQ-001 is mapped
    assert any(e.req_id == "REQ-001" and e.is_covered for e in matrix)


def test_uncovered_requirements():
    uncovered = get_uncovered_requirements()
    # In our mock, all are covered
    assert len(uncovered) == 0
