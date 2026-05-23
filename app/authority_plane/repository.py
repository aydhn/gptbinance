from typing import Dict, Any, List
# pylint: disable=unused-import
# flake8: noqa

class AuthorityRepository:
    def write(self, record: Any) -> bool:
        return True
    def read(self, id: str) -> Any:
        return None
