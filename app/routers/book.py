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

# Returns all the book in the books table
@router.get("/books", response_model=List[schemas.BookReturn])
def get_books(db: Session = Depends(get_db)):
    data = db.query(models.Book).all()
    return data

# Creates an entry in the books table
@router.post("/books",response_model=schemas.InventoryReturn)
def post_books(book:schemas.Book, db: Session = Depends(get_db)):
    data = models.Book(**book.dict())
    db.add(data)
    db.commit()
    db.refresh(data)
    store_data = data.as_dict()
    
    ## Getting the inventory to return
    b_id = data.id
    inventory = models.Inventory(book_id = b_id,stock= 0 )
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    
    return {"book" : store_data, "stock":inventory.stock}

# returns top 5 Books on the basis of times_issued
@router.get("/books/favourite", response_model=List[schemas.BookReturn])
def get_5_favourite_books(db: Session = Depends(get_db)):

    data = db.query(models.Book).order_by(models.Book.times_issued.desc()).limit(5).all()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Data Not Found")
    
    return data

# Returns all the books of the specified Category
@router.get("/books/category/{category}",response_model=List[schemas.BookReturn])
def get_books_by_category(category:str, db: Session = Depends(get_db)):
    data = db.query(models.Book).filter(models.Book.category == category).all()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Book with Category : {category} could not be found in the database")

    return data

# Returns the book entry of the specified Id
@router.get("/books/{id}",response_model=schemas.BookReturn)
def get_single_book(id:int, db: Session = Depends(get_db)):

    data = db.query(models.Book).filter(models.Book.id == id).first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the database")
    
    return data

# Deletes the book entry of the specified Id

@router.delete("/books/{id}")
def delete_book(id:int, db: Session = Depends(get_db)):
    
    data_query = db.query(models.Book).filter(models.Book.id == id)
    inv_query = db.query(models.Inventory).filter(models.Inventory.book_id == id)
    trans_query = db.query(models.Transaction).filter(models.Transaction.book_id == id)


    data = data_query.first()
    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the database")
    
    ## deleteing all book,inventory,transaction data (fail-safe in case ondelete: CASCADE does not work )
    data_query.delete(synchronize_session= False)
    inv_query.delete(synchronize_session= False)
    trans_query.delete(synchronize_session= False)


    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)

# Updates the book entry of the specified Id
@router.put("/books/{id}",response_model=schemas.BookReturn)
def update_book(id:int, book:schemas.Book, db: Session = Depends(get_db)):
    
    data_query = db.query(models.Book).filter(models.Book.id == id)
    data = data_query.first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the database")
    
    data_query.update(book.dict(),synchronize_session= False)
    db.commit()

    return data_query.first()


