from fastapi import FastAPI
from . import models
from .database import engine, SessionLocal
from .routers import book,student

app = FastAPI()


@app.get("/")
def root():
    return {"data" : "Welcome to the root"}

app.include_router(book.router)
app.include_router(student.router)
