from schemas.reminder_type import ReminderType, TimeRanges
from sqlalchemy.orm import Session
from datetime import datetime, UTC
from utils.logger import setup_logger

logger = setup_logger()


def get_reminder_type(due_date: datetime, now: datetime) -> str | None:
    # Ensure both datetimes are timezone-aware
    if due_date.tzinfo is None:
        due_date = due_date.replace(tzinfo=UTC)
    if now.tzinfo is None:
        now = now.replace(tzinfo=UTC)

    delta_hours = (due_date - now).total_seconds() / 3600
    logger.debug(f"Time until due date: {delta_hours:.2f} hours")
    logger.debug(f"Due date: {due_date.isoformat()}")
    logger.debug(f"Current time: {now.isoformat()}")

    # First check if we're in the 1h window (between 1h and 1h30m before due date)
    if TimeRanges.HOUR_1_MIN <= delta_hours <= TimeRanges.HOUR_1_MAX:
        logger.debug(
            f"Assignment is {delta_hours:.2f} hours from due date - sending 1h reminder"
        )
        return ReminderType.HOUR_1

    # Then check if we're in the 24h window (between 0h and 24h30m before due date)
    elif TimeRanges.HOUR_24_MIN <= delta_hours <= TimeRanges.HOUR_24_MAX:
        logger.debug(
            f"Assignment is {delta_hours:.2f} hours from due date - sending 24h reminder"
        )
        return ReminderType.HOUR_24

    logger.debug(
        f"Assignment is {delta_hours:.2f} hours from due date - no reminder needed"
    )
    return None
