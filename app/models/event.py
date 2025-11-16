import uuid
from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base


class Event(Base):
    __tablename__ = "events"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    title = Column(String, nullable=False)
    all_day = Column(Boolean, default=False)
    time_start = Column(TIMESTAMP(timezone=True), nullable=False)
    time_end = Column(TIMESTAMP(timezone=True), nullable=False)
    rrule = Column(String)
    url = Column(String)
    note = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())

class EventInvite(Base):
    __tablename__ = "event_invites"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id", ondelete="CASCADE"))
    email = Column(String, nullable=False)

class EventAlert(Base):
    __tablename__ = "event_alerts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID(as_uuid=True), ForeignKey("events.id", ondelete="CASCADE"))
    offset_seconds = Column(Integer, nullable=False)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True))
    event_id = Column(UUID(as_uuid=True))
    action = Column(String)
    payload = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())