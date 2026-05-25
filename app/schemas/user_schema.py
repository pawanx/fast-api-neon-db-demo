from pydantic import BaseModel,ConfigDict,EmailStr

# Pydantic model for request body
class UserCreate(BaseModel):
    name : str
    email : EmailStr


# Pydantic model for response body
class UserResponse(BaseModel):
    id : int
    name : str
    email : str

    model_config = ConfigDict(from_attributes=True)
