import pytest
import json
from app.connectors.binance.ws_message_parser import BinanceWsMessageParser
from app.data.live_stream_models import KlineUpdateEvent, TickerEvent, BookTickerEvent


def test_parse_kline():
    parser = BinanceWsMessageParser()
    payload = {
        "e": "kline",
        "E": 123456789,
        "s": "BTCUSDT",
        "k": {
            "t": 123000000,
            "T": 123059999,
            "s": "BTCUSDT",
            "i": "1m",
            "f": 100,
            "L": 200,
            "o": "0.0010",
            "c": "0.0020",
            "h": "0.0025",
            "l": "0.0015",
            "v": "1000",
            "n": 100,
            "x": False,
            "q": "1.0000",
            "V": "500",
            "Q": "0.500",
            "B": "123456",
        },
    }

    # Simulate a stream envelope
    raw_msg = json.dumps({"stream": "btcusdt@kline_1m", "data": payload})

    event = parser.parse_message(raw_msg)
    assert isinstance(event, KlineUpdateEvent)
    assert event.symbol == "BTCUSDT"
    assert event.interval == "1m"
    assert event.close_price == 0.0020


def test_parse_ticker():
    parser = BinanceWsMessageParser()
    payload = {
        "e": "24hrTicker",
        "E": 123456789,
        "s": "BNBBTC",
        "p": "0.0015",
        "P": "250.00",
        "w": "0.0018",
        "x": "0.0009",
        "c": "0.0025",
        "Q": "10",
        "b": "0.0024",
        "B": "10",
        "a": "0.0026",
        "A": "100",
        "o": "0.0010",
        "h": "0.0025",
        "l": "0.0010",
        "v": "10000",
        "q": "18",
        "O": 0,
        "C": 86400000,
        "F": 0,
        "L": 18150,
        "n": 18151,
    }

    raw_msg = json.dumps(payload)  # direct without stream envelope
    event = parser.parse_message(raw_msg)
    assert isinstance(event, TickerEvent)
    assert event.symbol == "BNBBTC"
    assert event.last_price == 0.0025


def test_parse_book_ticker():
    parser = BinanceWsMessageParser()
    payload = {
        "u": 400900217,
        "s": "BNBUSDT",
        "b": "25.35190000",
        "B": "31.21000000",
        "a": "25.36520000",
        "A": "40.66000000",
    }

    raw_msg = json.dumps({"stream": "bnbusdt@bookTicker", "data": payload})
    event = parser.parse_message(raw_msg)
    assert isinstance(event, BookTickerEvent)
    assert event.symbol == "BNBUSDT"
    assert event.best_bid_price == 25.3519


def test_parse_error():
    parser = BinanceWsMessageParser()
    event = parser.parse_message("not a json")
    assert event is None
