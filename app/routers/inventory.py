from fastapi import APIRouter, Depends, HTTPException, Response , status
from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from ..database import get_db
from typing import List

router = APIRouter(
    prefix = "/api",
    tags=['Inventory']
)

@router.get("/inventory")
def get_entire_inventory(db: Session = Depends(get_db)):
    data = db.query(models.Book, models.Inventory.stock).join(models.Inventory,models.Inventory.book_id == models.Book.id).group_by(models.Book.id).all()
    return data

@router.get("/inventory/{id}", response_model=schemas.InventoryReturn)
def get_single_inventory(id:int, db: Session = Depends(get_db)):

    data = db.query(models.Inventory).filter(models.Inventory.book_id == id).first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the database")
    
    book_data = db.query(models.Book).filter(models.Book.id == id).first()
    return {"book" : book_data, "stock":data.stock}


@router.put("/inventory/")
def update_inventory_by_id(inv:schemas.Inventory, db: Session = Depends(get_db)):
    id = inv.book_id
    data_query = db.query(models.Inventory).filter(models.Inventory.book_id == inv.book_id)
    data = data_query.first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the database")

    if inv.stock <0:
        raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE, detail= f"Book Stock cannot be {inv.stock}")
        
    data_query.update(inv.dict(),synchronize_session= False)
    db.commit()
    
    return data_query.first()