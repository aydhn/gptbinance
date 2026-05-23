from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import AuthorityTrustVerdict
from .enums import TrustVerdict

class TrustManager:
    def evaluate(self) -> AuthorityTrustVerdict:
        return AuthorityTrustVerdict(TrustVerdict.TRUSTED, {}, [])
