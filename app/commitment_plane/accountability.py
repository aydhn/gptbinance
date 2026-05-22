from app.commitment_plane.models import AccountabilityRecord

class AccountabilityManager:
    @staticmethod
    def create_accountability(accountable_actor: str, execution_actor: str = None,
                              escalation_actor: str = None, breach_responder: str = None,
                              caveats: str = None) -> AccountabilityRecord:
        if not accountable_actor:
            raise ValueError("Accountable actor is required")

        return AccountabilityRecord(
            accountable_actor=accountable_actor,
            execution_actor=execution_actor,
            escalation_actor=escalation_actor,
            breach_responder=breach_responder,
            caveats=caveats,
            lineage_refs=[]
        )
