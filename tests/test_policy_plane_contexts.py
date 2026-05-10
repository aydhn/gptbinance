import pytest
from app.policy_plane.contexts import ContextBuilder


def test_context_builder():
    ctx = ContextBuilder().with_environment("live").with_stage("prod").build()
    assert ctx.environment == "live"
    assert ctx.stage == "prod"
