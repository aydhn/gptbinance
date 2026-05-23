class JurisdictionApplicability:
    def check_scope_precedent(self):
        pass

# Precedent Plane Integration added


def check_jurisdiction_beneficiary_scope(right_id: str, jurisdiction: str, rights_registry) -> str:
    if not rights_registry.is_right_valid_in_jurisdiction(right_id, jurisdiction):
        return "explicit caution: right exists but wrong-scope beneficiary"
    return "trusted"
