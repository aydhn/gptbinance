import re

with open('tests/test_identity_plane.py', 'r') as f:
    content = f.read()

# Fix InvalidPrincipalDefinition
content = content.replace("with pytest.raises(ValueError):", "from app.identity_plane.exceptions import InvalidPrincipalDefinition\n    with pytest.raises(InvalidPrincipalDefinition):")

# Fix ImpersonationRecord and ElevationRecord calls
content = content.replace(
    'ElevationRecord(\n        record_id="e1", session_id="s1", granted_capabilities=["execute_trade"],\n        approved_by="admin2", justification="incident_response", expires_at=datetime.now(timezone.utc) + timedelta(minutes=15)\n    )',
    'ElevationRecord(\n        record_id="e1", session_id="s1", elevation_class=ElevationClass.JUST_IN_TIME, granted_capabilities=["execute_trade"],\n        approved_by="admin2", justification="incident_response", expires_at=datetime.now(timezone.utc) + timedelta(minutes=15)\n    )'
)

content = content.replace(
    'ImpersonationRecord(\n        record_id="imp1", session_id="s1", target_principal_id="target_admin",\n        approved_by="security_officer", justification="break_glass", expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)\n    )',
    'ImpersonationRecord(\n        record_id="imp1", session_id="s1", impersonation_class=ImpersonationClass.APPROVED_ADMIN, target_principal_id="target_admin",\n        approved_by="security_officer", justification="break_glass", expires_at=datetime.now(timezone.utc) + timedelta(minutes=10)\n    )'
)

# Fix AuthzEvaluationRecord return values assertions
content = content.replace('authz.evaluate("s1", "read_only", "live") == True', 'authz.evaluate("s1", "read_only", "live").is_allowed == True')
content = content.replace('authz.evaluate("s1", "execute_trade", "live") == False', 'authz.evaluate("s1", "execute_trade", "live").is_allowed == False')
content = content.replace('authz.evaluate("s1", "execute_trade", "live") == True', 'authz.evaluate("s1", "execute_trade", "live").is_allowed == True')
content = content.replace('authz.evaluate("s1", "super_admin", "live") == False', 'authz.evaluate("s1", "super_admin", "live").is_allowed == False')
content = content.replace('authz.evaluate("s1", "super_admin", "live") == True', 'authz.evaluate("s1", "super_admin", "live").is_allowed == True')

with open('tests/test_identity_plane.py', 'w') as f:
    f.write(content)
