from datetime import datetime, timedelta, UTC
from src.database.db import get_db
from src.model.assignments import Assignment
from utils.logger import setup_logger

logger = setup_logger()

def get_active_assignments(hours):
    """Get assignments that are published and due within the next X hours."""
    logger.info("Looking for active assignments")
    db = get_db()
    now = datetime.now(UTC)
    limit = now + timedelta(hours=hours)

    # MongoDB query
    assignments = db.assignments.find(
        {
            "status": "published",
            "due_date": {
                "$lte": limit,  # less than or equal to limit
                "$gte": now,  # greater than or equal to now
            },
        }
    )
    return [Assignment.from_dict(assignment) for assignment in assignments]
