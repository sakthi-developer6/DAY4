from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
import crud

from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Management API")

@app.post("/employees", response_model=schemas.Employee)
def create(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee)

@app.get("/employees", response_model=list[schemas.Employee])
def read_all(db: Session = Depends(get_db)):
    return crud.get_employees(db)

@app.get("/employees/{employee_id}", response_model=schemas.Employee)
def read_one(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db, employee_id)

    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee

@app.put("/employees/{employee_id}", response_model=schemas.Employee)
def update(employee_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    updated = crud.update_employee(db, employee_id, employee)

    if updated is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return updated

@app.delete("/employees/{employee_id}")
def delete(employee_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, employee_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted successfully"}