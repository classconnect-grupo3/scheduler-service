from schemas.reminder_type import ReminderType, TimeRanges
from sqlalchemy.orm import Session
from datetime import datetime, UTC


def get_reminder_type(due_date: datetime, now: datetime) -> str | None:
    # Ensure both datetimes are timezone-aware
    if due_date.tzinfo is None:
        due_date = due_date.replace(tzinfo=UTC)
    if now.tzinfo is None:
        now = now.replace(tzinfo=UTC)

    delta_hours = (due_date - now).total_seconds() / 3600

    if TimeRanges.HOUR_24_MIN <= delta_hours <= TimeRanges.HOUR_24_MAX:
        return ReminderType.HOUR_24
    elif TimeRanges.HOUR_1_MIN <= delta_hours <= TimeRanges.HOUR_1_MAX:
        return ReminderType.HOUR_1
    return None
