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

    logger.info(
        f"Searching for assignments due between {now.isoformat()} and {limit.isoformat()}"
    )

    logger.info(f"[XDD] Searching for assignments due between {now} and {limit}")

    # MongoDB query using proper datetime objects
    query = {
        "status": "published",
        "due_date": {
            "$lte": limit,  # less than or equal to limit
            "$gte": now,  # greater than or equal to now
        },
    }

    logger.info(f"MongoDB query: {query}")

    assignments = db.assignments.find(query)
    results = [Assignment.from_dict(assignment) for assignment in assignments]

    # Log found assignments
    for assignment in results:
        logger.info(
            f"Found assignment: {assignment.title} due at {assignment.due_date}"
        )

    return results
