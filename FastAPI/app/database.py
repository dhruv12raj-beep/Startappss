from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(bind= engine, autoflush=False, autocommit = False)

class Base(declarative_base):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# https- request -> get_db() -> create postgres session
# ->endpoint uses session -> requuest completed -> finally(execuuted)-> db.close()




