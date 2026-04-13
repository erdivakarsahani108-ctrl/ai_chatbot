from fastapi import APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.complaint import Complaint
from app.models.department import Department
from app.models.state import State
from app.models.district import District
from app.schemas.dashboard import DashboardSummary, SummaryItem, LocationList, StateDistrict

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary", response_model=DashboardSummary)
def dashboard_summary():
    with SessionLocal() as db:
        total = db.query(func.count(Complaint.id)).scalar() or 0
        status_rows = db.query(Complaint.status, func.count(Complaint.id)).group_by(Complaint.status).all()
        dept_rows = (
            db.query(Department.name, func.count(Complaint.id))
            .join(Complaint, Complaint.department_id == Department.id)
            .group_by(Department.name)
            .all()
        )
        state_rows = (
            db.query(State.name, func.count(Complaint.id))
            .join(Complaint, Complaint.state_id == State.id)
            .group_by(State.name)
            .all()
        )

        return DashboardSummary(
            total_complaints=total,
            status_breakdown=[SummaryItem(name=status, value=count) for status, count in status_rows],
            department_breakdown=[SummaryItem(name=dept or "Unknown", value=count) for dept, count in dept_rows],
            state_breakdown=[SummaryItem(name=state, value=count) for state, count in state_rows],
        )


@router.get("/locations", response_model=LocationList)
def location_list():
    with SessionLocal() as db:
        rows = db.query(State.name, District.name).join(District, District.state_id == State.id).all()
        result = [StateDistrict(state=state_name, district=district_name) for state_name, district_name in rows]
        return LocationList(locations=result)
