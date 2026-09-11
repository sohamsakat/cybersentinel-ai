from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, ConfigDict, Field


class NormalizedLogEvent(BaseModel):
    """
    Standard Normalized Security Event Schema across all heterogeneous log sources
    (Elastic Common Schema [ECS] inspired).
    """
    timestamp: datetime = Field(..., description="Timestamp of the event in UTC")
    source_type: str = Field(..., description="windows, linux_syslog, apache, firewall")
    source_ip: Optional[str] = Field(None, description="Originating IPv4 or IPv6 address")
    destination_ip: Optional[str] = Field(None, description="Target host or IP address")
    source_port: Optional[int] = Field(None, description="Originating network port")
    destination_port: Optional[int] = Field(None, description="Target service port")
    user: Optional[str] = Field(None, description="Target user account or username involved")
    event_type: str = Field(..., description="Normalized action: e.g., FAILED_LOGIN, SUCCESSFUL_LOGIN, HTTP_REQUEST, PRIVILEGE_ESCALATION, PORT_SCAN")
    severity_hint: str = Field(default="INFO", description="INFO, WARNING, ALERT, CRITICAL")
    raw_message: str = Field(..., description="Exact raw log string for forensic traceability")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Arbitrary engine-specific metadata (e.g., EventID, HTTP status code, flags)")


class LogBatchResponse(BaseModel):
    id: int
    filename: str
    source_type: str
    raw_count: int
    status: str
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)
