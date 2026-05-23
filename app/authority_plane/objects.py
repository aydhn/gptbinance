from typing import Dict, List
# pylint: disable=unused-import
# flake8: noqa
from .models import AuthorityObject
from .enums import AuthorityClass

class AuthorityObjectManager:
    def __init__(self):
        self.objects = {}

    def create_authoritative(self, id: str, owner: str, scope: List[str]) -> AuthorityObject:
        obj = AuthorityObject(
            authority_id=id, class_type=AuthorityClass.BINDING, owner=owner,
            scope=scope, mandate_posture={}, legitimacy_posture={}
        )
        self.objects[id] = obj
        return obj

    def create_local(self, id: str, owner: str, scope: List[str]) -> AuthorityObject:
        obj = AuthorityObject(
            authority_id=id, class_type=AuthorityClass.ADVISORY, owner=owner,
            scope=scope, mandate_posture={}, legitimacy_posture={}
        )
        self.objects[id] = obj
        return obj

    def create_federated(self, id: str, owner: str, scope: List[str]) -> AuthorityObject:
        obj = AuthorityObject(
            authority_id=id, class_type=AuthorityClass.FEDERATED, owner=owner,
            scope=scope, mandate_posture={}, legitimacy_posture={}
        )
        self.objects[id] = obj
        return obj

    def create_customer_facing(self, id: str, owner: str, scope: List[str]) -> AuthorityObject:
        obj = AuthorityObject(
            authority_id=id, class_type=AuthorityClass.BINDING, owner=owner,
            scope=scope, mandate_posture={"customer_facing": True}, legitimacy_posture={}
        )
        self.objects[id] = obj
        return obj
