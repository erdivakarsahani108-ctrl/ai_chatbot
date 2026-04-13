from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(String(20), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(50), default="Submitted", nullable=False)
    priority = Column(String(20), default="Medium", nullable=False)
    issue_category = Column(String(100), nullable=True)
    location = Column(String(200), nullable=True)
    escalation_level = Column(String(50), default="Level 1", nullable=False)
    assigned_officer = Column(String(120), nullable=True)
    redressal_link = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)

    department = relationship("Department", lazy="joined")
    state = relationship("State", lazy="joined")
    district = relationship("District", lazy="joined")

    @property
    def department_name(self):
        return self.department.name if self.department else "Unknown"

    @property
    def state_name(self):
        return self.state.name if self.state else "Unknown"

    @property
    def district_name(self):
        return self.district.name if self.district else "Unknown"
