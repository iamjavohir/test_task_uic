import uuid
from sqlalchemy import Column, String, Boolean, TIMESTAMP, ForeignKey, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    display_name = Column(String)
    password_hash = Column(String, nullable=False)
    tz = Column(String, default="Asia/Tashkent")
