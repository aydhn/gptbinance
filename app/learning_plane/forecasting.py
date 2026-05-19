from app.learning_plane.models import LearningForecastReport
from app.learning_plane.storage import storage

def create_forecast(forecast: LearningForecastReport):
    storage.save_forecast(forecast)
