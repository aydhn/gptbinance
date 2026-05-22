import pytest
import os

# We can run pytest to ensure the generated tests at least pass basic scaffolding
exit_code = os.system("pytest tests/test_precedent_plane_*.py -v")
print(f"Tests finished with exit code {exit_code}")
