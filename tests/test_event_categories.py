from app.events.categories import categorize_title
from app.events.enums import EventCategory


def test_categorize_title():
    assert categorize_title("US CPI Data") == EventCategory.INFLATION
    assert categorize_title("NFP Release") == EventCategory.LABOR
    assert categorize_title("FOMC Statement") == EventCategory.MACRO_POLICY
    assert categorize_title("Binance Maintenance") == EventCategory.EXCHANGE_MAINTENANCE
    assert categorize_title("Random Event") == EventCategory.OTHER
