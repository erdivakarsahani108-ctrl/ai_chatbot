import sys
from pathlib import Path

backend_dir = Path(__file__).resolve().parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import text
from sqlalchemy.exc import OperationalError

from app.api.health import router as health_router
from app.api.complaints import router as complaints_router
from app.api.chat import router as chat_router
from app.api.dashboard import router as dashboard_router
from app.api.config import router as config_router
from app.core.config import settings
from app.core.database import engine, SessionLocal
from app.models.base import Base
from app.models.complaint import Complaint
from app.models.state import State
from app.models.district import District
from app.models.department import Department
from app.models.form_history import FormHistory


def create_app() -> FastAPI:
    app = FastAPI(
        title="GovTech Grievance AI",
        description="A scalable citizens grievance redressal backend built with FastAPI.",
        version="0.1.0",
    )
    
    # Add CORS middleware to allow frontend requests
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(health_router)
    app.include_router(complaints_router)
    app.include_router(chat_router)
    app.include_router(dashboard_router)
    app.include_router(config_router)

    @app.get("/", include_in_schema=False)
    def root():
        return {
            "message": "GovTech Grievance AI backend is running.",
            "health": "/health",
            "complaints": "/complaints",
            "chat": "/chat",
            "dashboard": "/dashboard/summary",
            "docs": "/docs",
        }

    def ensure_database_schema():
        if settings.database_url.startswith("sqlite"):
            db_file = Path(settings.database_url.replace("sqlite:///", ""))
            db_file.parent.mkdir(parents=True, exist_ok=True)
            try:
                with engine.connect() as conn:
                    conn.execute(text("SELECT issue_category FROM complaints LIMIT 1"))
            except OperationalError:
                # If the schema does not exist yet, create it without moving the DB file.
                Base.metadata.create_all(bind=engine)
                return

    def seed_data():
        with SessionLocal() as db:
            if db.query(State).count() == 0:
                states = [
                    ("Uttar Pradesh", "UP", ["Lucknow", "Kanpur", "Varanasi", "Prayagraj", "Ghaziabad", "Agra"]),
                    ("Maharashtra", "MH", ["Mumbai", "Pune", "Nagpur", "Nashik", "Thane", "Aurangabad"]),
                    ("Karnataka", "KA", ["Bengaluru", "Mysore", "Hubli", "Mangalore", "Belgaum", "Davangere"]),
                    ("Delhi", "DL", ["New Delhi", "South Delhi", "North Delhi", "East Delhi", "West Delhi"]),
                    ("Tamil Nadu", "TN", ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem"]),
                    ("West Bengal", "WB", ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri"]),
                    ("Rajasthan", "RJ", ["Jaipur", "Jodhpur", "Udaipur", "Kota", "Bikaner"]),
                    ("Gujarat", "GJ", ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar"]),
                    ("Punjab", "PB", ["Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda"]),
                    ("Haryana", "HR", ["Faridabad", "Gurgaon", "Panipat", "Ambala", "Karnal"]),
                ]
                for name, code, districts in states:
                    state = State(name=name, code=code)
                    db.add(state)
                    db.flush()
                    for district_name in districts:
                        db.add(District(name=district_name, code=district_name[:4].upper(), state_id=state.id))
                db.commit()

            if db.query(Department).count() == 0:
                departments = [
                    ("Police", "Law enforcement and public safety", 24, "https://example.gov/police-redressal"),
                    ("Water Supply", "Water supply and drainage services", 48, "https://example.gov/water-redressal"),
                    ("Electricity", "Electricity supply and meter complaints", 48, "https://example.gov/electricity-redressal"),
                    ("Municipal Corporation", "Civic services, waste management and street repair", 72, "https://example.gov/municipal-redressal"),
                    ("Health Department", "Public health and hospital services", 48, "https://example.gov/health-redressal"),
                    ("Education", "School and educational institution services", 72, "https://example.gov/education-redressal"),
                    ("Road & Highways", "Road construction, maintenance and traffic", 96, "https://example.gov/road-redressal"),
                    ("Transport", "Public transport and vehicle registration", 48, "https://example.gov/transport-redressal"),
                    ("Revenue", "Land records and property grievances", 72, "https://example.gov/revenue-redressal"),
                    ("Urban Development", "Urban planning and development", 96, "https://example.gov/urban-redressal"),
                    ("Agriculture", "Farming and agricultural support", 120, "https://example.gov/agriculture-redressal"),
                    ("Labour", "Worker rights and labor complaints", 72, "https://example.gov/labour-redressal"),
                    ("Social Welfare", "Welfare schemes and benefits", 96, "https://example.gov/welfare-redressal"),
                    ("Banking", "Bank and financial services", 48, "https://example.gov/banking-redressal"),
                    ("RTO", "Vehicle registration and road tax", 48, "https://example.gov/rto-redressal"),
                    ("Postal", "Postal services and courier issues", 72, "https://example.gov/postal-redressal"),
                    ("Fire Safety", "Fire department and safety concerns", 24, "https://example.gov/fire-redressal"),
                    ("Sanitation", "Waste management and cleanliness", 72, "https://example.gov/sanitation-redressal"),
                    ("Parks & Recreation", "Parks, gardens and recreational facilities", 96, "https://example.gov/parks-redressal"),
                    ("Taxation", "Tax related complaints and refunds", 96, "https://example.gov/tax-redressal"),
                    ("Food Safety", "Food standards and hygiene issues", 48, "https://example.gov/food-redressal"),
                    ("Consumer Protection", "Consumer rights and grievances", 72, "https://example.gov/consumer-redressal"),
                    ("Housing", "Public housing and accommodation", 120, "https://example.gov/housing-redressal"),
                    ("Telecom", "Telephone and internet services", 48, "https://example.gov/telecom-redressal"),
                    ("Grievance Redressal", "General citizen complaints", 96, "https://example.gov/grievance-redressal"),
                    ("Sports", "Sports facilities and activities", 120, "https://example.gov/sports-redressal"),
                    ("Tourism", "Tourism facilities and monuments", 96, "https://example.gov/tourism-redressal"),
                    ("Community Development", "Community programs and events", 96, "https://example.gov/community-redressal"),
                    ("Disability Services", "Services for persons with disability", 72, "https://example.gov/disability-redressal"),
                    ("Women Empowerment", "Women safety and empowerment", 48, "https://example.gov/women-redressal"),
                    ("Child Welfare", "Child protection and welfare", 24, "https://example.gov/child-redressal"),
                    ("Disaster Management", "Disaster relief and emergency services", 24, "https://example.gov/disaster-redressal"),
                    ("Environment", "Pollution and environmental concerns", 96, "https://example.gov/environment-redressal"),
                    ("Wildlife", "Wildlife protection and conservation", 120, "https://example.gov/wildlife-redressal"),
                    ("Flood Control", "Flood management and water logging", 24, "https://example.gov/flood-redressal"),
                    ("Public Works", "Public infrastructure and maintenance", 96, "https://example.gov/public-works-redressal"),
                    ("Minority Affairs", "Minority community support", 96, "https://example.gov/minority-redressal"),
                    ("Veterans Affairs", "Military and veteran services", 96, "https://example.gov/veterans-redressal"),
                    ("Pension", "Pension and retirement benefits", 120, "https://example.gov/pension-redressal"),
                    ("Audit", "Financial audit and compliance", 96, "https://example.gov/audit-redressal"),
                    ("Cyber Crime", "Cyber crime and internet fraud", 48, "https://example.gov/cybercrime-redressal"),
                    ("Traffic", "Traffic violations and accidents", 72, "https://example.gov/traffic-redressal"),
                ]
                for name, desc, sla, redressal_url in departments:
                    db.add(Department(name=name, description=desc, sla_hours=sla, contact_url=f"https://example.gov/{name.lower().replace(' & ', '-').replace(' ', '-')}-contact", redressal_url=redressal_url))
                db.commit()

            if db.query(Complaint).count() < 50:
                states = db.query(State).all()
                districts = db.query(District).all()
                departments = db.query(Department).all()
                
                complaint_templates = [
                    ("Street light not working", "Electricity", "The street light on Main Road has been off for several nights.", "High"),
                    ("Water supply interrupted", "Water", "No water supply in our area for the last 2 days.", "High"),
                    ("Road potholes causing accidents", "Municipal", "Deep potholes on the highway need immediate repair.", "Medium"),
                    ("Police response delay", "Police", "Called police for theft but no response for hours.", "High"),
                    ("Hospital lacks basic facilities", "Health", "No doctors available in emergency ward.", "High"),
                    ("Power outage in neighborhood", "Electricity", "Complete blackout for 6 hours yesterday.", "Medium"),
                    ("Sewage overflow on street", "Municipal", "Sewage water flooding the road causing health issues.", "High"),
                    ("Tap water contaminated", "Water", "Water from taps is dirty and smells bad.", "High"),
                    ("Traffic signal malfunction", "Municipal", "Traffic light at junction not working properly.", "Medium"),
                    ("Medical store closed", "Health", "Only pharmacy in area closed for days.", "Medium"),
                    ("Cable theft in area", "Police", "Frequent cable thefts causing power issues.", "Low"),
                    ("Garbage not collected", "Municipal", "Waste piling up for a week.", "Medium"),
                    ("Meter reading incorrect", "Electricity", "Electricity bill much higher than usage.", "Low"),
                    ("Pipe leakage in street", "Water", "Water pipe burst causing water logging.", "Medium"),
                    ("No ambulance service", "Health", "Ambulance not available during emergency.", "High"),
                ]
                
                import random
                for i in range(50):
                    template = random.choice(complaint_templates)
                    dept = db.query(Department).filter(Department.name == template[1]).first()
                    state = random.choice(states)
                    district = random.choice([d for d in districts if d.state_id == state.id])
                    
                    complaint = Complaint(
                        ticket_id=f"GRV-{i+1:04d}",
                        title=template[0],
                        description=template[2],
                        status=random.choice(["Submitted", "In Progress", "Resolved"]),
                        priority=template[3],
                        issue_category=template[1],
                        location=f"{district.name}, {state.name}",
                        escalation_level=random.choice(["Level 1", "Level 2", "Level 3"]),
                        assigned_officer=f"Officer {random.randint(1,10)}",
                        redressal_link=dept.redressal_url if dept else "https://example.gov/grievance",
                        department_id=dept.id if dept else departments[0].id,
                        state_id=state.id,
                        district_id=district.id,
                    )
                    db.add(complaint)
                db.commit()

    @app.on_event("startup")
    def on_startup():
        try:
            ensure_database_schema()
            Base.metadata.create_all(bind=engine)
            seed_data()
        except Exception as e:
            print(f"Startup error: {e}")
            import traceback
            traceback.print_exc()

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
