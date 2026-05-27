from pydantic import BaseModel
from typing import List

class TimelineEvent(BaseModel):
    date: str
    event: str

class CaseSheetSummary(BaseModel):
    patient_overview: str
    chief_complaints: List[str]
    diagnosis: List[str]
    medications: List[str]
    lab_findings: List[str]
    treatment_given: List[str]
    risks_alerts: List[str]
    timeline: List[TimelineEvent]
    doctor_handoff_summary: str