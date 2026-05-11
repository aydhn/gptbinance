import pytest
from app.migration_plane.fallbacks import FallbackManager

def test_execute_fallback():
    manager = FallbackManager()
    result = manager.execute_fallback("mig_001")
    assert result.is_successful is True
