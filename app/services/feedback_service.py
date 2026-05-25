from sqlalchemy.orm import Session
from app.models.feedback_model import Feedback

############ CREATE SERVICE ############
def create_feedback(
        db:Session,
        name :str,
        comment : str
    ):

    existing_feedback_name = db.query(Feedback).filter(
        Feedback.name == name
    )

    if existing_feedback_name:
        raise ValueError(f"Feedback from {name} already exists.")


    new_feedback = Feedback(
        name = name,
        comment = comment
    )

    db.add(new_feedback)
    db.commit()
    db.refresh(new_feedback)
    return new_feedback

################ GET FEEDBACK SERVICE ##############
def get_feedback(
        db : Session,
        name : str = None
):
    if name:
        return db.query(Feedback).filter(Feedback.name == name).all()
    
    return db.query(Feedback).all()
   


################# DELETE FEEDBACK ##############
def remove_feedback(
        
        feedback_id : int,
        db : Session
) :
    feedback = db.query(Feedback).filter(Feedback.id == feedback_id).first()
    if not feedback:
        return None
    
    db.delete(feedback)
    db.commit()
    return feedback