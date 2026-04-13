from sqlalchemy import Column, Integer, String, Text

from app.models.base import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
    sla_hours = Column(Integer, nullable=False, default=48)
    contact_url = Column(String(255), nullable=True)
    redressal_url = Column(String(255), nullable=True)
