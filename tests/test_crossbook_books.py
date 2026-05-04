from app.crossbook.books import BooksNormalizer

def test_books_normalizer():
    normalizer = BooksNormalizer()
    assert normalizer.normalize({}) == []
