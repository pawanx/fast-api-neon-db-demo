from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#load env variables
load_dotenv()

#get neon db conncetion string
DATABASE_URL = os.getenv("DATABASE_URL")

# create sqlalchemy engine
# echo=true will log sql queries
engine = create_engine(DATABASE_URL, echo=True)

#Each instance of sessionLocal is db session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#base class for all db models
Base = declarative_base()