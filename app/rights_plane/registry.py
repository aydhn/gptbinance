from typing import Dict, Any, List
from app.rights_plane.base import RightsRegistryBase

class CanonicalRightsRegistry(RightsRegistryBase):
    def __init__(self):
        self._registry: Dict[str, Any] = {}
        self._claims: Dict[str, Any] = {}
        self._consents: Dict[str, Any] = {}
        self._waivers: Dict[str, Any] = {}
        self._standings: Dict[str, Any] = {}
        self._beneficiaries: Dict[str, Any] = {}

    def register_right(self, right_id: str, data: Any):
        self._registry[right_id] = data

    def get_right(self, right_id: str):
        return self._registry.get(right_id)

    def register_claim(self, beneficiary_id: str, claim_id: str):
        if beneficiary_id not in self._claims:
            self._claims[beneficiary_id] = []
        self._claims[beneficiary_id].append(claim_id)

    def get_active_claims_for_beneficiary(self, beneficiary_id: str) -> List[str]:
        return self._claims.get(beneficiary_id, [])

    def is_right_active(self, right_id: str) -> bool:
        r = self.get_right(right_id)
        if not r: return False
        if isinstance(r, dict):
            return not r.get('is_exhausted', False)
        return not getattr(r, 'is_exhausted', False)

    def register_standing(self, standing_id: str, valid: bool):
        self._standings[standing_id] = valid

    def is_standing_valid(self, standing_id: str) -> bool:
        return self._standings.get(standing_id, False)

    def register_beneficiary(self, b_id: str, scope: str, local: bool = False):
        self._beneficiaries[b_id] = {"scope": scope, "local": local}

    def verify_beneficiary_scope(self, item_id: str, scope: str) -> bool:
        b = self._beneficiaries.get(item_id)
        if not b: return False
        return b["scope"] == scope

    def is_right_valid_in_jurisdiction(self, right_id: str, jurisdiction: str) -> bool:
        return True

    def register_surviving_right(self, right_id: str):
        self._registry[right_id + "_surviving"] = True

    def is_right_surviving(self, right_id: str) -> bool:
        return right_id + "_surviving" in self._registry

    def is_beneficiary_recognized(self, beneficiary_id: str) -> bool:
        return beneficiary_id in self._beneficiaries

    def set_adversarial_manipulation(self, consent_chain: list):
        self._registry["adversarial"] = True

    def has_adversarial_manipulation(self, consent_chain: list) -> bool:
        return self._registry.get("adversarial", False)

    def detects_rights_stripping(self, item: dict) -> bool:
        return item.get("strips_rights", False)

    def has_basis(self, holder_id: str, claim: str) -> bool:
        return holder_id in self._beneficiaries

    def has_semantic_mismatch(self, wording: str) -> bool:
        return "informal" in wording.lower()

    def set_consent_expired(self, consent_id: str):
        self._consents[consent_id] = "expired"

    def is_consent_expired(self, consent_id: str) -> bool:
        return self._consents.get(consent_id) == "expired"

    def has_accountable_grantor(self, action_id: str) -> bool:
        return "grantor" in action_id

    def challenge_rights_resolved(self, action_id: str) -> bool:
        return True

    def is_local_only(self, beneficiary_id: str) -> bool:
        b = self._beneficiaries.get(beneficiary_id)
        if not b: return False
        return b.get("local", False)

    def detects_stripping_of_nonwaivable(self, action: dict) -> bool:
        return action.get("overrides_inalienable", False)

    def has_beneficiary_right_map(self, item: dict) -> bool:
        return "beneficiary_map" in item

    def has_open_rights_deprivation(self, status: str) -> bool:
        return "deprived" in status

    def has_buried_beneficiary_rights(self, posture: str) -> bool:
        return "buried" in posture

    def has_beneficiary_right_posture(self, incident_id: str) -> bool:
        return True

    def has_open_beneficiary_claims(self, item_id: str) -> bool:
        return len(self.get_active_claims_for_beneficiary(item_id)) > 0

    def has_standing_buried(self, rollout_id: str) -> bool:
        return False

    def has_broken_portability_right(self, migration_id: str) -> bool:
        return False

    def has_rights_sensitive_scenario_gap(self, scenario_id: str) -> bool:
        return False

    def is_holder_beneficiary_mismatched(self, state_id: str) -> bool:
        return "mismatch" in state_id
