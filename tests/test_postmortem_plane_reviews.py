import pytest
from app.postmortem_plane.reviews import PostmortemReviewer

def test_reviewer():
    assert PostmortemReviewer.require_review(None) == True
