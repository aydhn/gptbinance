import pytest
from app.continuity_plane.rollups import ContinuityRollupGenerator

def test_rollup_generator():
    generator = ContinuityRollupGenerator()
    assert generator is not None
