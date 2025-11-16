from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr
    display_name: Optional[str]

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID
    tz: str

    class Config:
        orm_mode = True
