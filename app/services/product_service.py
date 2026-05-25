from sqlalchemy.orm import Session
from app.models.product_model import Product
from fastapi import HTTPException

##### Create product ###########

def create_product(
        db : Session,
        product_name : str,
        quantity : int,
        in_stock :bool
):  
    if quantity < 0:
        raise ValueError("Quantity cannot be negative")

    new_product = Product(
        product_name = product_name,
        quantity = quantity,
        in_stock = in_stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


############# GET PRODUCTS #############
def get_products( 
        db :Session
):
    return db.query(Product).all()

########### DELETE PRODUCT #############
def delete_product(
        db :Session,
        product_id : int
):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return None
    
    db.delete(product)
    db.commit()

    return product


############# GET PRODUCTS BY NAME #####################
def get_products_by_name(
        db : Session,
        name : str
):
    return db.query(Product).filter(Product.product_name.ilike(f"%{name}%")).all()


########## ARCHIEVE A PRODUCT ###########################

def archieve_product(
        db : Session,
        product_id : int
):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(
            status_code=400,
            detail="Product not found"
            )
    
    product.is_archieved = True
    db.commit()
    db.refresh(product)