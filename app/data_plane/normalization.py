class Normalizer:
    @staticmethod
    def normalize_symbol(symbol: str) -> str:
        return symbol.upper().replace("-", "").replace("/", "")

    @staticmethod
    def normalize_timezone(dt: "datetime") -> "datetime":
        from datetime import timezone

        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
