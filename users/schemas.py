from pydantic import BaseModel, EmailStr, Field


class CreateUser(BaseModel):
    id: int = Field(gt=0, lt=1000)
    username: str = Field(..., min_length=3,max_length=20)
    email: EmailStr