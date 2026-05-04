"""
books.py
"""
from typing import List, Dict, Any
from app.crossbook.models import BookPositionRef
from app.crossbook.enums import BookType, MarginMode


class BookAbstraction:
    def __init__(self, book_type: BookType):
        self.book_type = book_type
        self.positions: List[BookPositionRef] = []

    def get_positions(self) -> List[BookPositionRef]:
        return self.positions

    def load_snapshot(self, data: List[Dict[str, Any]]):
        pass


class SpotBook(BookAbstraction):
    def __init__(self):
        super().__init__(BookType.SPOT)

    def load_snapshot(self, data: List[Dict[str, Any]]):
        self.positions = []
        for d in data:
            self.positions.append(
                BookPositionRef(
                    book_type=self.book_type,
                    symbol=d.get("asset", ""),
                    asset=d.get("asset", ""),
                    quantity=d.get("free", 0.0) + d.get("locked", 0.0),
                    notional=d.get("notional", 0.0),
                    is_borrowed=False,
                    margin_mode=MarginMode.NONE,
                    metadata=d,
                )
            )


class MarginBook(BookAbstraction):
    def __init__(self):
        super().__init__(BookType.MARGIN)

    def load_snapshot(self, data: List[Dict[str, Any]]):
        self.positions = []
        for d in data:
            self.positions.append(
                BookPositionRef(
                    book_type=self.book_type,
                    symbol=d.get("asset", ""),
                    asset=d.get("asset", ""),
                    quantity=d.get("netAsset", 0.0),
                    notional=d.get("notional", 0.0),
                    is_borrowed=d.get("borrowed", 0.0) > 0,
                    margin_mode=MarginMode.CROSS,  # Defaulting to cross for mock
                    metadata=d,
                )
            )


class FuturesBook(BookAbstraction):
    def __init__(self):
        super().__init__(BookType.FUTURES)

    def load_snapshot(self, data: List[Dict[str, Any]]):
        self.positions = []
        for d in data:
            self.positions.append(
                BookPositionRef(
                    book_type=self.book_type,
                    symbol=d.get("symbol", ""),
                    asset=d.get("symbol", "").replace(
                        "USDT", ""
                    ),  # Naive asset extraction
                    quantity=d.get("positionAmt", 0.0),
                    notional=d.get("notional", 0.0),
                    is_borrowed=False,
                    margin_mode=MarginMode.CROSS,
                    metadata=d,
                )
            )
