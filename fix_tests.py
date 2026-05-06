import re


def fix():
    files = [
        "tests/test_experiments_ablation.py",
        "tests/test_experiments_baselines.py",
        "tests/test_experiments_candidates.py",
        "tests/test_experiments_comparisons.py",
        "tests/test_experiments_definitions.py",
        "tests/test_experiments_findings.py",
        "tests/test_experiments_fragility.py",
        "tests/test_experiments_hypotheses.py",
        "tests/test_experiments_offline.py",
        "tests/test_experiments_packs.py",
        "tests/test_experiments_scopes.py",
        "tests/test_experiments_sensitivity.py",
        "tests/test_experiments_metrics.py",
        "tests/test_experiments_regimes.py",
        "tests/test_experiments_timesplits.py",
        "tests/test_experiments_paper_validation.py",
        "tests/test_experiments_promotions.py",
        "tests/test_experiments_policy.py",
        "tests/test_experiments_storage.py",
    ]

    for f in files:
        with open(f, "r") as fp:
            content = fp.read()

        with open(f, "w") as fp:
            fp.write(content)


if __name__ == "__main__":
    fix()
