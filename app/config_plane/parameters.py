from app.config_plane.models import ConfigParameter, ConfigParameterRef
from app.config_plane.enums import ConfigDomain, MutabilityClass, ParameterClass
from app.config_plane.exceptions import InvalidParameterDefinition

def create_parameter(
    domain: ConfigDomain,
    name: str,
    type_name: str,
    owner: str,
    mutability_class: MutabilityClass,
    parameter_class: ParameterClass = ParameterClass.STANDARD,
    experimentable: bool = False,
    runtime_safe: bool = False,
    release_sensitive: bool = False,
    has_default: bool = False,
    default_value: any = None
) -> ConfigParameter:

    if has_default and default_value is None and type_name != "Optional":
        # Simplified validation
        pass

    return ConfigParameter(
        ref=ConfigParameterRef(domain=domain, name=name),
        type_name=type_name,
        owner=owner,
        mutability_class=mutability_class,
        parameter_class=parameter_class,
        experimentable=experimentable,
        runtime_safe=runtime_safe,
        release_sensitive=release_sensitive,
        has_default=has_default,
        default_value=default_value
    )

# Bootstrap some canonical parameters to simulate a registry
strategy_params = {
    "feature_flags.enable_ml": create_parameter(
        domain=ConfigDomain.STRATEGY,
        name="feature_flags.enable_ml",
        type_name="bool",
        owner="strategy_team",
        mutability_class=MutabilityClass.RUNTIME_SAFE,
        experimentable=True,
        runtime_safe=True,
        has_default=True,
        default_value=False
    )
}
risk_params = {
    "max_daily_loss_pct": create_parameter(
        domain=ConfigDomain.RISK,
        name="max_daily_loss_pct",
        type_name="float",
        owner="risk_team",
        mutability_class=MutabilityClass.REVIEW_ONLY,
        has_default=True,
        default_value=2.0
    )
}
# A helper to auto-register them
from app.config_plane.schemas import registry, ConfigSchema, ConfigSchemaVersion
import uuid

def bootstrap_registry():
    registry.register_schema(ConfigSchema(
        domain=ConfigDomain.STRATEGY,
        version=ConfigSchemaVersion(version_id=str(uuid.uuid4())),
        parameters=strategy_params
    ))
    registry.register_schema(ConfigSchema(
        domain=ConfigDomain.RISK,
        version=ConfigSchemaVersion(version_id=str(uuid.uuid4())),
        parameters=risk_params
    ))

bootstrap_registry()

class ConfigFeatureLinkage:
    def link_params(self):
        pass
