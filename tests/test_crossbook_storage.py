from app.crossbook.storage import CrossBookStorage

def test_crossbook_storage():
    storage = CrossBookStorage()
    storage.save({})
