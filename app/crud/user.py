from sqlalchemy.orm import Session
from app.models.user import User
import uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_password_hash(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_user(db: Session, email: str, password: str, display_name: str = None):
    hashed_password = get_password_hash(password)
    user = User(email=email, display_name=display_name, password_hash=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
