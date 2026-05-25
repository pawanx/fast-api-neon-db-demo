from pydantic import BaseModel,ConfigDict,Field

class ProductCreate(BaseModel):
    product_name : str
    quantity : int = Field(ge = 0)
    in_stock : bool
    is_archieved : bool


class ProductResponse(BaseModel):
    id : int
    product_name : str
    quantity : int= Field(ge = 0)
    in_stock : bool
    is_archieved : bool

    model_config = ConfigDict(from_attributes=True)