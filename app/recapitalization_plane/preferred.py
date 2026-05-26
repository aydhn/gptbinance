# Canonical implementation for preferred
from app.recapitalization_plane.models import *
from app.recapitalization_plane.exceptions import *

def process_preferred(recap: RecapitalizationObject):
    return {"status": "processed", "module": "preferred"}
