from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from app.db.session import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String(64), nullable=False)  # e.g., LOGIN, UPLOAD_LOG, CHANGE_STATUS, EXPORT_PDF
    target_type = Column(String(32), nullable=True)  # INCIDENT, USER, SYSTEM
    target_id = Column(Integer, nullable=True)
    details = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
