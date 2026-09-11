from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from app.db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(128), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    role = Column(String(32), default="tier1_analyst", nullable=False)  # admin, tier1_analyst, incident_commander
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    log_batches = relationship("LogBatch", back_populates="uploader")
