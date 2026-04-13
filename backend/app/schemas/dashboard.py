from pydantic import BaseModel
from typing import List


class SummaryItem(BaseModel):
    name: str
    value: int


class DashboardSummary(BaseModel):
    total_complaints: int
    status_breakdown: List[SummaryItem]
    department_breakdown: List[SummaryItem]
    state_breakdown: List[SummaryItem]


class StateDistrict(BaseModel):
    state: str
    district: str


class LocationList(BaseModel):
    locations: List[StateDistrict]
