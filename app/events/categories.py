# Categorization logic / helpers
from app.events.enums import EventCategory


def categorize_title(title: str) -> EventCategory:
    title_lower = title.lower()
    if "cpi" in title_lower or "inflation" in title_lower:
        return EventCategory.INFLATION
    if "nfp" in title_lower or "payroll" in title_lower or "employment" in title_lower:
        return EventCategory.LABOR
    if "fomc" in title_lower or "rate decision" in title_lower:
        return EventCategory.MACRO_POLICY
    if "gdp" in title_lower:
        return EventCategory.GDP
    if "maintenance" in title_lower:
        return EventCategory.EXCHANGE_MAINTENANCE
    return EventCategory.OTHER
