from fastapi import  Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.dependencies.db import get_db

from app.schemas.user_schema import(UserCreate,UserResponse)
from app.services.user_service import (create_user, fetch_users)

router = APIRouter(prefix="/users", tags=["Users"])
########## CREATE USER ############

@router.post("/", response_model=UserResponse)
def add_user(
    user : UserCreate,
    db : Session = Depends(get_db)
):  
    try:  
        new_user = create_user(
        db,user.name,
        user.email
    )
    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))
    return new_user


############ GET ALL USERS #########
@router.get("/", response_model=list[UserResponse])
def get_users(
    db : Session = Depends(get_db)
):
    return fetch_users(db)
