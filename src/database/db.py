from pymongo import MongoClient
import os

MONGO_URL = os.getenv("MONGO_URL")
client = MongoClient(MONGO_URL)
db = client.scheduler_db 


def get_db():
    return db
