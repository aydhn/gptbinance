import sys
try:
    import pytest
    pytest.main(["tests/test_performance_security_plane.py", "-v"])
except Exception as e:
    print(e)
