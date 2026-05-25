from fastapi import APIRouter,Depends
from app.schemas.category_schema import (CategoryCreate,CategoryResponse)
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.services.category_service import (create_category,get_category)

router = APIRouter(prefix="/categories", tags=["Categories"])


################# Create category ############

@router.post("/", response_model=CategoryResponse)
def add_category(
     category : CategoryCreate,
    db : Session = Depends(get_db),
   
):
    new_category = create_category(
        db,
        category.name
    )

    return new_category
    

############ FETCH CATEGORY #####################
@router.get("/", response_model=list[CategoryResponse])
def fetch_category(
    db : Session
):
    return get_category(db)