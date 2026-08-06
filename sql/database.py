from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base 


DATABASE_URL = "postgresql+psycopg://postgres:1234@localhost/company"
engine = create_engine(DATABASE_URL, echo = True)

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

#create_engine: connect python to the database 