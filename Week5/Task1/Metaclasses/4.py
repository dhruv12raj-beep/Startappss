# Create a metaclass that automatically logs:

# Student class created
# Employee class created

# into a log file.

import logging

logging.basicConfig(
    filename = "report.log",
    level=logging.INFO,
    format="%(message)s"
)

class MyMeta(type):
    def __new__(cls,name,base,namespace):
        

        logging.info(f"{name} class created")

        return super().__new__(cls,name,base,namespace) 
    

class Student(metaclass = MyMeta):
    pass

class Employee(metaclass= MyMeta):
    pass

