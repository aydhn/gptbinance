import pytest
from app.model_plane.outputs import OutputValidator, TypedOutputDescriptor
from app.model_plane.models import OutputSchema
from app.model_plane.enums import OutputClass


def test_output_validation_scalar():
    validator = OutputValidator()
    schema = OutputSchema(
        output_class=OutputClass.SCALAR_SCORE,
        description="Test",
        expected_range=[0.0, 1.0],
    )

    valid_desc = TypedOutputDescriptor(
        output_id="out1",
        model_id="m1",
        checkpoint_id="c1",
        output_class=OutputClass.SCALAR_SCORE,
        raw_value=0.5,
    )
    assert validator.validate_output(valid_desc, schema) is True

    invalid_desc = TypedOutputDescriptor(
        output_id="out1",
        model_id="m1",
        checkpoint_id="c1",
        output_class=OutputClass.SCALAR_SCORE,
        raw_value=1.5,
    )
    assert validator.validate_output(invalid_desc, schema) is False


def test_output_validation_binary():
    validator = OutputValidator()
    schema = OutputSchema(
        output_class=OutputClass.BINARY_CLASS,
        description="Test",
        classes=["UP", "DOWN"],
    )

    valid_desc = TypedOutputDescriptor(
        output_id="out1",
        model_id="m1",
        checkpoint_id="c1",
        output_class=OutputClass.BINARY_CLASS,
        raw_value="UP",
    )
    assert validator.validate_output(valid_desc, schema) is True


def test_output_validation_missing():
    validator = OutputValidator()
    schema = OutputSchema(output_class=OutputClass.SCALAR_SCORE, description="Test")

    missing_desc = TypedOutputDescriptor(
        output_id="out1",
        model_id="m1",
        checkpoint_id="c1",
        output_class=OutputClass.SCALAR_SCORE,
        raw_value=None,
        is_missing=True,
    )
    assert validator.validate_output(missing_desc, schema) is False


def test_output_validation_class_mismatch():
    validator = OutputValidator()
    schema = OutputSchema(output_class=OutputClass.BINARY_CLASS, description="Test")

    mismatch_desc = TypedOutputDescriptor(
        output_id="out1",
        model_id="m1",
        checkpoint_id="c1",
        output_class=OutputClass.SCALAR_SCORE,
        raw_value=0.5,
    )
    assert validator.validate_output(mismatch_desc, schema) is False
