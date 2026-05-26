# Canonical implementation for debt
from app.recapitalization_plane.models import *
from app.recapitalization_plane.exceptions import *

def process_debt(recap: RecapitalizationObject):
    return {"status": "processed", "module": "debt"}
