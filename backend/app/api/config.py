from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.department import Department

router = APIRouter(prefix="/config", tags=["Configuration"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


ISSUE_CATEGORIES = [
    "Service Disruption",
    "Infrastructure Damage",
    "Safety Hazard",
    "Billing/Payment Issue",
    "Money/Financial Problem",
    "Documentation/Records",
    "Staff Misconduct",
    "Quality/Standard Violation",
    "Unauthorized Access/Trespassing",
    "Environmental Issue",
    "Security Issue",
    "Medical Help",
    "Links/Resources Help",
    "Suggestion/Feedback",
    "Complaint Review",
    "Fraud/Scam Report",
    "Accessibility Issue",
    "Discrimination",
    "Delayed Service",
    "Other"
]

PRIORITIES = ["Low", "Medium", "High"]


@router.get("/categories")
def get_categories():
    """Get all available issue categories"""
    return {
        "categories": ISSUE_CATEGORIES,
        "count": len(ISSUE_CATEGORIES)
    }


@router.get("/priorities")
def get_priorities():
    """Get all priority levels"""
    return {
        "priorities": PRIORITIES
    }


@router.get("/departments")
def get_all_departments(db: Session = Depends(get_db)):
    """Get all departments from database"""
    departments = db.query(Department).all()
    return {
        "departments": [{"id": d.id, "name": d.name, "description": d.description} for d in departments],
        "count": len(departments)
    }


@router.get("/form-options")
def get_form_options(db: Session = Depends(get_db)):
    """Get all form options: departments, categories, priorities"""
    departments = db.query(Department).all()
    return {
        "departments": [d.name for d in departments],
        "categories": ISSUE_CATEGORIES,
        "priorities": PRIORITIES,
        "department_count": len(departments),
        "category_count": len(ISSUE_CATEGORIES)
    }
