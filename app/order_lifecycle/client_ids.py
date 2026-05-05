import uuid


class ClientOrderIdGenerator:
    @staticmethod
    def generate(plan_id: str, leg_id: str, attempt_seq: int = 0) -> str:
        # Format compatible with strict exchanges (e.g., max 32 chars)
        short_plan = plan_id[-7:] if len(plan_id) > 7 else plan_id
        short_leg = leg_id[-7:] if len(leg_id) > 7 else leg_id
        unique = str(uuid.uuid4())[:8]
        return f"{short_plan}_{short_leg}_{attempt_seq}_{unique}"
