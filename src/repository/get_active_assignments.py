from datetime import datetime, timedelta, UTC
from sqlalchemy import and_
from src.database.db import get_db
from src.model.assignments import Assignment


def get_active_assignments(hours):
    """Get assignments that are published and due within the next X hours."""
    db = get_db()
    try:
        now = datetime.now(UTC)
        limit = now + timedelta(hours=hours)

        assignments = (
            db.query(Assignment)
            .filter(
                and_(
                    Assignment.status == "published",
                    Assignment.due_date <= limit,
                    Assignment.due_date >= now,
                )
            )
            .all()
        )

        return assignments
    finally:
        db.close()
