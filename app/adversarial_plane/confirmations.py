class ConfirmationIntegration:
    def confirm_exploit(self):
        # exploit confirmed states eradicate/contain/restore remedy refs olmadan trusted sayılmasın
        pass


def detect_adversarial_consent(consent_chain: list, rights_registry) -> str:
    if rights_registry.has_adversarial_manipulation(consent_chain):
        return "explicit caution: compliant consent chain under adversarial manipulation"
    return "trusted"
