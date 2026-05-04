from typing import List
from .models import BookPositionRef

class BooksNormalizer:
    """Normalizes spot, margin, futures books into a unified view."""
    def normalize(self, raw_books: dict) -> List[BookPositionRef]:
        # Minimal stub
        return []
