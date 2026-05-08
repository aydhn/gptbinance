from typing import Dict, Any, Optional
from pydantic import BaseModel, ConfigDict
from app.model_plane.models import OutputSchema, ModelPlaneBaseModel
from app.model_plane.enums import OutputClass
from app.model_plane.exceptions import ModelPlaneError


class TypedOutputDescriptor(ModelPlaneBaseModel):
    output_id: str
    model_id: str
    checkpoint_id: str
    output_class: OutputClass
    raw_value: Any
    is_missing: bool = False


class OutputValidator:
    def validate_output(
        self, descriptor: TypedOutputDescriptor, schema: OutputSchema
    ) -> bool:
        if descriptor.is_missing:
            return False

        if descriptor.output_class != schema.output_class:
            return False

        if descriptor.output_class == OutputClass.SCALAR_SCORE:
            if not isinstance(descriptor.raw_value, (int, float)):
                return False
            if schema.expected_range and len(schema.expected_range) == 2:
                min_val, max_val = schema.expected_range
                if not (min_val <= descriptor.raw_value <= max_val):
                    return False

        elif descriptor.output_class == OutputClass.BINARY_CLASS:
            if not isinstance(
                descriptor.raw_value, bool
            ) and descriptor.raw_value not in [0, 1]:
                if schema.classes and descriptor.raw_value not in schema.classes:
                    return False

        elif descriptor.output_class == OutputClass.MULTICLASS_REGIME:
            if schema.classes and descriptor.raw_value not in schema.classes:
                return False

        elif descriptor.output_class == OutputClass.PROBABILITY_VECTOR:
            if not isinstance(descriptor.raw_value, (list, dict)):
                return False

        return True
