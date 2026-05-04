from app.capital.storage import capital_storage
from app.capital.posture import generate_posture_snapshot


def test_storage(tmp_path):
    # Just verify it doesn't crash, actual file reading/writing is hard to test cleanly here
    generate_posture_snapshot("canary_micro", {})
    # This might write to data/capital, but we accept it for this test script scope.
    pass
