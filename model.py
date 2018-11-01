from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class cello(Base):
   __tablename__ = 'instruments'
   id = Column(Integer, primary_key=True)
   size = Column(Integer)
   color = Column(String)
   price= Column(Integer)

