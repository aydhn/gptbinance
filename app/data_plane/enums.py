from enum import Enum, auto


class SourceClass(str, Enum):
    EXCHANGE_KLINES = "exchange_klines"
    EXCHANGE_TRADES = "exchange_trades"
    BEST_BID_ASK = "best_bid_ask"
    MARK_PRICE = "mark_price"
    INDEX_PRICE = "index_price"
    FUNDING_HISTORY = "funding_history"
    OPEN_INTEREST = "open_interest"
    INSTRUMENT_METADATA = "instrument_metadata"
    TRADING_RULES_FILTERS = "trading_rules_filters"
    EVENT_CALENDAR = "event_calendar"
    FEE_SCHEDULE = "fee_schedule"
    INTERNAL_RUNTIME_OBSERVATION = "internal_runtime_observation"
    REPLAY_DATASET_SOURCE = "replay_dataset_source"


class FieldClass(str, Enum):
    NUMERIC = "numeric"
    STRING = "string"
    CATEGORICAL = "categorical"
    TIMESTAMP = "timestamp"


class DatasetClass(str, Enum):
    RAW = "raw"
    NORMALIZED = "normalized"
    REPLAY = "replay"
    OFFLINE = "offline"


class TimeSemantic(str, Enum):
    EVENT_TIME = "event_time"
    PUBLISH_TIME = "publish_time"
    AVAILABLE_AT_TIME = "available_at_time"
    INGEST_TIME = "ingest_time"
    PROCESSED_TIME = "processed_time"
    AS_OF = "as_of"


class RevisionClass(str, Enum):
    RESTATEMENT = "restatement"
    LATE_ARRIVAL = "late_arrival"


class GapClass(str, Enum):
    MISSING_BAR = "missing_bar"
    MISSING_TRADE_SPAN = "missing_trade_span"
    MISSING_FUNDING_POST = "missing_funding_post"
    MISSING_RULE_SNAPSHOT = "missing_rule_snapshot"


class AnomalyClass(str, Enum):
    DUPLICATE_PACKET = "duplicate_packet"
    OUT_OF_ORDER_UPDATE = "out_of_order_update"
    TIMESTAMP_SKEW = "timestamp_skew"
    NEGATIVE_INVALID_VALUE = "negative_invalid_value"
    IMPOSSIBLE_PRICE_JUMP = "impossible_price_jump"
    UNIT_MISMATCH = "unit_mismatch"
    STALE_SNAPSHOT = "stale_snapshot"


class ConsensusClass(str, Enum):
    PRIMARY = "primary"
    FALLBACK = "fallback"
    NO_CONSENSUS = "no_consensus"


class EquivalenceVerdict(str, Enum):
    CLEAN = "clean"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"


class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
