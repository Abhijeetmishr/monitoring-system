from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from ..db import database 

class Blog(database.Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)