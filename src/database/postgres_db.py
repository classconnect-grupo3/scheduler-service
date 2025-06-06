import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils.logger import setup_logger

logger = setup_logger()

# PostgreSQL configuration
DATABASE_URL = os.getenv("DATABASE_URL")
Base = declarative_base()


def init_postgres_db():
    """Initialize PostgreSQL database and create tables if they don't exist."""
    try:
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        logger.info("✅ PostgreSQL database initialized successfully")
        return engine
    except Exception as e:
        logger.error(f"❌ Failed to initialize PostgreSQL database: {e}")
        raise


def get_postgres_session():
    """Get a new PostgreSQL database session."""
    engine = init_postgres_db()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()
