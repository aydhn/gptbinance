from app.data_governance.models import (
    CanonicalEntityRef,
    SchemaVersionRef,
    ProvenanceRecord,
)
from enum import Enum
import pandas as pd
from pydantic import BaseModel, ConfigDict
from typing import Optional, Any


class Timeframe(str, Enum):
    M1 = "1m"
    M5 = "5m"
    M15 = "15m"
    H1 = "1h"
    H4 = "4h"
    D1 = "1d"
    W1 = "1wk"


class DataVendor(str, Enum):
    YFINANCE = "yfinance"
    BINANCE = "binance"
    MOCK = "mock"


class MarketDataFrame(BaseModel):
    """Wrapper around pandas DataFrame for type safety and validation."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    df: pd.DataFrame

    @classmethod
    def validate_schema(cls, df: pd.DataFrame) -> bool:
        required_columns = {"open", "high", "low", "close", "volume"}
        if not required_columns.issubset(df.columns):
            return False
        if not isinstance(df.index, pd.DatetimeIndex) and "timestamp" not in df.columns:
            return False
        return True

    def __init__(self, df: pd.DataFrame, **data: Any):
        super().__init__(df=df, **data)
        if not self.validate_schema(self.df):
            raise ValueError(
                "Invalid DataFrame schema. Must have OHLCV columns and datetime index/timestamp."
            )

        if (
            not isinstance(self.df.index, pd.DatetimeIndex)
            and "timestamp" in self.df.columns
        ):
            self.df["timestamp"] = pd.to_datetime(self.df["timestamp"])
            self.df.set_index("timestamp", inplace=True)
            self.df.index.name = "timestamp"

        if (
            isinstance(self.df.index, pd.DatetimeIndex)
            and self.df.index.name != "timestamp"
        ):
            self.df.index.name = "timestamp"
