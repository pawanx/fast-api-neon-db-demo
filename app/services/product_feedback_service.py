from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.product_feedback_model import ProductFeedback
from app.models.product_model import Product

def create_product_feedback(
        db :Session,
        product_id : int,
        comment :str,
        rating : int
):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    
    if product.is_archieved:
        raise HTTPException(
            status_code=400,
            detail="Cannot review archieved product"
        )
    
    new_product_feedback = ProductFeedback(
        product_id = product_id,
        comment = comment,
        rating = rating
    )

    db.add(new_product_feedback)
    db.commit()
    db.refresh(new_product_feedback)

    return new_product_feedback
