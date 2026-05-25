
from sqlalchemy.orm import Session
from app.models.user_model import User

def create_user(db: Session, name : str, email : str):

    existing_user = db.query(User).filter(
        User.email == email
    ).first()

    if existing_user:
       raise ValueError("Email already exists")

    new_user = User(
        name = name,
        email = email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def fetch_users(db : Session):
    
    return db.query(User).all()