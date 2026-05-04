with open('app/observability/runbooks.py', 'r') as f:
    content = f.read()

if "from app.observability.models import RunbookRef" not in content:
    content = "from app.observability.models import RunbookRef\n" + content

with open('app/observability/runbooks.py', 'w') as f:
    f.write(content)
