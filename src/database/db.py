import os
from pymongo.mongo_client import MongoClient
from pymongo.database import Database

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.scheduler_db  

def get_db() -> Database:
    return db
