from datetime import datetime, UTC
from database.mongo_db import get_mongo_session
from src.model.assignments import Assignment
from utils.logger import setup_logger

logger = setup_logger()


def get_active_assignments():
    """Get all published assignments that haven't expired yet."""
    logger.info("Looking for active assignments")
    db = get_mongo_session()
    now = datetime.now(UTC)

    logger.info(f"Searching for published assignments due after {now}")

    query = {
        "status": "published",
        "due_date": {
            "$gt": now,  # greater than now (not expired)
        },
    }

    assignments = db.assignments.find(query)
    results = [Assignment.from_dict(assignment) for assignment in assignments]

    logger.info(f"Found {len(results)} active assignments")

    return results
