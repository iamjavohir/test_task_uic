from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class EventBase(BaseModel):
    title: str
    all_day: bool = False
    time_start: datetime
    time_end: datetime
    rrule: Optional[str] = None
    url: Optional[str] = None
    note: Optional[str] = None


class EventCreate(EventBase):
    user_id: UUID


class EventUpdate(BaseModel):
    title: Optional[str] = None
    all_day: Optional[bool] = None
    time_start: Optional[datetime] = None
    time_end: Optional[datetime] = None
    rrule: Optional[str] = None
    url: Optional[str] = None
    note: Optional[str] = None


class Event(EventBase):
    id: UUID

    class Config:
        from_attributes = True