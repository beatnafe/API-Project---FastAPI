from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# Create a PostgreSQL database URL for SQLAlchemy
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()


def get_db():
    '''
    A database session will create a new SQLAlchemy SessionLocal that will be used in a single request, and then close it once the request is finished
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
