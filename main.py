from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel
from core.models import Base, db_helper
from typing import Annotated
from users.views import router as users_router
from api_v1 import router as router_v1

from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users_router, tags=["users"])
app.include_router(router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def root():
    return "yop!"


@app.get("/names/{name}")
def names(name: str):
    return f"hello, {name}"


@app.get("/items/{item_id}")
def items(item_id: Annotated[int, Path(gt=0, le=100000)]):
    return{
        "item":
        {item_id}
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)