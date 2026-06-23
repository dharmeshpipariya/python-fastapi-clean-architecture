from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
# from dotenv import load_dotenv

# load_dotenv()

"""You can add a DATABASE_URL environment variable to your .env file to override the default."""
# DATABASE_URL example: postgresql+psycopg2://user:password@localhost/dbname
#DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:password@localhost/tododb")
#DATABASE_URL = os.getenv("DATABASE_URL")

""" Or hard code SQLite here """
DATABASE_URL = "sqlite:///./tododb.db"

""" Or hard code PostgresSQL here """
# DATABASE_URL = "postgresql//postgres:password@localhost/tododb"

engine = create_engine(DATABASE_URL)
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

DbSession = Annotated[Session, Depends(get_db)]