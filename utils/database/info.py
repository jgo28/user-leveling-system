import os
import sqlalchemy as sqla
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import MultipleResultsFound
from dotenv import load_dotenv
from utils.database.models import Base

load_dotenv()

DB_USER = os.getenv('USERNAME')
DB_PASSWORD = os.getenv('PASSWORD')
DB_DATABASE = os.getenv('DATABASE')
DB_HOST = os.getenv('HOST')

e = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
engine = sqla.create_engine(e)
connection = engine.connect()
metadata = sqla.MetaData()    # Used for representing a Table
# Create the table
Base.metadata.create_all(engine)
# Creates a new session to the database based on the described engine
Session = sessionmaker(bind=engine)


def get_session():
    return Session
    