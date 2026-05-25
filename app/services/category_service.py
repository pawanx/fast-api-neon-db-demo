from sqlalchemy.orm import Session
from app.models.category_model import Category

def create_category(
        db : Session,
        name : str
):
    new_category = Category(
        name = name
    ) 

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category


######### GET CATEGORY #############

def get_category(
        db : Session
):
    return db.query(Category).all
