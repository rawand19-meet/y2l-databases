from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(size,color,price):
	cello_object = cello(size=size,color=color,price=price)
	session.add(cello_object)
	session.commit()


def update_product():
	

  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(color):
	session.query(cello).filter_by(
    color=color).delete()
  	session.commit()


delete_product("brown")

  pass

def get_product(id):
  pass
create_product(4,"brown",2000)