from src.database.postgres_db import Base, engine


def initialize_database():
    Base.metadata.create_all(bind=engine)
