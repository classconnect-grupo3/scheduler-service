from database.postgres_db import init_postgres_db
from scheduler.get_reminder_type import get_reminder_type
from src.retrieve_active_assignments import get_upcoming_assignments
from src.repository.sent_reminder import (
    was_reminder_sent,
    mark_reminder_sent,
)
from src.rabbitmq.publisher import publish_reminder_event
from utils.logger import setup_logger
from datetime import datetime, UTC

logger = setup_logger()


def main():
    now = datetime.now(UTC)
    try:
        # Initialize PostgreSQL database
        init_postgres_db()
        assignments = get_upcoming_assignments()
        for assignment in assignments:
            reminder_type = get_reminder_type(
                due_date=datetime.fromisoformat(assignment["assignment_due_date"]),
                now=now,
            )

            if not reminder_type:
                continue

            if was_reminder_sent(assignment["assignment_id"], reminder_type):
                logger.info(
                    f"⏩ {reminder_type} reminder already sent for {assignment['assignment_id']}"
                )
                continue

            publish_reminder_event(assignment)
            mark_reminder_sent(assignment["assignment_id"], reminder_type)
            logger.info(
                f"✅ Sent {reminder_type} reminder for {assignment['assignment_id']}"
            )

    except Exception as e:
        logger.error(f"Failed to check reminders: {e}")
