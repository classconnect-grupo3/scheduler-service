import pika
import json
import os
from rabbitmq.connection import get_rabbitmq_connection
from utils.logger import setup_logger

logger = setup_logger()

def publish_reminder_event(event_data: dict):
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue="assignment_reminder_queue", durable=True)
    
    logger.info("Publicando evento")
    channel.basic_publish(
        exchange='',
        routing_key="assignment_reminder_queue",
        body=json.dumps(event_data),
        properties=pika.BasicProperties(
            delivery_mode=2  # persistente
        )
    )
    connection.close()
    logger.info("Conexion con RABBITMQ cerrada")
