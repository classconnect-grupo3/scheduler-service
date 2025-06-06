from sqlalchemy.orm import Session
from src.model.sent_reminder import SentReminder
from datetime import datetime
from src.database.postgres_db import get_postgres_session
from contextlib import contextmanager


@contextmanager
def get_db_session():
    """Context manager for database sessions"""
    session = get_postgres_session()
    try:
        yield session
    finally:
        session.close()


def was_reminder_sent(assignment_id: str, reminder_type: str) -> bool:
    with get_db_session() as db:
        return (
            db.query(SentReminder)
            .filter_by(assignment_id=assignment_id, reminder_type=reminder_type)
            .first()
            is not None
        )


def mark_reminder_sent(assignment_id: str, reminder_type: str):
    with get_db_session() as db:
        reminder = SentReminder(
            assignment_id=assignment_id,
            reminder_type=reminder_type,
            sent_at=datetime.now(),
        )
        db.add(reminder)
        db.commit()
