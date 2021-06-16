from .database import db
from sqlalchemy import Column, Integer, String

class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)