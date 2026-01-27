from datetime import datetime
from models import GlucoseReading, InsulinDose, PatientData

MOCK_DATA = PatientData(
    glucose=[
        GlucoseReading(timestamp=datetime.now(), value=6.2),
        GlucoseReading(timestamp=datetime.now(), value=7.1),
    ],
    insulin=[
        InsulinDose(timestamp=datetime.now(), units=4.0),
    ],
    carbs=45,
)
