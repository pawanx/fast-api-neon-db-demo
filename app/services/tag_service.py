from sqlalchemy.orm import Session
from app.models.tag_model import Tag

######### CREATE TAG SERVICE #############

def create_tag(
        db : Session,
        name : int
):
    new_tag = Tag(
        name = name
    )

    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)

    return new_tag


######### GET TAG SERVICE ##################

def get_tags(
        db :Session
):
    return db.query(Tag).all()
    