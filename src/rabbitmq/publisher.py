import pika
import json
import os
from rabbitmq.connection import get_rabbitmq_connection
from utils.logger import setup_logger

logger = setup_logger()

def publish_reminder_event(event_data: dict):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    queue_name = os.getenv("NOTIFICATIONS_QUEUE_NAME")
    channel.queue_declare(queue=queue_name, durable=True)
    
    logger.info("Publicando evento")
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(event_data),
        properties=pika.BasicProperties(
            delivery_mode=2  # persistente
        )
    )
    connection.close()
    logger.info("Conexion con RABBITMQ cerrada")
