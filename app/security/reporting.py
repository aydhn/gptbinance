import json
from app.security.inventory import SecretInventory
from app.security.hardening import SecurityHardening

class SecurityReporter:
    def generate_inventory_report(self) -> str:
        inv = SecretInventory().get_inventory()
        return json.dumps([i.model_dump() for i in inv], indent=2)

    def generate_hardening_report(self) -> str:
        report = SecurityHardening().run_checks()
        return report.model_dump_json(indent=2)
