from app.constitution_plane.models import RuleTaxonomyRecord
from app.constitution_plane.enums import RuleTaxonomy
from typing import Dict

class RuleTaxonomyManager:
    def __init__(self):
        self.taxonomies: Dict[RuleTaxonomy, RuleTaxonomyRecord] = {
            RuleTaxonomy.BLOCKER: RuleTaxonomyRecord(taxonomy_class=RuleTaxonomy.BLOCKER, description="Non-waivable blocker."),
            RuleTaxonomy.CAUTION: RuleTaxonomyRecord(taxonomy_class=RuleTaxonomy.CAUTION, description="Warning that contributes to compound risk."),
            RuleTaxonomy.REVIEW_REQUIRED: RuleTaxonomyRecord(taxonomy_class=RuleTaxonomy.REVIEW_REQUIRED, description="Mandatory manual review."),
            RuleTaxonomy.VETO: RuleTaxonomyRecord(taxonomy_class=RuleTaxonomy.VETO, description="Hard stop."),
            RuleTaxonomy.WAIVER_ELIGIBLE: RuleTaxonomyRecord(taxonomy_class=RuleTaxonomy.WAIVER_ELIGIBLE, description="Can be bypassed with valid waiver."),
            RuleTaxonomy.OVERRIDE_PROHIBITED: RuleTaxonomyRecord(taxonomy_class=RuleTaxonomy.OVERRIDE_PROHIBITED, description="Cannot be overridden under any circumstance.")
        }
