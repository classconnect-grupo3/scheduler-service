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

    # Check if we're in the 1h window [0, 1h + UPPERBOUND_1HR]
    if TimeRanges.HOUR_1_MIN <= delta_hours <= TimeRanges.HOUR_1_MAX:
        return ReminderType.HOUR_1

    # Check if we're in the 24h window [1h + UPPERBOUND_1HR, 24h + UPPERBOUND_24HR]
    elif TimeRanges.HOUR_24_MIN <= delta_hours <= TimeRanges.HOUR_24_MAX:
        return ReminderType.HOUR_24

    logger.info(
        f"Assignment is {delta_hours:.2f} hours from due date - no reminder needed"
    )
    return None
