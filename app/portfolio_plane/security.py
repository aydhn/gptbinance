class SecurityLinkage:
    @staticmethod
    def check_mandatory_security_displacement(displaced_ids: list, security_initiative_ids: list) -> bool:
        return any(sid in displaced_ids for sid in security_initiative_ids)
