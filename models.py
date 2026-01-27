from pydantic import BaseModel
from typing import List
from datetime import datetime


class User(BaseModel):
    id: int
    role: str  # "parent" or "doctor"


class GlucoseReading(BaseModel):
    timestamp: datetime
    value: float


class InsulinDose(BaseModel):
    timestamp: datetime
    units: float


class PatientData(BaseModel):
    glucose: List[GlucoseReading]
    insulin: List[InsulinDose]
    carbs: int
