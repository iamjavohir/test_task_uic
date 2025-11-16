from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.event import EventCreate
import uuid
from datetime import datetime


def create_event(db: Session, event_data: EventCreate):
    event = Event(
        id=uuid.uuid4(),
        user_id=event_data.user_id,
        title=event_data.title,
        all_day=event_data.all_day,
        time_start=event_data.time_start,
        time_end=event_data.time_end,
        rrule=event_data.rrule,
        url=event_data.url,
        note=event_data.note
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def update_event(db: Session, event_id: str, updates: dict):
    event = db.query(Event).filter(Event.id == event_id).first()
    for key, value in updates.items():
        setattr(event, key, value)
    db.commit()
    db.refresh(event)
    return event

def delete_event(db: Session, event_id: str):
    event = db.query(Event).filter(Event.id == event_id).first()
    db.delete(event)
    db.commit()
    return True

def get_events(db: Session, user_id: str, start: datetime = None, end: datetime = None):
    q = db.query(Event).filter(Event.user_id == user_id)
    if start:
        q = q.filter(Event.time_start >= start)
    if end:
        q = q.filter(Event.time_end <= end)
    return q.all()