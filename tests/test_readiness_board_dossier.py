from app.readiness_board.dossier import DossierBuilder
from app.readiness_board.storage import ReadinessBoardStorage


def test_dossier_builder():
    storage = ReadinessBoardStorage()
    builder = DossierBuilder(storage)

    dossier = builder.build_dossier("c1", "s1", {}, ["ev1"], ["ev2"], [])
    assert dossier.dossier_id.startswith("dos_")
    assert storage.get_dossier(dossier.dossier_id) is not None
