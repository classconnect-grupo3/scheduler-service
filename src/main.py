import time
from retrieve_active_assignments import get_upcoming_assignments
from src.rabbitmq.publisher import publish_reminder_event
from utils.logger import setup_logger
from src.database.postgres_db import init_postgres_db

logger = setup_logger()

HOURS_BEFORE_DUE = 6


def main():
    try:
        # Initialize PostgreSQL database
        init_postgres_db()

        assignments = get_upcoming_assignments(HOURS_BEFORE_DUE)
        for a in assignments:
            logger.info(f"🔔 Publishing reminder: {a['assignment_title']}")
            publish_reminder_event(a)
    except Exception as e:
        logger.error(f"❌ Failed to check reminders: {e}")


if __name__ == "__main__":
    logger.info("🚀 Starting scheduler")
    main()
