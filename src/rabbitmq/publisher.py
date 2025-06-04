import pika
import json
import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL")  

def publish_reminder_event(event_data: dict):
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()

    channel.queue_declare(queue="assignment_reminder_queue", durable=True)
    
    channel.basic_publish(
        exchange='',
        routing_key="assignment_reminder_queue",
        body=json.dumps(event_data),
        properties=pika.BasicProperties(
            delivery_mode=2  # persistente
        )
    )

    connection.close()
