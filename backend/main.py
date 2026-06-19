from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User, Donor, BloodRequest, Appeal
from schemas import *

app = FastAPI(title="BloodLink API")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "BloodLink Running Successfully"}


# ==========================
# USERS
# ==========================

@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User Registered"}


@app.post("/login")
def login(user: Login, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email,
        User.password == user.password
    ).first()

    if existing_user:
        return {"message": "Login Successful"}

    return {"message": "Invalid Credentials"}


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# ==========================
# DONORS
# ==========================

@app.post("/donors")
def add_donor(donor: DonorCreate, db: Session = Depends(get_db)):

    new_donor = Donor(
        name=donor.name,
        blood_group=donor.blood_group,
        city=donor.city,
        phone=donor.phone
    )

    db.add(new_donor)
    db.commit()

    return {"message": "Donor Added"}


@app.get("/donors")
def get_donors(db: Session = Depends(get_db)):
    return db.query(Donor).all()


@app.get("/donors/{donor_id}")
def get_donor(donor_id: int, db: Session = Depends(get_db)):
    return db.query(Donor).filter(Donor.id == donor_id).first()


@app.put("/donors/{donor_id}")
def update_donor(
        donor_id: int,
        donor: DonorCreate,
        db: Session = Depends(get_db)
):

    existing = db.query(Donor).filter(
        Donor.id == donor_id
    ).first()

    if not existing:
        return {"message": "Donor Not Found"}

    existing.name = donor.name
    existing.blood_group = donor.blood_group
    existing.city = donor.city
    existing.phone = donor.phone

    db.commit()

    return {"message": "Donor Updated"}


@app.delete("/donors/{donor_id}")
def delete_donor(
        donor_id: int,
        db: Session = Depends(get_db)
):

    donor = db.query(Donor).filter(
        Donor.id == donor_id
    ).first()

    if not donor:
        return {"message": "Donor Not Found"}

    db.delete(donor)
    db.commit()

    return {"message": "Donor Deleted"}


# ==========================
# REQUESTS
# ==========================

@app.post("/requests")
def add_request(
        request: RequestCreate,
        db: Session = Depends(get_db)
):

    new_request = BloodRequest(
        patient_name=request.patient_name,
        blood_group=request.blood_group,
        city=request.city,
        hospital=request.hospital,
        priority=request.priority
    )

    db.add(new_request)
    db.commit()

    return {"message": "Request Added"}


@app.get("/requests")
def get_requests(db: Session = Depends(get_db)):
    return db.query(BloodRequest).all()


@app.get("/requests/{request_id}")
def get_request(
        request_id: int,
        db: Session = Depends(get_db)
):
    return db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()


@app.put("/requests/{request_id}")
def update_request(
        request_id: int,
        request: RequestCreate,
        db: Session = Depends(get_db)
):

    existing = db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()

    if not existing:
        return {"message": "Request Not Found"}

    existing.patient_name = request.patient_name
    existing.blood_group = request.blood_group
    existing.city = request.city
    existing.hospital = request.hospital
    existing.priority = request.priority

    db.commit()

    return {"message": "Request Updated"}


@app.delete("/requests/{request_id}")
def delete_request(
        request_id: int,
        db: Session = Depends(get_db)
):

    request = db.query(BloodRequest).filter(
        BloodRequest.id == request_id
    ).first()

    if not request:
        return {"message": "Request Not Found"}

    db.delete(request)
    db.commit()

    return {"message": "Request Deleted"}


# ==========================
# APPEALS
# ==========================

@app.post("/appeals")
def add_appeal(
        appeal: AppealCreate,
        db: Session = Depends(get_db)
):

    new_appeal = Appeal(
        patient_name=appeal.patient_name,
        blood_group=appeal.blood_group,
        city=appeal.city,
        priority=appeal.priority
    )

    db.add(new_appeal)
    db.commit()

    return {"message": "Appeal Added"}


@app.get("/appeals")
def get_appeals(db: Session = Depends(get_db)):
    return db.query(Appeal).all()


@app.get("/appeals/{appeal_id}")
def get_appeal(
        appeal_id: int,
        db: Session = Depends(get_db)
):
    return db.query(Appeal).filter(
        Appeal.id == appeal_id
    ).first()


@app.put("/appeals/{appeal_id}")
def update_appeal(
        appeal_id: int,
        appeal: AppealCreate,
        db: Session = Depends(get_db)
):

    existing = db.query(Appeal).filter(
        Appeal.id == appeal_id
    ).first()

    if not existing:
        return {"message": "Appeal Not Found"}

    existing.patient_name = appeal.patient_name
    existing.blood_group = appeal.blood_group
    existing.city = appeal.city
    existing.priority = appeal.priority

    db.commit()

    return {"message": "Appeal Updated"}


@app.delete("/appeals/{appeal_id}")
def delete_appeal(
        appeal_id: int,
        db: Session = Depends(get_db)
):

    appeal = db.query(Appeal).filter(
        Appeal.id == appeal_id
    ).first()

    if not appeal:
        return {"message": "Appeal Not Found"}

    db.delete(appeal)
    db.commit()

    return {"message": "Appeal Deleted"}