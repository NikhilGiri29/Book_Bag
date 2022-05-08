from fastapi import FastAPI
from . import models
from .database import engine, SessionLocal
from .routers import book,student,inventory,transaction

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"data" : "Welcome to da root"}

app.include_router(book.router)
app.include_router(student.router)
app.include_router(inventory.router)
app.include_router(transaction.router)
