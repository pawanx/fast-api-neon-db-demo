from fastapi import Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.feedback_schema import (FeedbackCreate,FeedbackResponse)
from app.services.feedback_service import (create_feedback,get_feedback, remove_feedback)
from typing import Optional

router = APIRouter(prefix="/feedbacks", tags=["Feedbacks"])

############# CREATE FEEDBACK ROUTE ###################
@router.post("/", response_model=FeedbackResponse)
def add_feedback(
    feedback : FeedbackCreate,
    db : Session = Depends(get_db)
):
  try:
    new_feedback = create_feedback(
      db, feedback.name, feedback.comment
   )
  except ValueError as e:
    raise HTTPException(status_code=400, detail=str(e))
  
  return new_feedback

############ Fetch Feedback ##############
@router.get("/", response_model=list[FeedbackResponse])
def fetch_feedbacks(
  name : Optional[str] = None,
  db : Session = Depends(get_db)
):
    feedbacks = get_feedback(
      db,name
    )
    return feedbacks
  
########## DELETE feedback ################
@router.delete("/{feedback_id}")
def delete_feedback(
  feedback_id : int,
  db : Session = Depends(get_db),
):
  deleted_feedback = remove_feedback(
   feedback_id,db
  )
  
  if not deleted_feedback:
    raise HTTPException(
      status_code=404,
      detail= "Feedback not found"
    )
  
  return{
    "message" : "feedback deleted successfully"
  }
