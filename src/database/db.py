import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from utils.logger import setup_logger

logger = setup_logger()


DB_URI = os.getenv("DB_URI")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_mongo_client():
    try:
        client = MongoClient(
            DB_URI,
            username=DB_USERNAME,
            password=DB_PASSWORD,
        )
        # Trigger connection attempt
        client.admin.command("ping")
        logger.info("Connected to database")
        return client
    except ConnectionFailure as err:
        logger.error("Failed to connect to database", exc_info=err)
        return None


def get_db():
    """Get the database instance from the MongoDB client."""
    client = get_mongo_client()
    if client is None:
        raise ConnectionError("Failed to connect to database")
    return client[DB_NAME]  
