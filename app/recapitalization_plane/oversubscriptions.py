# Canonical implementation for oversubscriptions
from app.recapitalization_plane.models import *
from app.recapitalization_plane.exceptions import *

def process_oversubscriptions(recap: RecapitalizationObject):
    return {"status": "processed", "module": "oversubscriptions"}
