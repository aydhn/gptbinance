from typing import Dict, Any, List
# pylint: disable=unused-import
# flake8: noqa
from .models import AuthorityArtifactManifest

class ManifestBuilder:
    def build(self) -> AuthorityArtifactManifest:
        return AuthorityArtifactManifest("mani-1", {}, {})
