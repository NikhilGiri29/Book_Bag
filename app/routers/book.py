from fastapi import APIRouter, Depends, HTTPException, Response , status
from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from ..database import get_db
from typing import List

router = APIRouter(
    prefix = "/api",
    tags=['Books']
)

@router.get("/books", response_model=List[schemas.BookReturn])
def get_books(db: Session = Depends(get_db)):
    data = db.query(models.Book).all()
    return data