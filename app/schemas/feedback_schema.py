from pydantic import BaseModel,ConfigDict

class FeedbackCreate(BaseModel):
    name : str
    comment : str


class FeedbackResponse(BaseModel):
    id : int
    name : str
    comment : str

    model_config = ConfigDict(from_attributes=True)