from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.complaint import Complaint
from app.models.department import Department
from app.models.state import State
from app.models.district import District
from app.schemas.complaint import ComplaintCreate, ComplaintResponse
from app.services.ai_engine import classify_department, detect_priority, redressal_link_for_department

router = APIRouter(prefix="/complaints", tags=["Complaints"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_ticket_id(db: Session) -> str:
    count = db.query(Complaint).count() + 1
    return f"GRV-{count:04d}"


def get_or_create_state(db: Session, name: str) -> State:
    state = db.query(State).filter(State.name == name).first()
    if state:
        return state
    state = State(name=name, code=name[:3].upper())
    db.add(state)
    db.commit()
    db.refresh(state)
    return state


def get_or_create_district(db: Session, name: str, state: State) -> District:
    district = db.query(District).filter(District.name == name, District.state_id == state.id).first()
    if district:
        return district
    district = District(name=name, code=name[:4].upper(), state_id=state.id)
    db.add(district)
    db.commit()
    db.refresh(district)
    return district


def get_or_create_department(db: Session, name: str) -> Department:
    department = db.query(Department).filter(Department.name == name).first()
    if department:
        return department
    department = Department(
        name=name,
        description=f"Official {name} department for citizen grievance redressal.",
        sla_hours=48,
        contact_url=f"https://example.gov/{name.lower()}-contact",
        redressal_url=redressal_link_for_department(name),
    )
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


@router.post("/", response_model=ComplaintResponse)
def create_complaint(payload: ComplaintCreate, db: Session = Depends(get_db)):
    ticket_id = generate_ticket_id(db)
    state = get_or_create_state(db, payload.state)
    district = get_or_create_district(db, payload.district, state)
    department_name = payload.department if payload.department and payload.department != 'Other' else classify_department(payload.description)
    priority = detect_priority(payload.description, payload.priority)
    department = get_or_create_department(db, department_name)
    redressal_link = redressal_link_for_department(department_name)
    complaint = Complaint(
        ticket_id=ticket_id,
        title=payload.title,
        description=payload.description,
        status="Submitted",
        priority=priority,
        issue_category=payload.issue_category or department_name,
        location=payload.location,
        escalation_level="Level 1",
        assigned_officer="Officer Not Assigned",
        redressal_link=redressal_link,
        department_id=department.id,
        state_id=state.id,
        district_id=district.id,
        created_at=datetime.utcnow(),
    )
    try:
        db.add(complaint)
        db.commit()
        db.refresh(complaint)
    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(status_code=500, detail="Unable to create complaint.") from exc
    return complaint


@router.get("/", response_model=list[ComplaintResponse])
def list_complaints(db: Session = Depends(get_db)):
    return db.query(Complaint).order_by(Complaint.created_at.desc()).all()


@router.get("/{ticket_id}", response_model=ComplaintResponse)
def get_complaint(ticket_id: str, db: Session = Depends(get_db)):
    complaint = db.query(Complaint).filter(Complaint.ticket_id == ticket_id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found.")
    return complaint
