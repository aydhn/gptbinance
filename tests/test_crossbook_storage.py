def test_storage_and_repository():
    from app.crossbook.storage import CrossBookStorage
    from app.crossbook.repository import CrossBookRepository

    storage = CrossBookStorage()
    repo = CrossBookRepository(storage)

    storage.save_graph("g1", {"data": "test"})
    res = repo.get_latest_graph()
    assert res == {"data": "test"}
