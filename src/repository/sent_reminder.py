from sqlalchemy.orm import Session
from src.model.sent_reminder import SentReminder
from datetime import datetime

def was_reminder_sent(db: Session, assignment_id: str, reminder_type: str) -> bool:
    return db.query(SentReminder).filter_by(
        assignment_id=assignment_id,
        reminder_type=reminder_type
    ).first() is not None


def mark_reminder_sent(db: Session, assignment_id: str, reminder_type: str):
    reminder = SentReminder(
        assignment_id=assignment_id,
        reminder_type=reminder_type,
        sent_at=datetime.now()
    )
    db.add(reminder)
    db.commit()
