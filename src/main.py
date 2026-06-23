from fastapi import FastAPI

from .database.core import engine, Base
from .entities.todo import Todo
from .entities.user import User
from .api import register_routes
from src.logging import configure_logging, LogLevels

configure_logging(LogLevels.info)

app = FastAPI()

""" Only uncomment below to create new tables in the database, otherwise the tests will fail if not connected to a real database """

# Base.metadata.create_all(bind=engine)
register_routes(app)