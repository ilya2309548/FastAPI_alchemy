from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Annotated
from users.views import router as users_router


app=FastAPI()
app.include_router(users_router, tags=["users"])




@app.get("/")
def root():
    return "yop!"


@app.get("/names/{name}")
def name(name:str):
    return f"hello, {name}"


@app.get("/items/{item_id}")
def items(item_id: Annotated[int, Path(gt=0, le=100000)]):
    return{
        "item":
        {item_id}
    }