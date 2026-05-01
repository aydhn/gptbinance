from datetime import datetime, timezone


def is_weekend(dt: datetime) -> bool:
    """Check if datetime is a weekend (Saturday=5, Sunday=6)."""
    return dt.weekday() >= 5


def get_local_now(tz_str: str = "UTC") -> datetime:
    # Minimal timezone handling, defaulting to UTC for simplicity unless pytz/zoneinfo is added
    return datetime.now(timezone.utc)
