# Canonical implementation for convertibles
from app.recapitalization_plane.models import *
from app.recapitalization_plane.exceptions import *

def process_convertibles(recap: RecapitalizationObject):
    return {"status": "processed", "module": "convertibles"}
