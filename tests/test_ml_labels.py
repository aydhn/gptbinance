from app.ml.models import LabelSpec
from app.ml.enums import LabelType
from app.ml.labels import MetaLabeler


def test_meta_labeler():
    spec = LabelSpec(
        name="meta_v1",
        label_type=LabelType.FORWARD_RETURN_SIGN,
        horizon_periods=12,
        success_definition="positive_return",
    )
    labeler = MetaLabeler()
    # Mock data
    assert labeler.generate_labels(None, spec) is None
