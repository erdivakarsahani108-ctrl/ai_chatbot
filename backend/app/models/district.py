from sqlalchemy import Column, Integer, String, ForeignKey

from app.models.base import Base


class District(Base):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
