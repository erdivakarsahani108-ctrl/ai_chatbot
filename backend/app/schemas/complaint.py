from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ComplaintBase(BaseModel):
    title: str = Field(..., example="Street light not working")
    description: str = Field(..., example="The street light near my house has been out for 5 days.")
    state: str = Field(..., example="Uttar Pradesh")
    district: str = Field(..., example="Lucknow")
    department: Optional[str] = Field(None, example="Electricity")
    priority: Optional[str] = Field(None, example="High")
    issue_category: Optional[str] = Field(None, example="Road repair")
    location: Optional[str] = Field(None, example="Near Sector 3, Indira Nagar")


class ComplaintCreate(ComplaintBase):
    pass


class ComplaintResponse(BaseModel):
    id: int
    ticket_id: str
    title: str
    description: str
    status: str
    priority: str
    issue_category: Optional[str]
    location: Optional[str]
    escalation_level: str
    assigned_officer: Optional[str]
    redressal_link: Optional[str]
    department_name: str
    state_name: str
    district_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
