from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import UserCreate, User
from app.core.database import get_db
from app.crud.user import create_user, get_user
from app.core.security import verify_token  # <-- auth import qilindi

router = APIRouter()

@router.post("/", response_model=User)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    token: str = Depends(verify_token)  # <-- token tekshirish
):
    db_user = create_user(db, email=user.email, display_name=user.display_name)
    return db_user

@router.get("/{user_id}", response_model=User)
def read_user(
    user_id: str,
    db: Session = Depends(get_db),
    token: str = Depends(verify_token)  # <-- token tekshirish
):
    db_user = get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user