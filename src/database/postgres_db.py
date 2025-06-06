import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils.logger import setup_logger
from src.model.sent_reminder import (
    SentReminder,
)  # Import the model to ensure it's included

logger = setup_logger()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_postgres_db():
    """Initialize PostgreSQL database and create tables if they don't exist."""
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("✅ PostgreSQL database initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize PostgreSQL database: {e}")
        raise

def get_postgres_session():
    """Get a new PostgreSQL database session."""
    return SessionLocal()
