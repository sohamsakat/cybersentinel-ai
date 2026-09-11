from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.session import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, ForeignKey("log_batches.id"), nullable=True)

    title = Column(String(256), nullable=False)
    severity = Column(String(16), default="MEDIUM", nullable=False)  # LOW, MEDIUM, HIGH, CRITICAL
    risk_score = Column(Float, default=50.0, nullable=False)  # 0.0 - 100.0
    attack_category = Column(String(128), nullable=False)  # Credential Access, Initial Access, etc.
    mitre_technique_id = Column(String(32), nullable=True)  # e.g., T1110
    mitre_technique_name = Column(String(128), nullable=True)  # e.g., Brute Force
    source_ip = Column(String(64), nullable=True)
    target_host = Column(String(128), nullable=True)
    confidence_score = Column(Float, default=0.85, nullable=False)  # 0.0 - 1.0

    summary = Column(Text, nullable=False)
    technical_details = Column(Text, nullable=True)
    recommended_mitigation = Column(Text, nullable=True)
    status = Column(String(32), default="OPEN", nullable=False)  # OPEN, INVESTIGATING, CONTAINED, RESOLVED

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    batch = relationship("LogBatch", back_populates="incidents")
