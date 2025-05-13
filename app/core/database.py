import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import settings

# SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL
)

# Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for Object-Relational Mapping models
Base = declarative_base()

# Logger setup
logger = logging.getLogger(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        # Log the error
        logger.error(f"DATABASE ERROR: {e}")
        db.rollback()  # Rollback any changes in case of an error
        raise  # Optionally re-raise the exception
    finally:
        db.close()
