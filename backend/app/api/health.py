from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import engine
from app.schemas.status import HealthStatus

router = APIRouter()


@router.get("/health", response_model=HealthStatus)
def health_check():
    database_status = "connected"
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except SQLAlchemyError:
        database_status = "disconnected"

    return HealthStatus(status="ok", database=database_status, redis="pending")
