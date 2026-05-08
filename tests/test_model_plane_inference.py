import pytest
from app.model_plane.inference import InferenceDescriptorLayer, InferenceRequest
from app.model_plane.outputs import TypedOutputDescriptor
from app.model_plane.enums import OutputClass
from datetime import datetime


def test_inference_receipt_generation():
    layer = InferenceDescriptorLayer()

    req = InferenceRequest(
        request_id="req1",
        manifest_id="mf_1",
        features={"f1": 1.0, "f2": 2.0},
        timestamp=datetime.now(),
    )

    out_desc = TypedOutputDescriptor(
        output_id="out1",
        model_id="m1",
        checkpoint_id="chk1",
        output_class=OutputClass.SCALAR_SCORE,
        raw_value=0.85,
    )

    response = layer.create_receipt(req, {"m1": out_desc})

    assert response.request_id == "req1"
    assert response.manifest_id == "mf_1"
    assert "m1" in response.outputs
    assert response.metadata["deterministic_run"] is True
    assert response.metadata["input_feature_count"] == 2
