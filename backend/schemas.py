from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class DonorCreate(BaseModel):
    name: str
    blood_group: str
    city: str
    phone: str

class RequestCreate(BaseModel):
    patient_name: str
    blood_group: str
    city: str
    hospital: str
    priority: str

class AppealCreate(BaseModel):
    patient_name: str
    blood_group: str
    city: str
    priority: str