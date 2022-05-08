from fastapi import APIRouter, Depends, HTTPException, Response , status
from sqlalchemy.orm import Session
from .. import models , schemas, utils
from ..database import get_db
from  typing import List
router = APIRouter(
    prefix = "/api",
    tags=['Students']
)
# Returns all the students data in the students table
@router.get("/students",response_model=List[schemas.StudentReturn])
def get_students(db: Session = Depends(get_db)):
    data = db.query(models.Student).all()
    return data

# Creates an entry in the students table
@router.post("/students",response_model=schemas.StudentReturn)
def create_students(student :schemas.StudentCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(student.password)
    student.password =  hashed_password

    data = models.Student(**student.dict())
    db.add(data)
    db.commit()
    db.refresh(data)

    return data

# Returns the student entry of the specified Id
@router.get("/students/{id}",response_model=schemas.StudentReturn)
def get_single_book(id:int, db: Session = Depends(get_db)):

    data = db.query(models.Student).filter(models.Student.id == id).first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Student with id : {id} could not be found in the database")
    
    return data

# Deletes the student entry of the specified Id
@router.delete("/students/{id}")
def delete_student(id:int, db: Session = Depends(get_db)):
    
    data_query = db.query(models.Student).filter(models.Student.id == id)
    data = data_query.first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Student with id : {id} could not be found in the database")
    
    ## If the student has pending Transactions then the student entry cannot be removed
    trans_query = db.query(models.Transaction).filter(models.Transaction.student_id == id).count()
    if trans_query >0:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= f"Student with id : {id} still has books {trans_query} to return")

    data_query.delete(synchronize_session= False)
    db.commit()

    return Response(status_code= status.HTTP_204_NO_CONTENT)

# Update the student entry of the specified Id
@router.put("/students/{id}",response_model=schemas.StudentReturn)
def update_student_contact_info(id:int, student:schemas.StudentUpdate, db: Session = Depends(get_db)):
    
    data_query = db.query(models.Student).filter(models.Student.id == id)
    data = data_query.first()

    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Student with id : {id} could not be found in the database")
    
    data_query.update(student.dict(),synchronize_session= False)
    db.commit()

    return data_query.first()