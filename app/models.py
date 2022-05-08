from email.policy import default
from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base, BaseMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship,backref

class Book(Base,BaseMixin):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, nullable = False)
    name = Column(String, nullable = False, unique= True)
    author = Column(String, nullable = False)
    category = Column(String, nullable = False)
    times_issued = Column(Integer,nullable = False,default = 0)
    
    

class Student(Base,BaseMixin):
    __tablename__ = "students" 

    id = Column(Integer, primary_key=True, nullable = False)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    roll_number = Column(String, nullable = False, unique =True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, default=func.now())

class Inventory(Base,BaseMixin):
    __tablename__ = "inventory"

    book_id = Column(Integer, ForeignKey("books.id",ondelete="CASCADE"), primary_key = True,nullable = False)
    stock = Column(Integer,nullable = False, default = 0)
    ## TODO: Add Number of Currently issed books

    book = relationship("Book",backref=backref("Inventory", cascade="all,delete") )

class Transaction(Base,BaseMixin):
    __tablename__ = "transaction"

    book_id = Column(Integer, ForeignKey("books.id",ondelete="CASCADE"), primary_key = True,nullable = False)
    student_id = Column(Integer, ForeignKey("students.id",ondelete="CASCADE"), primary_key = True,nullable = False)
    issued_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, default=func.now())

