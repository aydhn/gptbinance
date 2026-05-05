from app.market_truth.base import SourceAdapterBase
from typing import Dict, Any


class BinanceOfficialRestAdapter(SourceAdapterBase):
    """
    Enforces no-scraping policy. Connects only to official Binance endpoints.
    """

    def fetch_snapshot(self) -> Dict[str, Any]:
        # Dummy implementation. Should call official REST API.
        return {"status": "ok", "source": "official_rest"}


class BinanceOfficialWebsocketAdapter(SourceAdapterBase):
    def fetch_snapshot(self) -> Dict[str, Any]:
        # WebSockets stream, but this provides a summarized health snapshot
        return {"status": "streaming", "source": "official_ws"}
