from datetime import datetime, timedelta, timezone
import uuid
from typing import List, Dict
from .models import RiskCooldownRecord
from .enums import CooldownClass, RiskDomain


class CooldownGovernance:
    def __init__(self):
        self._cooldowns: Dict[str, RiskCooldownRecord] = {}

    def apply_cooldown(
        self,
        domain: RiskDomain,
        target_id: str,
        cooldown_class: CooldownClass,
        duration_minutes: int,
        reason: str,
    ) -> RiskCooldownRecord:
        now = datetime.now(timezone.utc)
        record = RiskCooldownRecord(
            cooldown_id=str(uuid.uuid4()),
            cooldown_class=cooldown_class,
            target_domain=domain,
            target_id=target_id,
            start_time=now,
            end_time=now + timedelta(minutes=duration_minutes),
            active=True,
            reason=reason,
        )
        self._cooldowns[record.cooldown_id] = record
        return record

    def is_active(self, domain: RiskDomain, target_id: str) -> bool:
        now = datetime.now(timezone.utc)
        for cd in self._cooldowns.values():
            if cd.target_domain == domain and cd.target_id == target_id:
                if cd.active and cd.end_time > now:
                    return True
        return False

    def get_active_cooldowns(self) -> List[RiskCooldownRecord]:
        now = datetime.now(timezone.utc)
        return [
            cd for cd in self._cooldowns.values() if cd.active and cd.end_time > now
        ]


global_cooldown_governance = CooldownGovernance()
