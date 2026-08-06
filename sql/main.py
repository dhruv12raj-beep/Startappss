# import psycopg

# connection = psycopg.connect(
#     host= "localhost",
#     dbname ="postgres" ,
#     user= "postgres",
#     password = "1234",
#     port = 5432
# )
# cursor = connection.cursor()
# name = input()
# query ='''
# select * from public.employees where name = %s''',
# (name,)

# cursor.execute(query)
# rows = cursor.fetchall()


# for row in rows:
#     print(row)

# cursor.close()
# connection.close()
# print("connection successfully build!")

#conn : used for transaction data, commit,rollback and connection actions.
# two  to manage data safely : om 


from database import Base, engine, SessionLocal
from models import EmployeeDetails

Base.metadata.create_all(bind = engine)

db = SessionLocal()
db.add(EmployeeDetails(name = "gurman", city="Indore", branch="indore", designation = "python developer" ))

db.commit()

emp = db.query(EmployeeDetails).filter(EmployeeDetails.name=="gurman").first()
print(emp)

# alembic its a sqlachemy  migration tool. it tracks database schema and updates the database witout losing existing data.
# alembic init alembic 
# migrate: alembic upgrade head 