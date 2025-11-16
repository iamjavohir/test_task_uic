from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.schemas.event import EventCreate, EventUpdate, Event
from app.core.database import get_db
from app.crud.event import create_event, get_events, update_event, delete_event

router = APIRouter()

@router.post("/", response_model=Event)
def create_new_event(event: EventCreate, db: Session = Depends(get_db)):
    return create_event(db, event_data=event)

@router.get("/", response_model=List[Event])
def list_events(user_id: str, start: Optional[datetime] = None, end: Optional[datetime] = None, db: Session = Depends(get_db)):
    return get_events(db, user_id=user_id, start=start, end=end)

@router.patch("/{event_id}", response_model=Event)
def edit_event(event_id: str, updates: EventUpdate, db: Session = Depends(get_db)):
    event = update_event(db, event_id=event_id, updates=updates.dict(exclude_unset=True))
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.delete("/{event_id}")
def remove_event(event_id: str, db: Session = Depends(get_db)):
    success = delete_event(db, event_id=event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted"}