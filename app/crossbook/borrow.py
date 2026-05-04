from .models import BorrowDependencyReport
from .enums import BorrowDependencyClass

class BorrowAnalyzer:
    def analyze(self) -> BorrowDependencyReport:
        return BorrowDependencyReport(total_borrowed_usd=0.0, dependency_class=BorrowDependencyClass.NONE)
