from app.workspaces.profiles import ProfileRegistry
from app.workspaces.enums import ProfileType, ProfileSensitivity

def test_default_spec_for_type():
    spec = ProfileRegistry.get_default_spec_for_type(ProfileType.CANARY_LIVE_CAUTION)
    assert spec["sensitivity"] == ProfileSensitivity.HIGH
    assert spec["live_affecting"] is True

    spec_paper = ProfileRegistry.get_default_spec_for_type(ProfileType.PAPER_DEFAULT)
    assert spec_paper["sensitivity"] == ProfileSensitivity.LOW
    assert spec_paper["live_affecting"] is False
