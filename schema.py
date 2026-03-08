from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# --- INPUT: Edge to Cloud ---
class ECGPacket(BaseModel):
    device_id: str = "SIM-001"
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    # 100 normalized data points (the temporal window)
    raw_signal: List[float] 
    # For cryptographic verification (Member C's focus)
    signature: Optional[str] = None 

# --- OUTPUT: AI Engine to Dashboard ---
class AnalysisResult(BaseModel):
    # Probability of a medical event (0.0 to 1.0)
    disease_score: float 
    # Quality of data (0.0 = total noise/failure, 1.0 = clean)
    integrity_score: float 
    # Final triage status
    status: str = "GREEN" # RED, YELLOW, or GREEN
    # Recommendation for the Clinical Report
    recommendation: str 

# --- CLINICAL REPORT: Dashboard Export ---
class ClinicalReport(BaseModel):
    patient_id: str
    report_id: str
    generated_at: str
    summary_findings: str
