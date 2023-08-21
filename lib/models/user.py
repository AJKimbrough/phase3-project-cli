from sqlalchemy import String, Integer, DateTime, Column, ForeignKey
from .base import Base
from datetime import datetime

class Exercise(Base):
    __tablename__ = 'exercises'

    id = Column(Integer, primary_key=True)
    exercise = Column(String)
    difficulty = Column(String)
    started_at = Column(DateTime, default=datetime.now())
    completed_at = Column(DateTime)