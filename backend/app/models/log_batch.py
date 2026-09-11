from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base


class LogBatch(Base):
    __tablename__ = "log_batches"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(256), nullable=False)
    source_type = Column(String(32), nullable=False)  # windows, linux_syslog, apache, firewall
    raw_count = Column(Integer, default=0, nullable=False)
    status = Column(String(32), default="UPLOADED", nullable=False)  # UPLOADED, PARSED, ANALYZED, FAILED
    uploaded_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    uploaded_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    uploader = relationship("User", back_populates="log_batches")
    incidents = relationship("Incident", back_populates="batch", cascade="all, delete-orphan")
