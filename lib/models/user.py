from .base import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    age = Column(Integer)
    