import pytest
from app.release.installer import Installer
from app.release.manifest import ManifestGenerator


def test_installer_create_plan():
    inst = Installer()
    plan = inst.create_plan(ManifestGenerator().create_manifest())
    assert plan.verdict is not None
