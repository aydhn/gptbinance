from typing import List
from .models import DataConsensusRecord, DataSourceDefinition


class ConsensusResolver:
    def resolve(
        self, primary: DataSourceDefinition, fallback: DataSourceDefinition
    ) -> DataConsensusRecord:
        # Resolve rules
        pass
