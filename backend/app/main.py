#backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_db_and_tables, get_session
from .models import Book
from contextlib import asynccontextmanager
from .routers import book
import os


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("アプリを起動します")
    print("データベースを作成します")
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book.router)
@app.get("/")
def get_hello():
    return {"message": "hello docker"}