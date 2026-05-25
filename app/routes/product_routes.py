from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.product_schema import (ProductCreate,ProductResponse)

from app.services.product_service import(
    create_product,
    get_products,
    delete_product,
    get_products_by_name,
    archieve_product
)

router = APIRouter(prefix="/products", tags=["Products"])

###### CREATE PRODUCT ##########
@router.post("/", response_model=ProductResponse)
def add_product(
    product : ProductCreate,
    db : Session = Depends(get_db)
):
    try:
        new_product = create_product(
            db,
            product.product_name,
            product.quantity,
            product.in_stock
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return new_product


######## GET PRODUCTS ############
@router.get("/", response_model=list[ProductResponse])
def fetch_products(
        db : Session = Depends(get_db)
):
    products = get_products(db)

    return products

######### DELETE PRODUCTS #######

@router.delete("/{product_id}")
def remove_product(
        product_id : int,
        db: Session = Depends(get_db)
):
    deleted_product = delete_product(
        db, product_id
    )

    if not deleted_product:
        raise HTTPException(
            status_code=404,
            detail="Product not found."
        )
    
    return{
        "message" : "Product deleted successfully"
    }


############ GET PRODUCTS BY NAME ############
@router.get("/search", response_model=list[ProductResponse])
def search_product_ny_name(
     name : str,
    db : Session = Depends(get_db),
):
    return get_products_by_name(
        db,name
    )


############ ARCHIEVE PRODUCT ##################
@router.post("/{product_id}/archieve", response_model=ProductResponse)
def archieve_existing_product(
    product_id : int,
    db : Session = Depends(get_db)
):
    return archieve_product(db,product_id)