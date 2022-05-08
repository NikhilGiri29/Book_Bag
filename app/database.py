from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import class_mapper
import sqlalchemy
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BaseMixin(object):                                                                                                                                                                             
    def as_dict(self):                                                                                                                                                                               
        result = {}                                                                                                                                                                                  
        for prop in class_mapper(self.__class__).iterate_properties:                                                                                                                                 
            if isinstance(prop, sqlalchemy.orm.ColumnProperty):                                                                                                                                                     
                result[prop.key] = getattr(self, prop.key)                                                                                                                                           
        return result
