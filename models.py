# models.py
from sqlalchemy import Column, Integer, String
from database import Base

class ClassSectionYear(Base):
    __tablename__  = 'PyTable'
    py_id = Column(Integer, primary_key=True, index=True)
    class_name = Column(String, index=True)
    section = Column(String, index=True)
    year = Column(Integer, index=True)
    count = Column(Integer)