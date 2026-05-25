from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.dependencies.db import get_db
from app.schemas.product_feedback_schema import (
    ProductFeedbackCreate,ProductFeedbackResponse
)

from app.services.product_feedback_service import create_product_feedback

router = APIRouter(prefix="/product_feedback",tags=["Product Feedback"])

@router.post("/", response_model=ProductFeedbackResponse)
def add_feedback(
    feedback : ProductFeedbackCreate,
    db : Session = Depends(get_db)
    
):
    return create_product_feedback(
        db=db,
        product_id=feedback.product_id,
        comment=feedback.comment,
        rating=feedback.rating
    )
    
    


