from app.postmortems.repository import PostmortemRepository


def test_repository():
    repo = PostmortemRepository()
    assert repo.get_by_id("PM-1") == {}
