from app.shadow_state.windows import get_consistency_windows
from app.shadow_state.enums import ConsistencyWindow


def test_consistency_windows():
    windows = get_consistency_windows()
    assert ConsistencyWindow.SUBMIT_ACK_TOLERANCE in windows
