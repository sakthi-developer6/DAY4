from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    name: str
    department: str
    salary: int
    email: EmailStr

class Employee(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True