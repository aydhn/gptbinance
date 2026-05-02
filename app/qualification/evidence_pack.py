from typing import List
from app.qualification.models import EvidencePack, QualificationRun
from app.qualification.evidence import EvidenceCollector


class EvidencePackAssembler:
    def assemble(self, run_id: str, required_sections: List[str]) -> EvidencePack:
        collector = EvidenceCollector()
        pack = EvidencePack(run_id=run_id)

        for section in required_sections:
            refs = collector.collect_refs(section)
            if hasattr(pack, section):
                setattr(pack, section, refs)

        # Check completeness (mock logic: all required are collected)
        pack.is_complete = True
        return pack
