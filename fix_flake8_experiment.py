import subprocess

with open("app/experiment_plane/__init__.py", "w") as f:
    f.write("from .registry import CanonicalExperimentRegistry\n")
    f.write("from .fairness import StandardFairnessEvaluator\n")
    f.write("from .stopping import StandardStoppingEvaluator\n")
    f.write("from .trust import StandardTrustEvaluator\n")
    f.write("\n__all__ = [\n    'CanonicalExperimentRegistry',\n    'StandardFairnessEvaluator',\n    'StandardStoppingEvaluator',\n    'StandardTrustEvaluator',\n]\n")

subprocess.run(["poetry", "run", "black", "app/experiment_plane/"])
subprocess.run(["poetry", "run", "flake8", "app/experiment_plane/"])
