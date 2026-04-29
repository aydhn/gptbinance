import uuid
from typing import Optional


class ClientOrderIdGenerator:
    """
    Generates deterministic or unique client order IDs.
    Lineage format: {session_id}-{symbol}-{side}-{intent_id}-{uuid}
    """

    def __init__(self, session_id: str):
        self.session_id = session_id[:8]

    def generate(self, symbol: str, side: str, intent_id: str) -> str:
        uid = uuid.uuid4().hex[:8]
        # Ensure it fits typical exchange limits (Binance allows 36 chars)
        raw_id = f"{self.session_id}-{symbol}-{side[:1]}-{intent_id[:4]}-{uid}"
        return raw_id[:36]
