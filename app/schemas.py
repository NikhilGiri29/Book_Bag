import datetime
from pydantic import BaseModel

class Book(BaseModel):
    name: str
    author : str
    category: str
    

class BookReturn(BaseModel):
    id: int
    name: str
    author : str
    category: str
    times_issued: int

    class Config:
        orm_mode = True


class StudentCreate(BaseModel):
    first_name: str
    last_name : str
    roll_number: str
    password: str

class StudentReturn(BaseModel):
    id: int
    first_name: str
    last_name : str
    roll_number: str
    password: str
    created_at: datetime.datetime

    class Config:
        orm_mode = True
    
class StudentUpdate(BaseModel):
    first_name: str
    last_name : str
    roll_number: str
    

class Inventory(BaseModel):
    book_id: int
    stock : int

class InventoryReturn(BaseModel):
    book : BookReturn
    stock: int
    class Config:
        orm_mode = True
class Issue_Book(BaseModel):
    book_id: int
    student_id   : int