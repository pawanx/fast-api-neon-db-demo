from fastapi import APIRouter,Depends
from app.schemas.tag_schema import (TagCreate,TagResponse)
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.services.tag_service import (create_tag,get_tags)

router = APIRouter(prefix="/tags", tags=["Tags"])

########### CREATE TAG ROUTER ############
@router.post("/", response_model=TagCreate)
def add_tag(
    tag : TagCreate,
    db : Session = Depends(get_db)
):
    new_tag = create_tag(
        db,
        tag.name
    )

    return new_tag


########### GET NEW TAG ROUTER ##############
@router.get("/", response_model=TagResponse)
def fetch_tags(
    db : Session = Depends(get_db)
):
    return get_tags(db)