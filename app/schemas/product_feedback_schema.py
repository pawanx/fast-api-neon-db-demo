from pydantic import BaseModel,ConfigDict

class ProductFeedbackCreate(BaseModel):
    product_id : int
    comment : str
    rating : int


class ProductFeedbackResponse(BaseModel):
    id : int
    product_id : int
    comment : str
    rating : int

    model_config = ConfigDict(form_attributes=True) 