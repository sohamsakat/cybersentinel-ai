from typing import List, Optional
from pydantic import BaseModel, Field


class ChatMessage(BaseModel):
    role: str = Field(..., description="user, assistant, or system")
    content: str = Field(..., description="Text content of the message")


class ChatRequest(BaseModel):
    message: str = Field(..., description="Natural language question from SOC analyst")
    incident_id: Optional[int] = Field(None, description="Optional incident ID for specific triage context")
    history: List[ChatMessage] = Field(default_factory=list, description="Recent conversation turns")


class ChatResponse(BaseModel):
    answer: str = Field(..., description="AI response grounded in MITRE ATT&CK & incident data")
    cited_sources: List[str] = Field(default_factory=list, description="MITRE Techniques or documentation cited")
