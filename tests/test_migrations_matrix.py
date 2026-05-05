from app.migrations.matrix import CompatibilityMatrixBuilder
from app.migrations.enums import MigrationDomain


def test_matrix_builder():
    builder = CompatibilityMatrixBuilder()
    matrix = builder.build(
        current_versions={MigrationDomain.CONFIG: "1.0.0"}, known_conflicts=["m1"]
    )

    assert matrix.domain_versions[MigrationDomain.CONFIG] == "1.0.0"
    assert matrix.mixed_version_safety is False
    assert "m1" in matrix.known_conflicts
