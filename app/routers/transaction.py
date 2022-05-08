import json
from fastapi import APIRouter, Depends, HTTPException, Response , status
from sqlalchemy.orm import Session
from .. import schemas
from .. import models
from ..database import get_db
from .inventory import update_inventory_by_id

router = APIRouter(
    prefix = "/api",
    tags=['Transaction']
)

@router.get("/transaction")
def get_all_transactions(db: Session = Depends(get_db)):
    data = db.query(models.Transaction).all()
    return {"data":data}

@router.get("/transaction/books/{id}")
def get_by_book_id(id:int, db: Session = Depends(get_db)):
    data = db.query(models.Transaction).filter(id == models.Transaction.book_id).all()
    return {"data":data}

@router.get("/transaction/students/{id}")
def get_by_student_id(id:int, db: Session = Depends(get_db)):
    data = db.query(models.Transaction).filter(id == models.Transaction.student_id).all()
    return {"data":data}

@router.post("/transaction")
def issue_book(trans : schemas.Issue_Book, db: Session = Depends(get_db)):
    # Check if book exist
    id =  trans.book_id
    book_query = db.query(models.Book).filter(trans.book_id == models.Book.id)
    book_data = book_query.first()
    if not book_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the database")

    # Check if student exist

    student_query = db.query(models.Student).filter(trans.student_id == models.Student.id)
    student_data = student_query.first()
    if not student_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Student with id : {trans.student_id} could not be found in the database")


    # if does then is it available
    inv = db.query(models.Inventory).filter(id == models.Inventory.book_id).first()
    if not inv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the Inventory, Please Update the Inventory")
    
    if inv.stock == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} is not currently available")

    # Check if the student has 3 books issued
        #later
    books_issued = db.query(models.Transaction).filter(trans.student_id == models.Transaction.student_id).count()
    if books_issued >=3:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail= f"Student with id : {trans.student_id} is already has issued 3 books. Please return books to issue new books.")

    ####
    # -1 in inventory
    dict = {"book_id" : id, "stock": int(inv.stock -1)}

    #plus 1 in number of times book issued
    book_update = book_data.as_dict()
    book_update["times_issued"] += 1
    print(book_update)
    book_query.update(book_update,synchronize_session= False)
    

    # Issue the book by making entry in the table of transaction

    data = models.Transaction(**trans.dict())
    db.add(data)
    update_inventory_by_id(schemas.Inventory.parse_obj(dict),db)
    db.commit()
    db.refresh(data)

    return data

@router.delete("/transaction")
def return_book(trans : schemas.Issue_Book,db: Session = Depends(get_db)):
    
    data_query = db.query(models.Transaction).filter(models.Transaction.book_id == trans.book_id).filter(models.Transaction.student_id == trans.student_id)
    data = data_query.first()
    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Book with id : {trans.book_id} issued to Student with id {trans.student_id} could not be found in the database")
    
    inv = db.query(models.Inventory).filter(trans.book_id == models.Inventory.book_id).first()
    if not inv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Book with id : {id} could not be found in the Inventory, Please Update the Inventory")
    

    data_query.delete(synchronize_session= False)
    
    dict = {"book_id" : trans.book_id, "stock": int(inv.stock +1)}
    update_inventory_by_id(schemas.Inventory.parse_obj(dict),db)

    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)
