# Reminder type constants
class ReminderType:
    HOUR_24 = "24h"
    HOUR_1 = "1h"


# Time range constants (in hours)
class TimeRanges:
    # Window sizes
    HOUR_24 = 24.0
    HOUR_1 = 1.0

    # Lower bounds (in minutes)
    LOWER_BOUND_24H = 30  # 30 minutes before 24h window
    LOWER_BOUND_1H = 30  # 30 minutes before due date

    # Calculated ranges
    HOUR_24_MAX = HOUR_24  # 24.0 hours (upper bound for 24h window)
    HOUR_24_MIN = HOUR_24 + (
        LOWER_BOUND_24H / 60
    )  # 24.5 hours (lower bound for 24h window)
    HOUR_1_MAX = HOUR_1  # 1.0 hours (upper bound for 1h window)
    HOUR_1_MIN = HOUR_1 + (LOWER_BOUND_1H / 60)  # 1.5 hours (lower bound for 1h window)
