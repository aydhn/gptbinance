import os

files = [
    "app/crossbook/__init__.py",
    "app/crossbook/models.py",
    "app/crossbook/enums.py",
    "app/crossbook/exceptions.py",
    "app/crossbook/base.py",
    "app/crossbook/books.py",
    "app/crossbook/mapping.py",
    "app/crossbook/graph.py",
    "app/crossbook/netting.py",
    "app/crossbook/collateral.py",
    "app/crossbook/borrow.py",
    "app/crossbook/funding.py",
    "app/crossbook/basis.py",
    "app/crossbook/conflicts.py",
    "app/crossbook/liquidation.py",
    "app/crossbook/overlay.py",
    "app/crossbook/policies.py",
    "app/crossbook/reporting.py",
    "app/crossbook/storage.py",
    "app/crossbook/repository.py",
    "app/crossbook/README.md",
    "docs/206_cross_book_exposure_ve_teminat_governance_mimarisi.md",
    "docs/207_fake_hedge_mode_conflict_ve_net_exposure_durustlugu_politikasi.md",
    "docs/208_collateral_pressure_borrow_dependency_ve_liquidation_sensitivity_politikasi.md",
    "docs/209_cross_book_overlay_qualification_ve_replay_entegrasyon_politikasi.md",
    "docs/210_phase_40_definition_of_done.md",
    "tests/test_crossbook_books.py",
    "tests/test_crossbook_mapping.py",
    "tests/test_crossbook_graph.py",
    "tests/test_crossbook_netting.py",
    "tests/test_crossbook_collateral.py",
    "tests/test_crossbook_borrow.py",
    "tests/test_crossbook_funding.py",
    "tests/test_crossbook_basis.py",
    "tests/test_crossbook_conflicts.py",
    "tests/test_crossbook_liquidation.py",
    "tests/test_crossbook_overlay.py",
    "tests/test_crossbook_policies.py",
    "tests/test_crossbook_storage.py",
]

for f in files:
    os.makedirs(os.path.dirname(f), exist_ok=True)
    if not os.path.exists(f):
        with open(f, "w") as file:
            if f.endswith(".py") and f != "app/crossbook/__init__.py":
                file.write('"""\n' + os.path.basename(f) + '\n"""\n')
            elif f.endswith(".md"):
                file.write('# ' + os.path.basename(f).replace('.md', '').replace('_', ' ') + '\n')
