from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app import models
from app.database import engine, get_db, Base

app = FastAPI()


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


class StudentCreate(BaseModel):
    reg_no: str
    name: str
    email: str


@app.get("/health")
def health_check():
    return {"status": "ok", "db": "connected", "student": "2212186"}


@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@app.get("/students/{reg_no}")
def get_student(reg_no: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.reg_no == reg_no).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
