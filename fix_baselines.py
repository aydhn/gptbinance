with open("app/performance_plane/baselines.py", "r") as f:
    content = f.read()

content = content.replace("from app.performance_plane.enums import BaselineClass\n, BenchmarkClass", "from app.performance_plane.enums import BaselineClass")
with open("app/performance_plane/baselines.py", "w") as f:
    f.write(content)
