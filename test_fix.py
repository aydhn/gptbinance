from app.config_plane.schemas import registry, ConfigSchema, ConfigSchemaVersion
from app.config_plane.enums import ConfigDomain

print("Registry initialized?", registry is not None)
print("Strategy Schema:", registry.get_schema(ConfigDomain.STRATEGY))

import sys
print(sys.modules.get('app.config_plane.schemas'))
print(sys.modules.get('app.config_plane.parameters'))
