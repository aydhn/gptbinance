# Canonical implementation for common
from app.recapitalization_plane.models import *
from app.recapitalization_plane.exceptions import *

def process_common(recap: RecapitalizationObject):
    return {"status": "processed", "module": "common"}
