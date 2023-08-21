from .base import Base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__ = 'users'