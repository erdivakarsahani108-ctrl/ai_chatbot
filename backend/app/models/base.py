from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Dummy(Base):
    __tablename__ = "dummy"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, default="hello")
