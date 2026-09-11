from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field


class IncidentBase(BaseModel):
    title: str
    severity: str = "MEDIUM"
    risk_score: float = Field(..., ge=0.0, le=100.0)
    attack_category: str
    mitre_technique_id: Optional[str] = None
    mitre_technique_name: Optional[str] = None
    source_ip: Optional[str] = None
    target_host: Optional[str] = None
    confidence_score: float = Field(default=0.85, ge=0.0, le=1.0)
    summary: str
    technical_details: Optional[str] = None
    recommended_mitigation: Optional[str] = None
    status: str = "OPEN"


class IncidentCreate(IncidentBase):
    batch_id: Optional[int] = None


class IncidentUpdate(BaseModel):
    status: Optional[str] = None  # OPEN, INVESTIGATING, CONTAINED, RESOLVED
    severity: Optional[str] = None
    recommended_mitigation: Optional[str] = None


class IncidentResponse(IncidentBase):
    id: int
    batch_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class IncidentStats(BaseModel):
    total_incidents: int
    critical_count: int
    high_count: int
    medium_count: int
    low_count: int
    open_count: int
    investigating_count: int
    resolved_count: int
    top_techniques: List[Dict[str, int]]
    recent_alerts: List[IncidentResponse]


class AIThreatAnalysisResult(BaseModel):
    """
    Strict structured output contract produced by LLM + RAG reasoning engine.
    Ensures zero hallucinated schema deviations.
    """
    threat_detected: bool = Field(..., description="Whether malicious or anomalous activity was detected")
    title: str = Field(..., description="Concise headline of the security incident")
    severity: str = Field(..., description="CRITICAL, HIGH, MEDIUM, or LOW")
    risk_score: float = Field(..., ge=0.0, le=100.0, description="0.0 to 100.0 calculated risk score")
    attack_category: str = Field(..., description="MITRE ATT&CK Tactic name, e.g. Credential Access")
    mitre_technique_id: str = Field(..., description="MITRE Technique ID, e.g. T1110")
    mitre_technique_name: str = Field(..., description="MITRE Technique Name, e.g. Brute Force")
    source_ip: Optional[str] = Field(None, description="Primary attacker IP address if identifiable")
    target_host: Optional[str] = Field(None, description="Impacted asset, server or endpoint")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="AI confidence in this classification")
    summary: str = Field(..., description="Executive summary of the attack for management")
    technical_details: str = Field(..., description="In-depth forensic narrative with log evidence citations")
    recommended_mitigation: str = Field(..., description="Step-by-step containment and remediation playbook")
