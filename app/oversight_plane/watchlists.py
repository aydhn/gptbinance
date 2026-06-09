from app.oversight_plane.models import WatchlistRecord

_watchlists = {}

def add_to_watchlist(watchlist_id: str, target_id: str, watchlist_type: str = "targeted"):
    _watchlists[watchlist_id] = WatchlistRecord(watchlist_id=watchlist_id, target_id=target_id, watchlist_type=watchlist_type)
