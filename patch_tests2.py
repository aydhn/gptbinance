import re

with open('tests/test_identity_plane.py', 'r') as f:
    content = f.read()

# Fix imports
content = content.replace("from app.identity_plane.enums import PrincipalClass, CapabilityRiskClass, SessionClass, TrustVerdict", "from app.identity_plane.enums import PrincipalClass, CapabilityRiskClass, SessionClass, TrustVerdict, ElevationClass, ImpersonationClass")

with open('tests/test_identity_plane.py', 'w') as f:
    f.write(content)
