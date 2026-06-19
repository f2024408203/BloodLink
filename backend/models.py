from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

class Donor(Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    blood_group = Column(String)
    city = Column(String)
    phone = Column(String)

class BloodRequest(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    blood_group = Column(String)
    city = Column(String)
    hospital = Column(String)
    priority = Column(String)

class Appeal(Base):
    __tablename__ = "appeals"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    blood_group = Column(String)
    city = Column(String)
    priority = Column(String)