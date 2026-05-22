import pytest
import os

def test_jurisdiction():
    assert os.path.exists("app/jurisdiction_plane/applicability.py")

def test_finality():
    assert os.path.exists("app/finality_plane/settlement.py")

def test_commitment():
    assert os.path.exists("app/commitment_plane/breaches.py")
