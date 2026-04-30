from app.ml.models import LabelSpec
from app.ml.enums import LabelType


class MetaLabeler:
    def generate_labels(self, data: "pd.DataFrame", spec: LabelSpec) -> "pd.Series":
        # future horizon logic, source price reference, etc
        pass
