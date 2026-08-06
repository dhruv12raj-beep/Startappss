from sqlalchemy import Column, Integer ,String
from database import Base 
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key = True)
    name = Column(String(50))

    employees = relationship("EmployeeDetails", back_populates= "Department")


class EmployeeDetails(Base):
    __tablename__ = "employeeDetails"

    id =  Column(Integer,primary_key=True)
    name = Column(String(50))
    city = Column(String(50))
    branch = Column(String(50))
    salary = Column(Integer)
    designation = Column(String(50))

    department = relationship("Department", back_populates="employeeDetails")

    def __repr__(self):
        return f"EmployeeDetails(id={self.id},name={self.name},city = {self.city},branch = {self.branch}, designation = {self.designation})"



