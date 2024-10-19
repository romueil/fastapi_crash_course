from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_table, delete_table
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("Database has been cleaned")
    await create_table()
    print("Database is ready to work")
    yield
    print("Shutdown")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
