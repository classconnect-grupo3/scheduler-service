import time
from retrieve_active_assignments import get_upcoming_assignments
from src.rabbitmq.publisher import publish_reminder_event
from utils.logger import setup_logger

logger = setup_logger()


def main():
    try:
        assignments = get_upcoming_assignments()
        for a in assignments:
            logger.info(f"🔔 Publicando recordatorio: {a['assignment_title']}")
            publish_reminder_event(a)
    except Exception as e:
        logger.error(f"Fallo al verificar recordatorios: {e}")


if __name__ == "__main__":
    logger.info("🚀 Iniciando scheduler")
    main()
