import subprocess

subprocess.run(
    [
        "poetry",
        "run",
        "flake8",
        "app/readiness_board/",
        "tests/test_readiness_board_admissibility.py",
        "tests/test_readiness_board_candidates.py",
        "tests/test_readiness_board_conditional.py",
        "tests/test_readiness_board_contradictions.py",
        "tests/test_readiness_board_decisions.py",
        "tests/test_readiness_board_domains.py",
        "tests/test_readiness_board_dossier.py",
        "tests/test_readiness_board_evidence.py",
        "tests/test_readiness_board_freeze.py",
        "tests/test_readiness_board_history.py",
        "tests/test_readiness_board_memos.py",
        "tests/test_readiness_board_promotions.py",
        "tests/test_readiness_board_resolution.py",
        "tests/test_readiness_board_storage.py",
    ]
)
