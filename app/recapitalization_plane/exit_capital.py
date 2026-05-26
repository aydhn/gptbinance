# Canonical implementation for exit_capital
from app.recapitalization_plane.models import *
from app.recapitalization_plane.exceptions import *

def process_exit_capital(recap: RecapitalizationObject):
    return {"status": "processed", "module": "exit_capital"}
