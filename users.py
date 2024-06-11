from pydantic import BaseModel,Field
from fastapi import FastAPI
from fastapi import APIRouter
from typing import Annotated


router=APIRouter(prefix="/users")

class CreateUser(BaseModel):
    id: int = Field(gt=0, lt=1000)
    name: str

@router.post("/")
def post_user(user: CreateUser):
    return {"message": f"added {user}"}