# Reminder type constants
class ReminderType:
    HOUR_24 = "24h"
    HOUR_1 = "1h"


# Time range constants (in hours)
class TimeRanges:
    # Window sizes
    HOUR_24 = 24.0
    HOUR_1 = 1.0

    # Upper bounds (in minutes)
    UPPER_BOUND_1H = 30  # 30 minutes upper bound for 1h window
    UPPER_BOUND_24H = 30  # 30 minutes upper bound for 24h window

    # Calculated ranges
    HOUR_1_MAX = HOUR_1 + (UPPER_BOUND_1H / 60)  # 1.5 hours (upper bound for 1h window)
    HOUR_1_MIN = 0.0  # 0.0 hours (lower bound for 1h window)
    HOUR_24_MAX = HOUR_24 + (
        UPPER_BOUND_24H / 60
    )  # 24.5 hours (upper bound for 24h window)
    HOUR_24_MIN = HOUR_1_MAX  # 1.5 hours (lower bound for 24h window)
