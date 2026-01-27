from fastapi import FastAPI, Depends
from auth import require_role
from data import MOCK_DATA

app = FastAPI(title="DiaCare Connect API")


@app.get("/")
def root():
    return {"status": "DiaCare Connect API running"}


@app.get("/patient/data")
def get_patient_data(
    user=Depends(require_role(["parent", "doctor"]))
):
    """
    Parents & doctors can view patient diabetes data
    """
    return MOCK_DATA


@app.get("/doctor/summary")
def doctor_summary(
    user=Depends(require_role(["doctor"]))
):
    """
    Doctors only: long-term clinical review
    """
    return {
        "message": "Clinical trends and analytics would be shown here"
    }
