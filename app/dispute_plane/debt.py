class DebtTracker:
    def calculate_debt(self, dispute):
        debt = 0
        if [i for i in dispute.issues if not i.resolved]:
            debt += 100 # Issue burial debt
        return debt
