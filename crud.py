from sqlalchemy.orm import Session
import models
import schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    new_employee = models.Employee(**employee.model_dump())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(
        models.Employee.id == employee_id
    ).first()

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeCreate):
    emp = get_employee(db, employee_id)

    if emp:
        emp.name = employee.name
        emp.department = employee.department
        emp.salary = employee.salary
        emp.email = employee.email

        db.commit()
        db.refresh(emp)

    return emp

def delete_employee(db: Session, employee_id: int):
    emp = get_employee(db, employee_id)

    if emp:
        db.delete(emp)
        db.commit()

    return emp